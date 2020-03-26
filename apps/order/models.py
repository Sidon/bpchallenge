import uuid
from django.db import models
from django.contrib.auth import get_user_model
from pyUFbr.baseuf import ufbr
from ..customer.models import Customer, Address
from ..item.models import Item
from ..utils import dbutils
from . import OrderStatus

User = get_user_model()
CHOICES_UF = tuple([tuple([u, u]) for u in ufbr.list_uf])
bnull = dict(blank=True, null=True)


class Order(models.Model):
    number = models.CharField('Número do pedido', max_length=8)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='pedidos_cliente')
    ship_address = models.OneToOneField(Address, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField("Ultima Atualização", auto_now=True)
    status = models.CharField(max_length=32, choices=OrderStatus.CHOICES)
    token = models.CharField(max_length=36, unique=True, blank=True)
    # Token of a checkout instance that this order was created from
    checkout_token = models.CharField(max_length=36, blank=True)
    customer_note = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-number']

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):
        self.number = dbutils.next_code(type(self), 'number')
        if not self.token:
            self.token = str(uuid.uuid4())
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='itens_pedido')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='pedidos_item')
    item_name = models.CharField(max_length=386)
    item_sku = models.CharField(max_length=32)
    qt = models.DecimalField('Quantidade', max_digits=11, decimal_places=2)
    gross_price = models.DecimalField('Valor Original', max_digits=11, decimal_places=2)
    net_price = models.DecimalField('Valor liquido', max_digits=11, decimal_places=2)

    class Meta:
        verbose_name = 'Itens de pedido'
        verbose_name_plural = 'Itens de pedidos'

    @property
    def total(self):
        _desconto = self.discount.value if self.discount.kind == 'N' else \
            self.price * (self.discount.value / 100)
        total = self.qt * (self.price - _desconto)
        return total


