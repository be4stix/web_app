from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from main.forms import NoteAddForm
from .models import Note
# Create your views here.
def main_view(request):
    form = NoteAddForm(request.POST)
    context ={
        'form':form,
    }
    if request.method == 'POST':
        form = NoteAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')  
        else:
            form = NoteAddForm()
        context = {
            'form': form,
        }
    return render(request, 'main/main.html', context)

def notes(request):
    notes = Note.objects.all()
    context = {
        'notes': notes,
    }
    return render(request, 'main/notes.html', context)

def change_note(request,pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
    }
    if request.method == "POST":
        note.title = request.POST.get('title')
        note.context = request.POST.get('context')
        note.save()
        return redirect("notes")
    
    return render(request, 'main/change_note.html', context)

def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    note.delete()
    return redirect('notes')