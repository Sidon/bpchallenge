from rest_framework import serializers
from ...apps.order.models import Order, OrderItem, Address
from ...apps.item.models import Item


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'customer', 'ship_address', 'customer_note')

    def create(self, validated_data):
        try:
            order = Order.objects.create(**validated_data)
            return order
        except Exception as e:
            error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
            raise serializers.ValidationError(error)


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'item', 'qt', 'gross_price', 'net_price')

    def create(self, validated_data):
        try:
            order_item = OrderItem.objects.create(**validated_data)
            return order_item
        except Exception as e:
            error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
            raise serializers.ValidationError(error)


        # if Order.objects.filter(pk=validated_data['order']).exists() and Item.objects.filter(pk=validated_data['item']):
        #     order_item = OrderItem.objects.create(**validated_data)
        #     return order_item


