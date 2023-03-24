from rest_framework import serializers

class ReporteSerializer(serializers.Serializer):
    palabra = serializers.CharField()
    conteo = serializers.IntegerField()
    ultima_fecha = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')