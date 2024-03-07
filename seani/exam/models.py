from django.db import models

from django.contrib.auth.models import User
from career.models import Career
from library.models import Module, Question
class Stage(models.Model):
    stage = models.IntegerField(
        verbose_name = "Etapa",
    )
    application_date = models.DateField(
        verbose_name = "Fecha de Aplicación",
    )

    def month(self):
        months = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre',
                'noviembre','diciembre']
        return months[self.application_date.month]
    month.short_description = 'Mes'

    def year(self):
        return self.application_date.year

    def __str__(self):
        return f"{ self.stage } - { self.month() }{ self.year() }"
    year.short_description = 'Año'
    class Meta:
        verbose_name = "etapa"
        verbose_name_plural = "etapas"

class Exam(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = "Usuario")
    career = models.ForeignKey(Career, on_delete=models.CASCADE, verbose_name = "Carrera")
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, verbose_name = "Etapa")
    modules = models.ManyToManyField(Module, through='ExamModule', verbose_name = "Modulos")
    questions = models.ManyToManyField(Question, through='Breakdow', verbose_name = "Preguntas")
    score = models.FloatField(default=0.0, verbose_name = "Calificación")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación")
    update = models.DateTimeField(auto_now=True, verbose_name = "Fecha de actualización")

    def __str__(self):
        return f"{ self.user } - { self.career } - { self.score }"

    class Meta:
        verbose_name = "examen"
        verbose_name_plural = "exámenes"

class ExamModule(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name = "Examen")
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name = "Modulo")
    activate = models.BooleanField(default=True, verbose_name = "Activo")
    score = models.FloatField(default=0.0, verbose_name = "Calificación")

    def __str__(self):
        return f"{ self.module } - { self.score }"

class Breakdow(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name = "Examen")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name = "Preguntas")
    answer = models.CharField(max_length = 5, default = '-', verbose_name = "Respuesta")
    correct = models.CharField(max_length = 5, default = '-', verbose_name = "Correcto")

    def __str__(self):
        return f"{ self.question } - { self.answer }"