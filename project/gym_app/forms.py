from django import forms
from django.db import models
from django.contrib.auth.models import User
from gym_app.models import User, Athlete, Tracker, Exercise, PersonalTrainer, BodyScreening
from django.db.models import Q

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))   

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password', 'email']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username','password', 'email', 'first_name', 'last_name')

class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': "form-control"}))
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ChangePasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('password', )


class AthleteForm(forms.ModelForm):

    level = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}), choices=Athlete.LEVELS)
    training_period = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}), choices=Athlete.TRAINING_PERIOD)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}), choices=Athlete.GENDERS)

    class Meta:
        model = Athlete
        fields = ('level', 'training_period', 'gender')

class PersonalTrainerForm(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}), choices=Athlete.GENDERS)
    class Meta:
        model = PersonalTrainer
        fields = ('gender',)

class ExerciseForm(forms.ModelForm):
    weight = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    repetition = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    sets = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    class Meta:
        model = Exercise
        fields = ('weight','repetition', 'sets')

class BodyScreeningForm(forms.ModelForm):
    class Meta:
        model = BodyScreening
        fields = ('triceps', 'biceps', 'subscapular','supraspinale','suprailic',
        'abdominal','chest','thigh','calf','weight','feet', 'inches')

class AthleteSelectForm(forms.Form):
    athlete = forms.ModelChoiceField(queryset=User.objects.filter( Q(groups__name='premium')), empty_label='...', to_field_name='username', widget=forms.Select(attrs={'class': "form-control"}))

class AthleteWorkoutDaySelectForm(forms.Form):
    athlete = forms.ModelChoiceField(queryset=User.objects.filter(Q(groups__name='premium')), empty_label='...', to_field_name='username', widget=forms.Select(attrs={'class': "form-control"}))
    DAYS = (
        ('Whole week', 'Whole week'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    )   
    day = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}), choices=DAYS, 
        required=True, 
        initial='Whole week'
        )

class UserTypeForm(forms.Form):

    GROUPS = (
        ('regular', 'Athlete'),
        ('personal_trainer', 'Personal Trainer'),
    )
    group = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}),choices=GROUPS, required=True, label='User Type')

class PaymentForm(forms.Form):
    owner = forms.CharField(
        max_length=100, 
        required=True, 
        label='Name on Card', 
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder' : "Card Holder's Name"}) 
         )
    
    number = forms.CharField(
        max_length=16, 
        required=True, 
        label='Card Number',
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder' : "Debit/Credit Card Number"})
        )
    ccv = forms.CharField(
        max_length=4, 
        required=True, 
        label='Card CCV',
         widget=forms.TextInput(attrs={'class': "form-control", 'placeholder' : "Security Code"}) 
        )

    MONTHS = (
        ('01', 'Jan (01)'),
        ('02', 'Feb (02)'),
        ('03', 'Mar (03)'),
        ('04', 'Apr (04)'),
        ('05', 'May (05)'),
        ('06', 'Jun (06)'),
        ('07', 'Jul (07)'),
        ('08', 'Aug (08)'),
        ('09', 'Sep (09)'),
        ('10', 'Oct (10)'),
        ('11', 'Nov (11)'),
        ('12', 'Oct (12)'),
        )
    
    YEARS = (
        ('15','2015'),
        ('16','2016'),
        ('17','2017'),
        ('18','2018'),
        ('19','2019'),
        ('20','2020'),
        ('21','2021'),
        ('22','2022'),
        ('23','2023'),
        ('24','2024'),
        ('25','2025'),
        ('26','2026'),
        )

    month = forms.ChoiceField(
        choices=MONTHS, 
        required=True, 
        label='Month',
        widget=forms.Select(attrs={'class': "form-control col-sm-2"})
        )

    year = forms.ChoiceField(
        choices=YEARS, 
        required=True, 
        label='Year',
        widget=forms.Select(attrs={'class': "form-control col-sm-2"}),
        )

class UserGenderForm(forms.Form):
    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
    )   
    gender = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}), choices=GENDERS, 
        required=True, 
        initial='F'
        )




