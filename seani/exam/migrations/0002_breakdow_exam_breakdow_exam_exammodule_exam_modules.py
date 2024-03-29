# Generated by Django 5.0.2 on 2024-02-29 16:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
        ('exam', '0001_initial'),
        ('library', '0003_alter_module_options_alter_question_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Breakdow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(default='-', max_length=5)),
                ('correct', models.CharField(default='-', max_length=5)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.question')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0.0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('carrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career')),
                ('questions', models.ManyToManyField(through='exam.Breakdow', to='library.question')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.stage')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='breakdow',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam'),
        ),
        migrations.CreateModel(
            name='ExamModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activate', models.BooleanField(default=True)),
                ('score', models.FloatField(default=0.0)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.module')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exam.exam')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='modules',
            field=models.ManyToManyField(through='exam.ExamModule', to='library.module'),
        ),
    ]
