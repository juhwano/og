# Generated by Django 4.0.2 on 2022-02-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choice_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
