from django.contrib import admin

# Register your models here.
from .models import Note
from .models import Comment

admin.site.register(Note)
admin.site.register(Comment)