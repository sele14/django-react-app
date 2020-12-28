from django.shortcuts import render
from rest_framework import generics
from .models import Investments
from .serializers import InvestSerializer
from .serializers import CreateInvestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class InvestmentsView(generics.CreateAPIView):
    # get all objects we created in the Investments class (type, name, price etc.)
    queryset = Investments.objects.all()
    serializer_class = InvestSerializer

class CreateInvestmentsView(APIView):
    serializer = CreateInvestSerializer
    def post(self, request, format=None):
        # create new session if one is not active
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            asset_type = serializer.data.asset_type
            asset_name = serializer.data.asset_name
            asset_name = serializer.data.asset_name
            asset_quantity = serializer.data.asset_quantity
            asset_price = serializer.data.asset_price

