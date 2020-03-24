# graphql/core/schema.apy
from graphene_django import DjangoObjectType
from web.base_django.apps.customer.models import Customer, Address, Phone, NaturalPerson, LegalPerson, Packing, \
    ItemCategory, Item, ItemVariation


class ClienteType(DjangoObjectType):
    class Meta:
        model = Customer


class EnderecoType(DjangoObjectType):
    class Meta:
        model = Address


class FoneType(DjangoObjectType):
    class Meta:
        model = Phone


class NaturalPersonType(DjangoObjectType):
    class Meta:
        model = NaturalPerson


class PessoaJuridicaType(DjangoObjectType):
    class Meta:
        model = LegalPerson


class EmbalagemType(DjangoObjectType):
    class Meta:
        model = Packing


class CategoriaItemType(DjangoObjectType):
    class Meta:
        model = ItemCategory


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


class ItemVariacaoType(DjangoObjectType):
    class Meta:
        model = ItemVariation