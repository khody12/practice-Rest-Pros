from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount', # within our actual model, this is called get_discount, but we used SerializeMethodField and a function to change what is shown to 'my_discount'
        ]

    def get_my_discount(self, obj):
        return obj.get_discount()