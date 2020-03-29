from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import CustomerSerializer, AddressSerializer
from .models import Customer, Address
from .forms import LoginForm


class CustomerCreateViewSet(GenericViewSet, mixins.CreateModelMixin,):
    permission_classes = (AllowAny,)
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomerViewSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class AddressViewSet(GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

