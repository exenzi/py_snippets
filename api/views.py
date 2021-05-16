from rest_framework import viewsets
from .serializers import SnippetSerializer
from website.models import Snippet

# ViewSets define the view behavior.
class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all().order_by('-pub_date')
    serializer_class = SnippetSerializer

