# Generated by Django 2.0.6 on 2019-02-11 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0004_article_blog_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='blog_type',
            field=models.IntegerField(choices=[(0, 'python'), (1, 'java'), (2, '区块链'), (3, '随笔')], default='随笔', verbose_name='文章类型'),
        ),
    ]