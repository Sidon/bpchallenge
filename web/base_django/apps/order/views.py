from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem


class OrderViewSet(GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderItemViewSet(GenericViewSet,
                       mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
