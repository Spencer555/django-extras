from django.db import models
from django.utils.text import slugify


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    price = models.PositiveIntegerField(default=1)
    cost = models.PositiveIntegerField(default=1)
    slug = models.SlugField(max_length=150, unique=True, blank=True, editable=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}")
        super(Book, self).save(*args, **kwargs)


    @property
    def profit_margin(self):
        return self.price - self.cost


    @property
    def loss(self):
        loss = self.cost - self.price 
        if loss < 0:
            return loss
        return False


