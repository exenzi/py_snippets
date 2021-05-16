from rest_framework import serializers
from website.models import Snippet


# Serializers define the API representation.
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ['title', 'code', 'description', 'pub_date']

