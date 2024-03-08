# Generated by Django 4.2.7 on 2024-03-08 17:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0002_goodhabit_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='EasyHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=200)),
                ('is_public', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='goodhabit',
            name='fee_some',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='награда предметом'),
        ),
        migrations.AddField(
            model_name='goodhabit',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='goodhabit',
            name='period',
            field=models.CharField(choices=[('week', 'Раз в неделю'), ('every_day', 'Каждый день')], default='every_day', max_length=20, verbose_name='периодичность'),
        ),
        migrations.AddField(
            model_name='goodhabit',
            name='time_action',
            field=models.PositiveIntegerField(default=120, validators=[django.core.validators.MaxValueValidator(120)]),
        ),
        migrations.AlterField(
            model_name='goodhabit',
            name='place',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='goodhabit',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='goodhabit',
            name='fee_habit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='habit.easyhabit', verbose_name='награда привычкой'),
        ),
    ]