from django.shortcuts import render
from rest_framework import generics
from .models import Investments
from .serializers import InvestSerializer

class InvestmentsView(generics.CreateAPIView):
    # get all objects we created in the Investments class (type, name, price etc.)
    queryset = Investments.objects.all()
    serializer_class = InvestSerializer
