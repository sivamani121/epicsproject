# Generated by Django 4.0.7 on 2023-04-03 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='meaning',
            field=models.CharField(blank=True, max_length=1638),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='tags',
            field=models.CharField(max_length=1638),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='words',
            field=models.CharField(max_length=1638),
        ),
    ]
