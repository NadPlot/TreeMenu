from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    url_name = models.CharField(max_length=50, default=f'{name}')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Заголовки'

    def __str__(self):
        return self.name
