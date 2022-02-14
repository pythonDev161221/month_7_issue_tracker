from django.contrib.auth.forms import UserCreationForm


class MyUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")

    def clean(self):
        cleaned_data = super(MyUserCreateForm, self).clean()
        if not cleaned_data['first_name']:
            if not cleaned_data['last_name']:
                raise ValueError('it should be at least first name or last name')
        if not cleaned_data['email']:
            raise ValueError('email is required')
        return cleaned_data

