# Generated by Django 4.0.5 on 2022-06-08 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_otherlocation_contactperson_slug_workstation_slug_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OtherLocation',
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='l_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='workstations',
            field=models.ManyToManyField(blank=True, to='core.workstation'),
        ),
        migrations.AlterField(
            model_name='workstation',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='workstationrole',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
