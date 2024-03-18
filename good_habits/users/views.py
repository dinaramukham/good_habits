from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import UserSerializer, MyTokenObtainPairSerializer
from .models import User


class MyTokenObtainPairView(TokenObtainPairSerializer):
    serializer_class = MyTokenObtainPairSerializer


# Create your views here.
class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
