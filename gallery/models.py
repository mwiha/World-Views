from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image = models.ImageField(upload_to = 'images/',default='')
    image_location = models.ForeignKey('Location',default='')
    image_category = models.ForeignKey('Category',default='')


class Category(models.Model):
    category_name = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.category_name