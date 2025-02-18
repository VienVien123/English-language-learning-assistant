from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms.widgets import TextInput, PasswordInput

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(help_text="A valid email address, please.", required=True)
    class Meta:
        model = get_user_model()
        fields = ["first_name","last_name","username", "email", "password1", "password2"]
        def save(self, commit=True):
            user = super(CreateUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user
                
class LoginUserForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))
    