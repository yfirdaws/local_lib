from django.db import models

# Create your models here.
class book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30, default='anonymous')
    email = models.EmailField(blank = True)
    describe = models.TextField(default = 'DataFlair Django tutorials')
    def __str__(self):
        return self.name