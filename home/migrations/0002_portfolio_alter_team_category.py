# Generated by Django 4.0.2 on 2022-02-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Sarlavha')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Rasmi')),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolio',
            },
        ),
        migrations.AlterField(
            model_name='team',
            name='category',
            field=models.CharField(max_length=300, verbose_name='Kasbi'),
        ),
    ]
