#
#  Project SmartDjango REST
#  Copyright (c) Alessio Saltarin 2021
#  This software is licensed under MIT license
#

from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=130)
    pages = models.IntegerField()
    isbn = models.CharField(max_length=30)

