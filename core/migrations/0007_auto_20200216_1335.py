# Generated by Django 2.2.6 on 2020-02-16 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_pengaduan_status_pengaduan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengaduan',
            name='status_pengaduan',
            field=models.BooleanField(default=True),
        ),
    ]
