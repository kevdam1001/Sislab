from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CursosAcademicosSerializer, EventosSerializer, AsistenciaAcademicaSerializer, UtilizacionLaboratoriosSerializer, UtilizacionLaboratoriosAsistenciaSerializer
from .models import CursosAcademicos, Eventos, AsistenciaAcademica, UtilizacionLaboratorios, UtilizacionLaboratoriosAsistencia


# IMPORTANTE! PARA CONSULTARLO :
#INGRESAS A http://localhost:8000/requests/api/v1/requests/?no_salon=T-208
class CursosAcademicosView(viewsets.ModelViewSet):
    serializer_class = CursosAcademicosSerializer

    def get_queryset(self):
        # Obtener el valor del parámetro de consulta 'no_salon'
        no_salon_param = self.request.query_params.get('no_salon')

        if no_salon_param:
            # Realizar la consulta personalizada utilizando el parámetro 'no_salon'
            queryset = CursosAcademicos.objects.raw('exec dbo.ConsultaCursosAcademicos @lab = %s', [no_salon_param])
            
        else:
            # Si no se proporciona el parámetro 'no_salon', devolver todos los registros
            queryset = CursosAcademicos.objects.raw("exec dbo.ConsultaCursosAcademicos @lab = ''")
        return queryset

class EventosView(viewsets.ModelViewSet):
    serializer_class = EventosSerializer

    def get_queryset(self):
        # Obtener el valor del parámetro de consulta 'no_salon'
        no_salon_param = self.request.query_params.get('no_salon')

        if no_salon_param:
            # Realizar la consulta personalizada utilizando el parámetro 'no_salon'
            queryset = Eventos.objects.raw('exec dbo.ConsultaEventos @lab = %s', [no_salon_param])
            
        else:
            # Si no se proporciona el parámetro 'no_salon', devolver todos los registros
            queryset = Eventos.objects.raw("exec dbo.ConsultaEventos @lab = ''")
        return queryset

#VIEWS PARA SEDES
class SedesCursosAcademicosView(viewsets.ModelViewSet):
    serializer_class = CursosAcademicosSerializer

    def get_queryset(self):
        # Obtener el valor del parámetro de consulta 'no_salon'
        no_salon_param = self.request.query_params.get('no_salon')

        if no_salon_param:
            # Realizar la consulta personalizada utilizando el parámetro 'no_salon'
            queryset = CursosAcademicos.objects.raw('exec dbo.ConsultaSedesCursosAcademicos @lab = %s', [no_salon_param])
            
        else:
            # Si no se proporciona el parámetro 'no_salon', devolver todos los registros
            queryset = CursosAcademicos.objects.raw("exec dbo.ConsultaSedesCursosAcademicos @lab = ''")
        return queryset

class SedesEventosView(viewsets.ModelViewSet):
    serializer_class = EventosSerializer

    def get_queryset(self):
        # Obtener el valor del parámetro de consulta 'no_salon'
        no_salon_param = self.request.query_params.get('no_salon')

        if no_salon_param:
            # Realizar la consulta personalizada utilizando el parámetro 'no_salon'
            queryset = Eventos.objects.raw('exec dbo.ConsultaSedesEventos @lab = %s', [no_salon_param])
            
        else:
            # Si no se proporciona el parámetro 'no_salon', devolver todos los registros
            queryset = Eventos.objects.raw("exec dbo.ConsultaSedesEventos @lab = ''")
        return queryset

class AsistenciaAcademicaView(viewsets.ModelViewSet):
    serializer_class = AsistenciaAcademicaSerializer

    def get_queryset(self):
        # Obtener el valor del parámetro de consulta 'no_salon'
        no_salon_param = self.request.query_params.get('no_salon')
        day = self.request.query_params.get('day')
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')
        horaInicio = self.request.query_params.get('horaInicio')
        horaFin = self.request.query_params.get('horaFin')
        area = self.request.query_params.get('area')

        queryset = AsistenciaAcademica.objects.raw('exec dbo.AsistenciaAcademica @lab = %s,@day = %s,@month = %s,@year = %s,@horaInicio = %s,@horaFin = %s,@area = %s', [no_salon_param,day,month,year, horaInicio,horaFin,area] )
        return queryset

class UtilizacionLaboratoriosView(viewsets.ModelViewSet):
    serializer_class = UtilizacionLaboratoriosSerializer

    def get_queryset(self):
        # Obtener el valor del parámetro de consulta 'no_salon'
        ciclo = self.request.query_params.get('ciclo')
        area = self.request.query_params.get('area')

        queryset = UtilizacionLaboratorios.objects.raw('exec dbo.UtilizacionLaboratorios @ciclo = %s,@area = %s', [ciclo,area] )
        return queryset

class UtilizacionLaboratoriosAsistenciaView(viewsets.ModelViewSet):
    serializer_class = UtilizacionLaboratoriosAsistenciaSerializer

    def get_queryset(self):
        # Obtener el valor del parámetro de consulta 'no_salon'
        lab = self.request.query_params.get('lab')
        ciclo = self.request.query_params.get('ciclo')

        queryset = UtilizacionLaboratoriosAsistencia.objects.raw('exec dbo.UtilizacionLaboratoriosAsistencia @lab = %s,@ciclo = %s', [lab,ciclo] )
        return queryset
