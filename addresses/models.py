from django.db import models
import uuid


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    city = models.CharField(max_length=127)
    street = models.CharField(max_length=127)
    number = models.SmallIntegerField()
    zip_code = models.CharField(max_length=8)
    state = models.CharField(max_length=2)
