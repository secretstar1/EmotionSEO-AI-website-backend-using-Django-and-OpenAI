# Generated by Django 4.2.9 on 2024-01-24 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='word_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='word',
            name='word_limit',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
