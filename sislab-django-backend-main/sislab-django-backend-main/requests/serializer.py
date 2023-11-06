from rest_framework import serializers
from .models import CursosAcademicos, Eventos, AsistenciaAcademica, UtilizacionLaboratorios, UtilizacionLaboratoriosAsistencia

#serializer para consulta de cursos academicos
class CursosAcademicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursosAcademicos
        fields = '__all__'

#serializer para consulta de eventos
class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = '__all__'

#serializer para reporte de asistencia academica
class AsistenciaAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsistenciaAcademica
        fields = '__all__'

#serializer para reporte de utilizacion de laboratorios
class UtilizacionLaboratoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilizacionLaboratorios
        fields = '__all__'
        #serializer para reporte de utilizacion de laboratorios

class UtilizacionLaboratoriosAsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilizacionLaboratoriosAsistencia
        fields = '__all__'
