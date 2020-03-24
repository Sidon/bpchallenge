import graphene
from . import types


class OrderQuery:
    order = graphene.Field(
        types.OrderType,
        numero=graphene.String()
    )

    def resolve_order(self, info, **kwargs):
        numero=kwargs.get('numero')
        if numero:
            return types.Order.objects.get(numero=numero)


# class ItemPedidoQuery:
#     item = graphene.Field(
#         types.OrderItem,
#
#     )
