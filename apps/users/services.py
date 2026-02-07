from django.contrib.auth import get_user_model
from users.models import Customer

#User = get_user_model()

def register_user(*, email: str, password:str):
    """user = User.objects.create(
        email=email,
        #password=set_password(password)
    )"""
    pass
