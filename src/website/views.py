from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Snippet, Tag

class IndexView(ListView):
    model = Snippet
    template_name = 'website/index.html'
    ordering = ['-pub_date']
    paginate_by = 12

def snippet_detail(request, slug):
    snippet = get_object_or_404(Snippet, slug__iexact=slug)
    snippet.view_count += 1
    snippet.save()
    return render(request, 'website/snippet_detail.html', context={'snippet': snippet})

class SnippetCreateView(LoginRequiredMixin, CreateView):
    model = Snippet
    fields = ['title', 'slug', 'code', 'description', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SnippetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Snippet
    fields = ['title', 'slug', 'code', 'description', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        snippet = self.get_object()
        if self.request.user == snippet.author:
            return True
        return False


class SnippetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Snippet
    success_url = '/'

    def test_func(self):
        snippet = self.get_object()
        if self.request.user == snippet.author:
            return True
        return False

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'website/tag_detail.html', context={'tag': tag})
