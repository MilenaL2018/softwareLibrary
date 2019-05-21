from django.core.validators import validate_email
from django.db import models

models.EmailField()

EmailField = models.CharField(validators= [validate_email])

