from django import forms
from django.contrib.auth.models import User
from gym_app.models import User, RegularAthlete, Tracker, Exercise

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password', 'email']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', , 'password', 'email', 'first_name', 'last_name')

class UserEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ChangePasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('password', )

class RegularAthleteForm(forms.ModelForm):

    class Meta:
        model = RegularAthlete
        fields = ('level', 'training_period')

class ExerciseForm(forms.ModelForm):

    class Meta:
        model = Exercise
        fields = ('weight','repetition', 'sets')

