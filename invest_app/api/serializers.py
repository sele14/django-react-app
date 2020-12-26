# Translates the model.py class to a json response
from rest_framework import serializers
from .models import Investments

class InvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investments
        fields = ('id', 'asset_type', 'asset_name', 'asset_name',
                'asset_quantity','asset_price')
