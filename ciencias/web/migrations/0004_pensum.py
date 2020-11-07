# Generated by Django 3.1 on 2020-10-27 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_carreras'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pensum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_pensum', models.CharField(max_length=200)),
                ('materia1', models.CharField(max_length=50)),
                ('materia2', models.CharField(max_length=50)),
                ('materia3', models.CharField(max_length=50)),
                ('materia4', models.CharField(max_length=50)),
                ('materia5', models.CharField(max_length=50)),
                ('materia6', models.CharField(max_length=50)),
                ('materia7', models.CharField(max_length=50)),
                ('materia8', models.CharField(max_length=50)),
                ('materia9', models.CharField(max_length=50)),
                ('materia10', models.CharField(max_length=50)),
                ('materia11', models.CharField(max_length=50)),
                ('materia12', models.CharField(max_length=50)),
                ('materia13', models.CharField(max_length=50)),
                ('materia14', models.CharField(max_length=50)),
                ('materia15', models.CharField(max_length=50)),
                ('materia16', models.CharField(max_length=50)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.carreras')),
            ],
        ),
    ]
