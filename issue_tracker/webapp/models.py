from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django.db import models

# Create your models here.
import webapp.models


class BaseStr(models.Model):

    def __str__(self):
        return f'{self.name}'


class Type(BaseStr):
    name = models.CharField(max_length=100, null=False, blank=False, default='Task')


# class IssueType(models.Model):
#     issue = models.ForeignKey('webapp.Issue', related_name='issue_types',
#                               on_delete=models.CASCADE, verbose_name='Задача')
#     type_name = models.ForeignKey('webapp.Type', on_delete=models.CASCADE,
#                                   related_name='type_issues', verbose_name='Тип')
#
#     def __str__(self):
#         return '{} | {}'.format(self.issue, self.type_name)


class Status(BaseStr):
    name = models.CharField(max_length=100, null=False, blank=False, default='New')


class Issue(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False,
                               validators=(MinLengthValidator(5, 'it should not be less then 5 character'),))
    description = models.TextField(max_length=2000, null=True, blank=True,
                                   validators=(MinLengthValidator(1),), )
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT,
                               validators=(), )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # type_names_old = models.ManyToManyField('webapp.Type', related_name='issues_old',
    #                                    through='webapp.IssueType',
    #                                    through_fields=('issue', 'type_name'),
    #                                    blank=True)
    type_names = models.ManyToManyField('webapp.Type', related_name='issues')
    project = models.ForeignKey('webapp.Project', related_name='issues', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.summary}'


class Project(models.Model):
    start_date = models.DateField()
    finish_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return f'{self.name, self.finish_date}'
