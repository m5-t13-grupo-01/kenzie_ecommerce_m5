from django.db import models
import uuid

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(max_length=127, unique=True)
    is_seller = models.BooleanField(default=False)

    address = models.OneToOneField(
        "adresses.Address", on_delete=models.CASCADE, related_name="user"
    )

    cart = models.ForeignKey(
        "carts.Cart", on_delete=models.CASCADE, related_name="user"
    )
