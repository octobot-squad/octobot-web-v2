# Generated by Django 4.0.2 on 2022-02-02 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_blog_paragraph_3_blog_paragraph_4'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='slug',
            field=models.CharField(default='/', max_length=400),
            preserve_default=False,
        ),
    ]