from rest_framework.viewsets import ModelViewSet
from search.models import Search
from search.api.serializers import SearchSerializer
from rest_framework.response import Response


class SearchApiViewSet(ModelViewSet):
    serializer_class = SearchSerializer
    queryset = Search.objects.all()

    def buscar_palabra(self, request, palabra):
        obj_serch = Search(palabra=palabra, resumen='ejemplo2',contenido='ejemplo3')
        obj_serch.save()
        serializer = self.get_serializer(obj_serch)
        return Response(serializer.data)
