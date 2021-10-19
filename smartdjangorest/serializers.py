#
#  Project SmartDjango REST
#  Copyright (c) Alessio Saltarin 2021
#  This software is licensed under MIT license
#

from rest_framework import serializers
from smartdjangorest.models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'pages', 'isbn']
