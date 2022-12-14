# Generated by Django 4.0.2 on 2022-05-17 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estreno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('año', models.IntegerField()),
                ('director', models.CharField(max_length=40)),
                ('puntaje', models.FloatField()),
                ('reseña', models.CharField(max_length=240)),
            ],
        ),
    ]
