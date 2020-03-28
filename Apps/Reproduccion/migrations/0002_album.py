# Generated by Django 3.0.3 on 2020-03-28 00:29

import Apps.Reproduccion.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reproduccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('duracion', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('fecha', models.DateField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to=Apps.Reproduccion.models.images_path)),
            ],
        ),
    ]
