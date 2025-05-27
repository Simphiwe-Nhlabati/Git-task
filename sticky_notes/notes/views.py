from django.shortcuts import render, get_object_or_404, redirect
from .models import Notes
from .forms import StickyNote


# Create your views here.
def read_sticky_notes(request):
    """
    View to display a list of all notes.
    
    :param request: HTTP request object.
    :return: Rendered template with a list of notes.
    """
    notes_list = Notes.objects.all()
    return render(request, 'notes/home.html', {'sticky_notes': notes_list})


def create_sticky_notes(request):
    """
    View to create a new note.
    
    :param request: HTTP request object.
    :return: Rendered template for creating a new note.
    """
    if request.method == 'POST':
        form = StickyNote(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read_sticky_notes')
    else:
        form = StickyNote(request.POST)
        return render(request, 'notes/form.html', {'form': form, 'action': 'Create'})
        

def update_sticky_notes(request, pk):
    """
    View to update an existing note.
    
    :param request: HTTP request object.
    :param pk: Primary key of the note to be updated.
    :return: Rendered template for updating the specified note.
    """
    sticky_note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        form = StickyNote(request.POST, instance=sticky_note)
        if form.is_valid():
            form.save()
            return redirect('read_sticky_notes')
    else:
        form = StickyNote(instance=sticky_note)
        return render(request, 'notes/form.html', {'form': form, 'action': 'Update'})


def delete_sticky_notes(request, pk):
    """
    View to delete an existing note.
    
    :param request: HTTP request object.
    :param pk: Primary key of the note to be deleted.
    :return: Redirect to the note list after deletion.
    """
    sticky_note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        sticky_note.delete()
        return redirect('read_sticky_notes')
    return render(request, 'notes/delete.html', {'sticky_note': sticky_note})   



