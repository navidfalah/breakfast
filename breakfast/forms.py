from django import forms
from .models import BreakFast, Order, Invoice
from user_auth.models import User


class AddOrder(forms.ModelForm):

    class Meta:
        model = Order
        fields = "__all__"


class UpdateOrder(forms.ModelForm):

    class Meta:
        model = Order
        fields = "__all__"


class AddBreakFast(forms.ModelForm):

    class Meta:
        model = BreakFast
        fields = "__all__"


class UpdateBreakFast(forms.ModelForm):

    class Meta:
        model = BreakFast
        fields = "__all__"


class AddInvoice(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = "__all__"


class UpdateInvoice(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = "__all__"

