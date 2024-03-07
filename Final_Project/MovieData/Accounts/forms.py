from django import forms
from django.contrib.auth.models import User
from . models import Profile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  # This For Additional Field
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']



# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         image = forms.ImageField()
#         model = Profile
#         fields = ['image']



# class UserUpdate(forms.ModelForm):
#     email = forms.EmailField()  # This For Additional Field
#     class Meta:
#         model = User
#         fields = ['username', 'email','first_name','last_name','password']



# class ProfileUpdate(forms.ModelForm):
#     class Meta:
#         image = forms.ImageField()
#         model = Profile
#         fields = ['image']