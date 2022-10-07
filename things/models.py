from sys import maxsize
from wsgiref.validate import validator
from django.db.models import (
  Model,
  CharField,
  IntegerField
)
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Thing(Model):
  name = CharField(max_length=30, unique=True, null=False, blank=False)
  description = CharField(max_length=120)
  quantity = IntegerField(validators=[
    MinValueValidator(0), MaxValueValidator(100)
  ])

  def __str__(self) -> str:
    return '{} (x{}): {}'.format(self.name, self.quantity, self.description)
