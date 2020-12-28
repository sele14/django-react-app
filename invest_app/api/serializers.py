# Translates the model.py class to a json response
from rest_framework import serializers
from .models import Investments

class InvestSerializer(serializers.ModelSerializer):
    """
    Takes the input and serialize it into an acceptable return format
    """
    class Meta:
        model = Investments
        fields = ('id', 'asset_type', 'asset_name', 'asset_name',
                'asset_quantity','asset_price')

class CreateInvestSerializer(serializers.ModelSerializer):
    """
    Take the data from request, and convert to python format we can work with
    """
    class Meta:
        model = Investments
        fields = ('asset_type', 'asset_name', 'asset_name',
                'asset_quantity','asset_price')

