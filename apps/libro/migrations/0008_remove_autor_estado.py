# Generated by Django 2.0.6 on 2019-01-24 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0007_autor_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='estado',
        ),
    ]
