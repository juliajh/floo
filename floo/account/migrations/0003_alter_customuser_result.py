# Generated by Django 3.2.7 on 2021-09-24 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customuser_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='result',
            field=models.CharField(choices=[('fire', 'FIRE족'), ('yolo', 'YOLO족')], max_length=5),
        ),
    ]
