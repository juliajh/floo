# Generated by Django 3.2.7 on 2021-09-25 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_customuser_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='result',
            field=models.CharField(choices=[('fire', 'FIRE족'), ('null', '미선택'), ('yolo', 'YOLO족')], default='null', max_length=5),
        ),
    ]