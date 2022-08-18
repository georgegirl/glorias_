# Generated by Django 4.1 on 2022-08-16 15:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_ass', '0002_rename_body_post_body_post_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Post_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='SEACHANGE', max_length=255),
        ),
    ]
