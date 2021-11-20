from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Message
from .srializers import MessageSerializers

# Create your views here.


class MessageViews(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

