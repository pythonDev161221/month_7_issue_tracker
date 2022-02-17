from django import forms
from django.core.exceptions import ValidationError

from .models import Issue, Project


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = ['project', 'is_deleted']
        widgets = {
            'type_names': forms.CheckboxSelectMultiple
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['summary'] == cleaned_data['description']:
            raise ValidationError('Description should not duplicate title')
        return cleaned_data


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = []
        widgets = {
            'start_date': forms.SelectDateWidget,
            'finish_date': forms.SelectDateWidget,
        }


class ProjectUserForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['users', ]
        # widgets = {
        #     'users': forms.MultipleChoiceField
        # }