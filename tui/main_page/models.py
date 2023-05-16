from django.db import models
from django.urls import reverse


class Tui(models.Model):
    objects = None
    thuja = 'туя'
    pine = 'сосна'
    juniper = 'можж'
    bush = 'куст'
    fruit = 'плод'
    flower = 'цвет'
    trunk = 'штамб'
    spruce = 'ель'
    mix = 'смесь'
    wood = 'Деревья'
    choice_of_thuja = [
        (thuja, 'туи'),
        (pine,'сосны'),
        (juniper, 'можжевельники'),
        (bush, 'кустарники'),
        (fruit, 'плодоввые'),
        (flower, 'цветы'),
        (trunk, 'штамбовые'),
        (spruce, 'ели'),
        (mix,  'смесь'),
        (wood, 'Деревья')
    ]
    title = models.CharField(max_length=100, verbose_name='сорт')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='описание')
    price = models.DecimalField(decimal_places=2, max_digits=15, verbose_name='цена', default=10)
    availability = models.BooleanField(default=True, verbose_name='доступность')
    choice = models.CharField(max_length=20, choices=choice_of_thuja, default=thuja, verbose_name='выбор раздела')
    image = models.ImageField(upload_to='photos', verbose_name='фото')
    amount = models.IntegerField(default=1, verbose_name='кол-во')
    thuja_cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категории')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Список туй'
        verbose_name_plural = 'Список туй'
        ordering = ['content', 'thuja_cat']


class Category(models.Model):
    choice_thuja = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.choice_thuja

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
