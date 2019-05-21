from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.core.validators import validate_email


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class InitForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

    def clean_name(self):
        return "name_passed_value"

    #Field validation

    def clean_email(self):
        email_passed = self.cleaned_data.get("email")
        email_req = "yourdomain.com"
        if not email_req in email_passed:
            raise forms.ValidationError("Email inválido, intente de nuevo")
        return email_passed

    def clean_password(self):
        password_passed = self.cleaned_data.get("password")
        password_req = "..."
        if not password_req in password_passed:
            raise forms.ValidationError("Contraseña inválida, intente de nuevo")
        return password_passed

    #General validation

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        email_passed = cleaned_data.get("email")
        email_req = "yourdomain.com"
        password_passed = cleaned_data.get("password")
        password_req = "..." #Ver con Agus
        if not email_req in email_passed:
            raise forms.ValidationError("Email o contraseña incorrectas")
        return email_passed

