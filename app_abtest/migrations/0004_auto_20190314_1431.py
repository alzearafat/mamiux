# Generated by Django 2.1.7 on 2019-03-14 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_abtest', '0003_auto_20190314_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designcomment',
            name='design_abtest_tester_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tester_user_hook', to='app_user.Tester', verbose_name='Tester user'),
        ),
    ]
