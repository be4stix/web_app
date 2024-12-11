from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(("Название"), max_length=200,default="")
    context = models.CharField(("Текст заметки"), max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    note = models.ForeignKey("Note", on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    context = models.CharField(("Текст комментария"), max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)