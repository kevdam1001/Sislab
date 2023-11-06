from django.urls import path, include
from rest_framework import routers
from requests import views

router = routers.DefaultRouter()
router.register(r'cursosacademicos', views.CursosAcademicosView, 'cursosacademicos')
router.register(r'eventos', views.EventosView, 'eventos')
router.register(r'sedescursosacademicos', views.SedesCursosAcademicosView, 'sedescursosacademicos')
router.register(r'sedeseventos', views.SedesEventosView, 'sedeseventos')
router.register(r'asistencia', views.AsistenciaAcademicaView, 'asistencia')
router.register(r'utilizacion', views.UtilizacionLaboratoriosView, 'utilizacion')
router.register(r'utilizacionasistencia', views.UtilizacionLaboratoriosAsistenciaView, 'utilizacionasistencia')

urlpatterns = [
    path('api/v1/', include(router.urls))
]
