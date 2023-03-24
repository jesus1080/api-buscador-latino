from rest_framework.viewsets import ModelViewSet
from search.models import Search
from search.api.serializers import SearchSerializer
from search.api.report_serializers import ReporteSerializer
from rest_framework.response import Response
from django.db.models import Count, Max
import wikipediaapi


class SearchApiViewSet(ModelViewSet):
    serializer_class = SearchSerializer
    queryset = Search.objects.all()
    wiki = wikipediaapi.Wikipedia(
            language='es',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )
   

    def buscar_palabra(self,request,palabraIn):
       
        page = self.wiki.page(palabraIn)
        obj_serch = Search(palabra=palabraIn,resumen=page.summary,contenido=page.text)
        obj_serch.save()
        serializer = self.get_serializer(obj_serch)
        return Response(serializer.data)
    
    def reporte(self,request):

        queryReporte = Search.objects.values('palabra').annotate(conteo=Count('palabra'), ultima_fecha=Max('create_at')).order_by('-conteo', '-ultima_fecha')
        serializer = ReporteSerializer(queryReporte, many=True)
        return Response(serializer.data)
