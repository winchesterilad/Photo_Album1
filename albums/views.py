from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Album
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'albums/album_list.html'


class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'albums/album_detail.html'


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['title', 'image']
    template_name = 'albums/create.html'
    success_url = reverse_lazy('album-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['title', 'image']
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album-list')


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'albums/album_confirm_delete.html'
    success_url = reverse_lazy('album-list')
    
def register_view(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('/')

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
    