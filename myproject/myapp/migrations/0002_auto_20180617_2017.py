# Generated by Django 2.0.6 on 2018-06-17 20:17

from django.db import migrations, models
import myproject.myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='', validators=[myproject.myapp.models.validate_file_extension]),
        ),
    ]
