from rest_framework import serializers
from apps.customer.models import Customer, Address


class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = Customer
        fields = ('id', 'full_name', 'phones', 'email', 'password')

    def create(self, validated_data):
        customer = Customer.objects.create_customer(**validated_data)
        return customer


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id', 'customer', 'street', 'number', 'country', 'zip', 'address_type')

    def create(self, validated_data):
        try:
            address = Address.objects.create(**validated_data)
            return address
        except Exception as e:
            error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
            raise serializers.ValidationError(error)
