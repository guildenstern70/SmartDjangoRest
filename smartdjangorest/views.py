#
#  Project SmartDjango REST
#  Copyright (c) Alessio Saltarin 2021
#  This software is licensed under MIT license
#

from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from rest_framework import viewsets
from rest_framework import permissions
from smartdjangorest.serializers import UserSerializer, GroupSerializer


def index(request):
    template = loader.get_template('index.html')
    context = {
        'title': 'SmartDjango REST',
    }
    return HttpResponse(template.render(context, request))


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
