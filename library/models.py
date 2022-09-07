from django.db import models
from uuid import uuid4


class Book(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField('Title', max_length=50)
    author = models.CharField('Author', max_length=50)
    release = models.DateField('Release')
    state = models.CharField('State', max_length=50)
    pages = models.PositiveIntegerField('Pages')
    publishing_company = models.CharField('Publishing Company', max_length=50)
    add = models.DateField(auto_now_add=True)
