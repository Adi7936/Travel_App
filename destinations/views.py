from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.




class DestinationListCreate(generics.ListCreateAPIView):
        # authentication_classes = [TokenAuthentication]

        queryset = Destination.objects.all()
        serializer_class = DestinationSerializer
        authentication_classes = [TokenAuthentication] 
        permission_classes = [IsAuthenticated]


class DestinationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication]
        queryset = Destination.objects.all()
        serializer_class = DestinationSerializer
        authentication_classes = [TokenAuthentication] 
        permission_classes = [IsAuthenticated]

    

