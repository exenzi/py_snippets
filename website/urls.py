from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('new/', SnippetCreateView.as_view(), name='snippet-create'),
    path('<str:slug>/update', SnippetUpdateView.as_view(), name='snippet-update'),
    path('<str:slug>/delete', SnippetDeleteView.as_view(), name='snippet-delete'),
    path('<str:slug>/', snippet_detail, name='snippet'),
    # path('tags/', tags_list, name="tags_list"),
    path('tag/<str:slug>', tag_detail, name='tag_detail')
]
