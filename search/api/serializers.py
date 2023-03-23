from rest_framework.serializers import ModelSerializer
from search.models import Search

class SearchSerializer(ModelSerializer):
    class Meta:
        model = Search
        fields = ['id','palabra','resumen','contenido']