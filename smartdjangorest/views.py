#
#  Project SmartDjango REST
#  Copyright (c) Alessio Saltarin 2021
#  This software is licensed under MIT license
#

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from smartdjangorest.models import Book
import logging


logger = logging.getLogger(__name__)


def index(request):
    """
    Home page
    """
    template = loader.get_template('index.html')
    context = {
        'title': 'SmartDjango REST',
    }
    return HttpResponse(template.render(context, request))


def books(request):
    """
    Books page
    """
    template = loader.get_template('books.html')
    availablebooks = Book.objects.all().order_by('id')
    context = {
        'title': 'SmartDjango REST | Available Books',
        'books': availablebooks,
    }
    return HttpResponse(template.render(context, request))


def addnewbook(request):
    """
    Add new book page
    """
    if request.method == 'POST':
        author = request.POST['author']
        title = request.POST['title']
        pages = request.POST['pages']
        isbn = request.POST['isbn']
        logger.info('Received new book form POST')
        logger.info('Author = ' + author)
        logger.info('Title = ' + title)
        newbook = Book(
            author=author,
            title=title,
            pages=pages,
            isbn=isbn
        )
        newbook.save()
        logger.info('Saved new book with ID=' + str(newbook.id))
        return HttpResponseRedirect('/books')
    else:
        template = loader.get_template('addbook.html')
        context = {
            'title': 'SmartDjango REST | Add new book',
        }
        return HttpResponse(template.render(context, request))

