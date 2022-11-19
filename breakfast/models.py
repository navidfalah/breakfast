from django.db import models
from PIL import Image
from persian_tools import digits, separator
from email.policy import default
from statistics import mode
import uuid
from django.db import models
from django.utils import timezone


khabgah_choices = (
    ('یزد','یزد'),
)


choices_rate = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


def resize(nameOfFile):
    img = Image.open(nameOfFile)
    size = (200, int(img.size[1] * 200 / img.size[0]))
    img.resize(size, Image.ANTIALIAS).save(nameOfFile)
    img.save(nameOfFile)


class BreakFast(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام کالا')
    slug = models.SlugField(allow_unicode=True)
    image = models.ImageField(upload_to='breakfast')
    price = models.IntegerField(verbose_name='قیمت کالا')
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    

    def price_comma(self):
        persian_number = digits.convert_to_fa(self.price)
        persian_number = separator.add(persian_number)  
        return persian_number
    
    def last_comma(self):
        persian_number = digits.convert_to_fa(self.last_price)
        persian_number = separator.add(persian_number) 
        return persian_number

    def persian_off(self):
        off = self.off
        off = digits.convert_to_fa(off)
        return off

    def __str__(self):
        return self.name


class Order(models.Model):
    buyer = models.ForeignKey(to='user_auth.User', on_delete=models.CASCADE)
    BreakFast = models.ForeignKey(BreakFast, on_delete=models.CASCADE,verbose_name='نام محصول')
    total_price = models.PositiveIntegerField(default=0)
    paid = models.BooleanField(default=False, verbose_name='پرداخت شده؟')
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.buyer.mobile


class Invoice(models.Model):
    buyer = models.ForeignKey(to='user_auth.User', on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.buyer.mobile
