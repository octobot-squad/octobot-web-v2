from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField('Ism Familya', max_length=200)
    category = models.CharField('Kasbi', max_length=300)
    image = models.ImageField('Rasmi', upload_to='images/')
    phone = models.CharField('Telefon raqami', max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    telegram = models.CharField(blank=True, max_length=100)

    class Meta:
        verbose_name = "Jamoa"
        verbose_name_plural = "Jamoa"

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


class Portfolio(models.Model):
    title = models.CharField('Sarlavha', max_length=200)
    slug = models.CharField(max_length=400)
    image = models.ImageField('Rasmi', upload_to='images/')

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio"

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


class Blog(models.Model):
    title = models.TextField('Sarlavhasi', max_length=351)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField('Tavsifi', max_length=2000)
    orta_description = models.TextField('Orta Tekst', blank=True, max_length=3001)
    past_description = models.TextField('Pastki Tavsif:', blank=True, max_length=1000)
    paragraph_3 = models.TextField('Paragraf 3', blank=True, max_length=500)
    paragraph_4 = models.TextField('Paragraf 4', blank=True, max_length=500)
    image = models.ImageField('Rasmi', upload_to='images/')
    create_on_date = models.DateField(auto_now=True)
    create_on_time = models.TimeField(auto_now=True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog"

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


class Total(models.Model):
    n1 = models.CharField(max_length=10)
    n2 = models.CharField(max_length=10)
    n3 = models.CharField(max_length=10)
    n4 = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Hisob"
        verbose_name_plural = "Hisob"

    def __str__(self):
        return self.n1


class Aloqa(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
    create_date = models.DateField(auto_now=True)
    create_time = models.TimeField(auto_now=True)
    ip = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Aloqa Formasi'
        verbose_name_plural = 'Aloqa Formasi'
