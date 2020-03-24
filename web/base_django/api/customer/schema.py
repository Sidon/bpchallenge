# graphql/core/schema.apy
import graphene
from . import types


# class ClienteQuery:
#     cliente = graphene.Field(
#         types.ClienteType,
#         id=graphene.Int(),
#         identificacao=graphene.String(),
#     )
#
#     all_clientes = graphene.List(types.Customer)
#     def resolve_all_clientes(self, info, **kwargs):
#         return types.Customer.objects.all()
#
#     def resolve_cliente(self, info, **kwargs):
#         id = kwargs.get('id_pessoa')
#         # identificacao = kwargs.get('identificacao')
#
#         if id:
#             pf = types.PessoaFisica.objects.get(cpf=id)
#             if pf:
#                 return pf.cliente
#             pj = types.LegalPerson.objects.get(cnpj=id)
#             if pj:
#                 return pj.cliente
#
#         return None


class EmbalagemQuery:
    embalagem = graphene.Field(
        types.EmbalagemType,
        codigo = graphene.String(),
    )

    def resolve_embalagem(self, info, **kwargs):
        codigo = kwargs.get('codigo')
        if codigo:
            return types.Packing.objects.get(codigo=codigo)
        return None

    all_embalagens = graphene.List(types.EmbalagemType)

    def resolve_all_embalagens(self, info, **kwargs):
        return types.Packing.objects.all()



class CategoriaItemQuery:
    categoria = graphene.Field(
        types.CategoriaItemType,
        codigo=graphene.String()
    )

    def resolve_categoria(self, info, **kwargs):
        codigo = kwargs.get('codigo')
        if codigo:
            return types.ItemCategory.objects.get(codigo=codigo)
        return None

    all_categories = graphene.List(types.CategoriaItemType)

    def resolve_all_categories(self, info, **kwargs):
        return types.ItemCategory.objects.all()


class ItemQuery:
    item = graphene.Field(
        types.ItemType,
        codigo=graphene.String()
    )

    def resolve_item(self, info, **kwargs):
        codigo = kwargs.get('codigo')
        if codigo:
            return types.Item.objects.get(codigo=codigo)
        return None

    all_items = graphene.List(types.ItemType)

    def resolve_all_items(self, info, **kwargs):
        return types.Item.objects.all()


class ItemVariacaoQuery:
    variacao = graphene.Field(
        types.ItemVariacaoType,
        codigo=graphene.String()
    )

    def resolve_variacao(self, info, **kwargs):
        codigo=kwargs.get('codigo')
        if codigo:
            return types.ItemVariation.objects.get(codigo=codigo)
        return None

    all_variacoes = graphene.List(types.ItemVariacaoType)

    def resolve_all_variacoes(self, info, **kwargs):
        return types.ItemVariation.objects.all()

