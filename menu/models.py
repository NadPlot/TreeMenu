from django.db import models
from django.urls import reverse

from .translit import transliterate


class Menu(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=50, blank=True)
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE, related_name='children',
    )
    order = models.IntegerField(blank=True, verbose_name='Уровень вложенности')

    class Meta:
        verbose_name = 'Заголовок в Меню'
        verbose_name_plural = 'Заголовки'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('header', args=[self.url])

    def save(self, *args, **kwargs):
        url = '-'.join(transliterate(self.name.lower()).split())  # moe-menu-1
        self.url = f'{self.parent.url}-{url}'
        if not self.parent:
            self.order = 0
        else:
            self.order = self.parent.order + 1
        super().save(*args, **kwargs)
