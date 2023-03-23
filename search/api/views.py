from rest_framework.viewsets import ModelViewSet
from search.models import Search
from search.api.serializers import SearchSerializer
from rest_framework.response import Response
import wikipediaapi


class SearchApiViewSet(ModelViewSet):
    serializer_class = SearchSerializer
    queryset = Search.objects.all()
   

    def buscar_palabra(self,request,palabraIn):
        wiki = wikipediaapi.Wikipedia(
            language='es',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )
            
        
        page = wiki.page(palabraIn)
        obj_serch = Search(palabra=palabraIn,resumen=page.summary,contenido=page.text)
        obj_serch.save()
        serializer = self.get_serializer(obj_serch)
        return Response(serializer.data)
