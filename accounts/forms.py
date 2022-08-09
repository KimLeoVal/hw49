from django import forms
from django.contrib.auth import login
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect


class MyUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label="Пароль", strip=False, required=True, widget=forms.PasswordInput
                               )
    password2 = forms.CharField(label="Подтвердите пароль", required=True, widget=forms.PasswordInput,
                                       strip=False)
    email = forms.EmailField(max_length=200, required=True, validators=[validate_email])
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']
        field_classes = {'username': UsernameField}

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        print(first_name,last_name)
        if not first_name and not last_name:
            raise ValidationError("Заполните имя или фамилию")

    # def CustomValidator(self,form,request):
    #     form=MyUserCreationForm(data=request.Post)
    #     first_name = cleaned_data.get('first_name')
    #     last_name = cleaned_data.get('last_name')
    #     if not first_name and last_name:
    def form_valid(self, form):
        first_name = form.get('first_name')
        last_name = form.get('last_name')
        if  first_name=='' and last_name=='':
            print(first_name,last_name)
            raise ValidationError("Заполните имя или фамилию")
        user = form.save()

        login(self.request, user)

        return redirect(self.get_success_url())


    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
