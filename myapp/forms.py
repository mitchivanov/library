from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserCreateForm(forms.ModelForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label="Номер телефона", widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_address = forms.CharField(label="Адрес", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'user_address']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя",widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={'class': 'form-control'}))

