import os
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from apps.customer.views import CustomerViewSet, AddressViewSet, CustomerCreateViewSet
from apps.item.views import ItemViewSet
from apps.order.views import OrderViewSet, OrderItemViewSet
from .views import ReadMeView

__author__ = "Sidon Duarte"
__date__ = "Created by 10/09/18"
__email__ = "sidoncd@gmail.com"

schema_view = get_schema_view(
   openapi.Info(
      title="BRASILPREV Test :: By Sidon 2020",
      default_version='v1',
      description="""The test consists of building a REST API to simulate a virtual store. This store must have a 
      register of its customers, products and orders.
      
      Test and know the endpoints in the "playground" and documentation below.
      """,
      contact=openapi.Contact(email="sidonc@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name='bpchallenge'

router = DefaultRouter()
router.register('add-customer', CustomerCreateViewSet, basename='addcustomer'),
router.register('customer', CustomerViewSet, basename='customer'),
router.register('item', ItemViewSet, basename='itens')
router.register('order', OrderViewSet, basename='orders'),
router.register('orderitem', OrderItemViewSet, basename='orderitens')
router.register('address', AddressViewSet, basename='address')


urlpatterns = [
    path('', ReadMeView.as_view(), {'rst_file': os.path.join(settings.BASE_DIR, 'README.rst')}, name='home'),
    path('readme', ReadMeView.as_view(), {'rst_file': os.path.join(settings.BASE_DIR, 'README.rst')}, name='readme'),
    path('admin/', admin.site.urls),
    path('api/v1/', include((router.urls, 'api-root'),  namespace='api-root')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

admin.site.site_header = "Brasilprev Python Test Admin"
admin.site.site_title = "Brasilprev Python Test Admin Portal"
admin.site.index_title = "Wellcome to BRASILPREV Test"


