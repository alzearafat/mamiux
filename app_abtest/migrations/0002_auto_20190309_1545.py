# Generated by Django 2.1.7 on 2019-03-09 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_abtest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='design_comment',
            field=models.TextField(blank=True, null=True, verbose_name='Comment'),
        ),
    ]