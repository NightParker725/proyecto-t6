# Generated by Django 5.0.4 on 2024-05-05 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_event_descripcion_event_titulo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='estado_alimentacion',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='estado_extras',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='estado_transporte',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]