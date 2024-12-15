from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    title = models.CharField(("Название"), max_length=200,default="")
    context = models.TextField(("Текст заметки"), max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)


