# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EssNutr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('food', models.CharField(max_length=100)),
                ('kcal', models.IntegerField()),
                ('proteins', models.DecimalField(decimal_places=1, max_digits=4)),
                ('fats', models.DecimalField(decimal_places=1, max_digits=4)),
                ('carbohydrates', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('category', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('gender', models.CharField(max_length=6, choices=[('male', 'male'), ('female', 'female')], blank=True)),
                ('choices', models.ForeignKey(to='essential_nutritions.EssNutr')),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='essnutr',
            name='f_category',
            field=models.ForeignKey(to='essential_nutritions.FoodCategory'),
            preserve_default=True,
        ),
    ]
