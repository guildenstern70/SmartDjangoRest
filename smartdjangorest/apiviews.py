#
#  Project SmartDjango REST
#  Copyright (c) Alessio Saltarin 2021
#  This software is licensed under MIT license
#
from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from smartdjangorest.models import Book
from smartdjangorest.serializers import BookSerializer

import logging


logger = logging.getLogger(__name__)


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer


class BooksByAuthor(APIView):
    """
    API endpoint to retrieve books by author
    """
    def get(self, request, author, format=None):
        logger.info('Looking books with author = ' + author)
        filtered_books = _get_book_by_author(author)
        logger.info('Found books: ' + str(filtered_books))
        serializer = BookSerializer(filtered_books, many=True)
        return Response(serializer.data)


def _get_book_by_author(author):
    try:
        return Book.objects.filter(author__contains=author)
    except Book.DoesNotExist:
        raise Http404
