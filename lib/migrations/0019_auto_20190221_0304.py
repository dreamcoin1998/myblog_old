# Generated by Django 2.1.7 on 2019-02-20 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0018_auto_20190221_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpomment',
            name='article',
        ),
        migrations.DeleteModel(
            name='Cpomment',
        ),
    ]
