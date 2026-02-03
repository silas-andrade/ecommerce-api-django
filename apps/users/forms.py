from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from django.forms import ModelForm
from .models import User

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'fullname',
            'phone_number',
            'email',
            'date_of_birth',
            'password1',
            'password2',
        ]
        
        labels = {
            'fullname': _("Full name"),
            'phone_number': _("Phone Number"),
            'email': _("E-mail"),
            'date_of_birth': _("Date of birth"),
            'password1': _("Password"),
            'password2': _("Repeat the password"),
        }
