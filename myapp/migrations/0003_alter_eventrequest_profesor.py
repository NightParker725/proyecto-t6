# Generated by Django 5.0.2 on 2024-03-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_eventrequest_estado_solicitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventrequest',
            name='profesor',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
