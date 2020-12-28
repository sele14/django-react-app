from django.db import models
from django import forms

ASSET_CHOICES = (
    ("Equities","Equities"),
    ("Fixed Income","Fixed Income"),
    ("Cash & Equiv.","Cash & Equiv."),
    ("Real Estate","Real Estate"),
    ("Commodities","Commodities"),
    ("Derivatives","Derivatives"),
    ("Cryptocurrencies","Cryptocurrencies")
    )

class Investments(models.Model):
    """
    A model that stores the current investments for each user.
    Contains the asset type (bond, stock, etc.), asset name (e.g. AAPL stock), and asset quantity and price.
    """
    asset_type = models.CharField(max_length=100, choices=ASSET_CHOICES, default='Equities')
    asset_name = models.CharField(max_length=20, default="", unique=False)
    asset_quantity = models.IntegerField(default=0)
    asset_price = models.FloatField(default=0)

    # Adding a string representation of the model to display the contents in human-readable form
    def __str__(self):
        return self.asset_type
    