#
#  Project SmartDjango REST
#  Copyright (c) Alessio Saltarin 2021
#  This software is licensed under MIT license
#
from django.http import Http404

from smartdjangorest.models import Book


def get_book_by_author(author_name_part):
    try:
        return Book.objects.filter(author__contains=author_name_part)
    except Book.DoesNotExist:
        raise Http404

