from django.db import IntegrityError

from .models import MyUser


async def create_user(t_name, t_username, t_user_id, username, email, password):
    try:
        return True, MyUser.objects.create_user(
            tele_name=t_name,
            tele_username=t_username,
            tele_user_id=t_user_id,
            username=username,
            email=email,
            password=password
        )
    except IntegrityError:
        return False, MyUser.objects.get(
            username=username,
        )


