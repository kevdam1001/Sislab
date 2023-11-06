# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class CursosAcademicos(models.Model):
    title = models.CharField(db_column='title', max_length=500, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    startDate = models.CharField(db_column='startDate', max_length=500,)  # Field name made lowercase.
    endDate = models.CharField(db_column='endDate', max_length=500,)  # Field name made lowercase.
    id = models.IntegerField(db_column='id', unique=True, primary_key=True)  # Field name made lowercase.
    location = models.CharField(db_column='location', max_length=500, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    rRule = models.CharField(db_column='rRule', max_length=500, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    exDate = models.CharField(db_column='exDate', max_length=500, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    class Meta:
        managed = False

class Eventos(models.Model):
    title = models.CharField(db_column='title', max_length=500, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    startDate = models.CharField(db_column='startDate', max_length=500,)  # Field name made lowercase.
    endDate = models.CharField(db_column='endDate', max_length=500,)  # Field name made lowercase.
    id = models.IntegerField(db_column='id', unique=True, primary_key=True)  # Field name made lowercase.
    location = models.CharField(db_column='location', max_length=500, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    class Meta:
        managed = False

class AsistenciaAcademica(models.Model):
    id = models.IntegerField(db_column='Id', unique=True, primary_key=True)  # Field name made lowercase.
    hora = models.CharField(db_column='Hora', max_length=500, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    carnet = models.CharField(db_column='Carnet', max_length=500,)  # Field name made lowercase.
    salon = models.CharField(db_column='Salon', max_length=500,)  # Field name made lowercase.
    curso = models.CharField(db_column='Curso', max_length=500, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=500, db_collation='Modern_Spanish_CI_AS')
    apellido = models.CharField(db_column='Apellido', max_length=500, db_collation='Modern_Spanish_CI_AS')
    class Meta:
        managed = False

class UtilizacionLaboratorios(models.Model):
    No_Salon = models.CharField(db_column='No_Salon', max_length=500, primary_key=True, unique=True)  # Field name made lowercase.
    Estudiantes = models.CharField(db_column='Estudiantes', max_length=500, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    class Meta:
        managed = False

class UtilizacionLaboratoriosAsistencia(models.Model):
    No_Carnet = models.CharField(db_column='No_Carnet', max_length=500, primary_key=True, unique=True)  # Field name made lowercase.
    Nombre = models.CharField(db_column='Nombre', max_length=500, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    class Meta:
        managed = False
