# Generated by Django 3.2.7 on 2021-09-24 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='count_num',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
