from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

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
