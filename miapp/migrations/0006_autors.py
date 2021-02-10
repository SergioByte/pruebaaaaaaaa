# Generated by Django 3.1.4 on 2021-01-27 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0005_auto_20210127_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('sexo', models.BooleanField()),
                ('pais', models.CharField(max_length=150)),
                ('fecha_nacimiento', models.DateField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
