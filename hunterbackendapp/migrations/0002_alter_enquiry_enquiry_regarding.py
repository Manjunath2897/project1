# Generated by Django 5.0.3 on 2024-10-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunterbackendapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='enquiry_regarding',
            field=models.CharField(choices=[('Knowledge', 'Knowledge'), ('Jobs', 'Jobs'), ('HRMS', 'HRMS')], max_length=50),
        ),
    ]
