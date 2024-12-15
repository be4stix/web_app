from django import forms
from .models import Note

class NoteAddForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title','context']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        note = super().save(commit=False)
        if commit:
            note.save()
        return note