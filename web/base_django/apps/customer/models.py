import uuid
from django.core.validators import URLValidator
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django_countries.fields import CountryField
from pyUFbr.baseuf import ufbr

CHOICES_UF = tuple([tuple([u, u]) for u in ufbr.list_uf])
bnull = dict(blank=True, null=True)

User = get_user_model()


ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)



class CustomerManager(models.Manager):
    def create_customer(self, email, full_name, phones, password):
        user = self.model(
            email=email,
            full_name=full_name,
            phones=phones
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class Customer(User):
    full_name = models.CharField("Nome completo", max_length=70)
    phones = ArrayField(models.CharField(max_length=15), blank=True)
    objects = CustomerManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=20)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)

    def __str__(self):
        return self.customer.full_name

    class Meta:
        verbose_name_plural = 'Addresses'
