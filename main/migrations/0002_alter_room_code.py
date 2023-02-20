# Generated by Django 4.1.6 on 2023-02-12 17:43

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=main.models.generate_unique_code, max_length=8, unique=True),
        ),
    ]