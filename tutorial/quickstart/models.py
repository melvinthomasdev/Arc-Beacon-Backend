from django.db import models

# Create your models here.
from django.contrib.auth.models import User, Group
from rest-rest_framework import viewsets
from .serilaizers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class= UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset=Group.onjects.all()
    serializer_class = GroupSerializer
