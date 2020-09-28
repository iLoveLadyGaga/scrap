from django.db import models
from .utils import cyrillic_to_latin


class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='City name',
                            unique=True)
    slug = models.CharField(max_length=50,
                            blank=True,
                            unique=True)

    class Meta:
        verbose_name = 'City name'
        verbose_name_plural = 'City names'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = cyrillic_to_latin(str(self.name))
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Programming language',
                            unique=True)
    slug = models.CharField(max_length=50,
                            blank=True,
                            unique=True)

    class Meta:
        verbose_name = 'Programming language'
        verbose_name_plural = 'Programming languages'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = cyrillic_to_latin(str(self.name))
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250,
                             verbose_name='Vacancy title')
    company = models.CharField(max_length=250,
                               verbose_name='Company name')
    description = models.TextField(verbose_name='Description')
    city = models.ForeignKey('City', on_delete=models.CASCADE,
                             verbose_name='')
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 verbose_name='Programming language')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.title