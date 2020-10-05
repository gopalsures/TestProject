from django import forms
from testapp.models import Course, Lesson
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'


class LessonForm(forms.ModelForm):
    class Meta:
        model=Lesson
        fields='__all__'
