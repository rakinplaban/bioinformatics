# Generated by Django 3.2.13 on 2022-10-25 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('precisionmedicine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=25),
        ),
    ]
