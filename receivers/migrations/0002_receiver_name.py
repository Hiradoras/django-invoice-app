# Generated by Django 4.0.2 on 2022-02-15 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receivers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiver',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
