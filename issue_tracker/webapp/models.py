from django.db import models


# Create your models here.
import webapp.models


class BaseStr(models.Model):

    def __str__(self):
        return f'{self.name}'


class Type(BaseStr):
    name = models.CharField(max_length=100, null=False, blank=False, default='Task')


class Status(BaseStr):
    name = models.CharField(max_length=100, null=False, blank=False, default='New')


class Issue(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=2000, null=True, blank=True)
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT)
    type = models.ForeignKey('webapp.Type', on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.summary}'
