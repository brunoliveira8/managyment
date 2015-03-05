from django import forms
from django.contrib.auth.models import User
from gym_app.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
