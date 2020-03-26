import uuid
from django.db import models

bnull = dict(blank=True, null=True)


class Item(models.Model):
    sku = models.CharField(max_length=20)
    name = models.CharField('Nome do Produto', max_length=100)
    description = models.TextField('Descrição', **bnull)
    bar_code = models.CharField('Código de barras', max_length=13)
    price = models.DecimalField('Preço', max_digits=11, decimal_places=2)

    class Meta:
        verbose_name = 'Item de estoque'
        verbose_name_plural = 'Itens de estoque'

    def __str__(self):
        return self.name


