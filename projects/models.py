from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=150)
    image_name = models.ImageField(null=True, blank=True)
    demo = models.CharField(max_length=500)
    source_code = models.CharField(max_length=500)

    def __str__(self):
        return self.title
