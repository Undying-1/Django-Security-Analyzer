from django.db import models


# Create your models here.
class Archive(models.Model):
    name = models.CharField(max_length=255, unique=True)
    file = models.FileField(upload_to='archives/')

    class Meta:
        verbose_name = '- Проект'
        verbose_name_plural = '- Проекты'

    def __str__(self):
        return self.name


class Problems(models.Model):
    project = models.ForeignKey("Archive", on_delete=models.CASCADE, verbose_name='Проект', null=True, blank=True)
    location = models.TextField(verbose_name='Путь')
    error = models.TextField(verbose_name='Ошибка')
    level = models.CharField(max_length=255, verbose_name='Уровень ошибки')

    class Meta:
        verbose_name = '- Ошибка'
        verbose_name_plural = '- Ошибки'

    def __str__(self):
        return self.project.name