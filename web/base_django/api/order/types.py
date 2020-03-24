from graphene_django import DjangoObjectType
from web.base_django.apps.order.models import Order, OrderItem, DiscountCode

class OrderType(DjangoObjectType):
    class Meta:
        model = Order

class OrderItemType(DjangoObjectType):
    class Meta:
        model = OrderItem

class DiscountCodeType(DjangoObjectType):
    class Meta:
        model = DiscountCode

