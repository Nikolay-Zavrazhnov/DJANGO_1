from datetime import datetime

from django.db import models

from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля

    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(unique=True, null=True)
    release_date = models.DateField(default=datetime.now)
    lte_exists = models.BooleanField(null=True)
    slug = models.SlugField(unique=True, null=True, verbose_name='name')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)


