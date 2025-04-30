from django import forms
from django.contrib.auth.forms import UserCreationForm

from prjctapp.models import LoginView, Giver, Seeker, JobVacancy, ApplyForJob


class LoginUser(UserCreationForm):
    username=forms.CharField()
    password1 = forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password",widget=forms.PasswordInput)

    class Meta:
        model =LoginView
        fields =("username","password1","password2")

class GiverForm(forms.ModelForm):
    class Meta:
        model = Giver
        fields =("name","email","phone_no","profile_pic")

class SeekerForm(forms.ModelForm):
    class Meta:
        model = Seeker
        fields = ("name", "email", "contact_no", "profile_pic")


class JobsForm(forms.ModelForm):
    class Meta:
        model = JobVacancy
        fields = ("job_name","job_location","job_time_shift","job_discription","responsibilities","qualifications","experience_requiered","company_details","salary")

class ApplyForm(forms.ModelForm):
    class Meta:
        model = ApplyForJob
        fields =("name","Email","Resume","portifolio_link","cover_letter")


