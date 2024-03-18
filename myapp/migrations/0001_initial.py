# Generated by Django 5.0.3 on 2024-03-18 05:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('presupuesto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('alimentacion', models.CharField(max_length=200)),
                ('transporte', models.CharField(max_length=200)),
                ('profesor', models.CharField(max_length=200)),
                ('estado_solicitud', models.CharField(max_length=200, null=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]