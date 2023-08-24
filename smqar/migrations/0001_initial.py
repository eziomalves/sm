# Generated by Django 4.1.7 on 2023-03-15 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concentracao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('c_mp10', models.FloatField()),
                ('c_mp25', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Indice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('indice_mp25', models.FloatField()),
                ('indice_mp10', models.FloatField()),
                ('classificacao', models.PositiveSmallIntegerField()),
            ],
        ),
    ]