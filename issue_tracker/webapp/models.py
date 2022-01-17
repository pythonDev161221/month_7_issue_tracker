from django.db import models

# Create your models here.
import webapp.models


class BaseStr(models.Model):

    def __str__(self):
        return f'{self.name}'


class Type(BaseStr):
    name = models.CharField(max_length=100, null=False, blank=False, default='Task')


class IssueType(models.Model):
    issue = models.ForeignKey('webapp.Issue', related_name='issue_types',
                              on_delete=models.CASCADE, verbose_name='Задача')
    type_name = models.ForeignKey('webapp.Type', on_delete=models.CASCADE,
                                  related_name='type_issues', verbose_name='Тип')

    def __str__(self):
        return '{} | {}'.format(self.issue, self.type_name)


class Status(BaseStr):
    name = models.CharField(max_length=100, null=False, blank=False, default='New')


class Issue(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=2000, null=True, blank=True)
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT)
    type = models.ForeignKey('webapp.Type', on_delete=models.PROTECT, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    type_names = models.ManyToManyField('webapp.Type', related_name='issues',
                                       through='webapp.IssueType',
                                       through_fields=('issue', 'type_name'),
                                       blank=True)

    def __str__(self):
        return f'{self.summary}'
