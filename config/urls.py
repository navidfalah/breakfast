from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
# from blog.views import  go_to_gateway_shop, callback_gateway_shop
# from azbankgateways.urls import az_bank_gateways_urls
# admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('breakfast.urls')),
    path('', include('user_auth.urls')),
    # path('bankgateways/', az_bank_gateways_urls()),
    # path('go-to-shop/', go_to_gateway_shop, name='go-to-shop'),
    # path('callback_shop/', callback_gateway_shop, name='callback-shop'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
