# Generated by Django 4.1 on 2022-10-26 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daftarwilayah', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wilayah',
            name='jangka_waktu',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='wilayah',
            name='kebutuhan',
            field=models.TextField(default=''),
        ),
    ]