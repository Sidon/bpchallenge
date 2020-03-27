from rest_framework import serializers
from apps.item.models import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'sku', 'name', 'description', 'bar_code', 'price')

    # def create(self, validated_data):
    #     item = Item.objects.create(**validated_data)
    #     return item
