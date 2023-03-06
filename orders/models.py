from django.db import models
import uuid


class StatusChoices(models.TextChoices):
    PEDIDO_REALIZADO = "Pedido Realizado"
    EM_ANDAMENTO = "Em Andamento"
    ENTREGUE = "Entregue"

class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(max_length=127, choices=StatusChoices.choices, default=StatusChoices.PEDIDO_REALIZADO)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="orders",
    )