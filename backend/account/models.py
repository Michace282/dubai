from django.db import models
from backend.mixin import TimeStampedModel
import uuid


class Guest(TimeStampedModel):
    uuid = models.UUIDField(verbose_name='UUID', default=uuid.uuid4, unique=True)
