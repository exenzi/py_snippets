from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from functools import reduce

from .models import Snippet, Tag

class IndexView(ListView):
    model = Snippet
    template_name = 'website/index.html'
    ordering = ['-pub_date']
    paginate_by = 3


class SearchView(ListView):
    model = Snippet
    template_name = 'website/search_results.html'
    ordering = ['-pub_date']
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q').strip()
        query_list = query.split()
        q_list = []
        for q in query_list:
            q_list.append(Q(title__icontains=q) | Q(code__icontains=q))
        object_list = Snippet.objects.filter(*q_list).order_by('-pub_date')
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q').strip()
        query_list = context['query'].split()
        context['q'] = f"q={'+'.join(query_list)}&"
        return context

def snippet_detail(request, slug):
    snippet = get_object_or_404(Snippet, slug__iexact=slug)
    snippet.view_count += 1
    snippet.save()
    return render(request, 'website/snippet_detail.html', context={'snippet': snippet})

class SnippetCreateView(LoginRequiredMixin, CreateView):
    model = Snippet
    fields = ['title', 'code', 'description', 'tags']

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
