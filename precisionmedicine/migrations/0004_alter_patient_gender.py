# Generated by Django 3.2.13 on 2022-10-26 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('precisionmedicine', '0003_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='M', max_length=1),
        ),
    ]