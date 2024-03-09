from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


# Create your views here.
class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
