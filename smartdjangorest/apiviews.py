#
#  Project SmartDjango REST
#  Copyright (c) Alessio Saltarin 2021
#  This software is licensed under MIT license
#
from rest_framework import viewsets
from rest_framework.response import Response

from smartdjangorest.dao import get_book_by_author
from smartdjangorest.models import Book
from smartdjangorest.serializers import BookSerializer
from rest_framework.decorators import action

import logging


logger = logging.getLogger(__name__)


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows books to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer

    @action(methods=['get'], detail=False, url_path='by_author/(?P<author>[^/.]+)')
    def get_by_author(self, request, author):
        """
        API endpoint to get books by author
        """
        logger.info('Looking books with author = ' + author)
        filtered_books = get_book_by_author(author)
        logger.info('Found books: ' + str(filtered_books))
        serializer = BookSerializer(filtered_books, many=True)
        return Response(serializer.data)
