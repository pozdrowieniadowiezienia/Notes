from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import NoteForm
from .models import Note


# Create your views here.
class NoteListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        notes = Note.objects.filter(author=request.user)
        paginator = Paginator(notes, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'note_list.html', {'page_obj': page_obj})


note_list_view = NoteListView.as_view()


class NoteCreateView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        form = NoteForm()
        return render(request, 'note_form.html', {'form': form})

    def post(self, request):
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('note_list')
        return render(request, 'note_form.html', {'form': form})


note_create_view = NoteCreateView.as_view()


class NoteDetailView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, pk):
        note = Note.objects.get(pk=pk, author=request.user)
        return render(request, 'note_detail.html', {'note': note})


note_detail_view = NoteDetailView.as_view()
