# Generated by Django 2.2.6 on 2020-02-16 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200216_0746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pengaduan',
            old_name='status',
            new_name='status_verifikasi',
        ),
    ]
