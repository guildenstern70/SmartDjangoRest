#
#  Project SmartDjango REST
#  Copyright (c) Alessio Saltarin 2021
#  This software is licensed under MIT license
#

from django.core.management.base import BaseCommand

from smartdjangorest.models import Book


#
# This command is run by
# 'python manage.py populate_db'
#
def _create_books():
    book1 = Book(author='John Doe', title='Lisp', pages=320, isbn='978-3-16-148410-0')
    book1.save()

    book2 = Book(author='Helen McFarrel', title='A Java Walkthrough', pages=678, isbn='978-6-18-999410-0')
    book2.save()

    book3 = Book(author='Renzo Piano', title='Una architettura', pages=223, isbn='978-5-78-343432-1')
    book3.save()

    book4 = Book(author='Mark Twain', title='Tom Sawyer', pages=342, isbn='978-7-32-233322-1')
    book4.save()


def _delete_book(isbn):
    book = Book.objects.filter(isbn=isbn)
    if book:
        book.delete()


def _delete_books():
    _delete_book('978-3-16-148410-0')
    _delete_book('978-6-18-999410-0')
    _delete_book('978-5-78-343432-1')
    _delete_book('978-7-32-233322-1')


class Command(BaseCommand):
    args = ''
    help = 'Populates the Book DB'

    def handle(self, *args, **options):
        _delete_books()
        _create_books()

