# Generated by Django 2.0.6 on 2019-02-13 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0010_auto_20190212_0248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_time']},
        ),
    ]