from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from bank.serializers import User_Serializer, Group_Serializer

class User_Viewsets(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User_Serializer
    serializer_class = User_Serializer

class Group_Viewset(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = Group_Serializer