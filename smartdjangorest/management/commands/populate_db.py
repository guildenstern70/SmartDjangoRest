#
#  Project SmartDjango REST
#  Copyright (c) Alessio Saltarin 2021
#  This software is licensed under MIT license
#

from django.core.management.base import BaseCommand
from smartdjangorest.models import Book


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Populates the Book DB'

    def _create_tags(self):
        book1 = Book(author='John Doe', title='Lisp', pages=320, isbn='978-3-16-148410-0')
        book1.save()

        book2 = Book(author='Helen McFarrel', title='A Java Walkthrough', pages=678, isbn='978-6-18-999410-0')
        book2.save()

        book3 = Book(author='Renzo Piano', title='Una architettura', pages=223, isbn='978-5-78-343432-1')
        book3.save()

    def handle(self, *args, **options):
        self._create_tags()

