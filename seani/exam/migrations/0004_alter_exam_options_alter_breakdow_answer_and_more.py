# Generated by Django 5.0.2 on 2024-03-07 16:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
        ('exam', '0003_rename_user_exammodule_exam'),
        ('library', '0003_alter_module_options_alter_question_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': 'examen', 'verbose_name_plural': 'exámenes'},
        ),
        migrations.AlterField(
            model_name='breakdow',
            name='answer',
            field=models.CharField(default='-', max_length=5, verbose_name='Respuesta'),
        ),
        migrations.AlterField(
            model_name='breakdow',
            name='correct',
            field=models.CharField(default='-', max_length=5, verbose_name='Correcto'),
        ),
        migrations.AlterField(
            model_name='breakdow',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam', verbose_name='Examen'),
        ),
        migrations.AlterField(
            model_name='breakdow',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.question', verbose_name='Preguntas'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='carrer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career', verbose_name='Carrera'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='modules',
            field=models.ManyToManyField(through='exam.ExamModule', to='library.module', verbose_name='Modulos'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(through='exam.Breakdow', to='library.question', verbose_name='Preguntas'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='score',
            field=models.FloatField(default=0.0, verbose_name='Calificación'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.stage', verbose_name='Etapa'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='update',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='exammodule',
            name='activate',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='exammodule',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam', verbose_name='Examen'),
        ),
        migrations.AlterField(
            model_name='exammodule',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.module', verbose_name='Modulo'),
        ),
        migrations.AlterField(
            model_name='exammodule',
            name='score',
            field=models.FloatField(default=0.0, verbose_name='Calificación'),
        ),
    ]