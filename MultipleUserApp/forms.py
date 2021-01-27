from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ValidationError
from .models import *

class UserRegister(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    is_role = forms.ModelChoiceField(
        label='Role',
        queryset=Role.objects.all(),
        initial=0)
