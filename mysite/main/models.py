from django.db import models

# Create your models here.
class HomeName(models.Model):

    name = models.CharField('Home name', max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']


class HomeImage(models.Model):

    img = models.ImageField('Home image', upload_to='grtnak')


class Contact(models.Model):

    username = models.CharField('User name', max_length=100)
    email = models.EmailField('User email')
    review = models.TextField('User review')

    def __str__(self):
        return self.username
    

class About(models.Model):

    name = models.CharField('About name', max_length=60)
    text = models.TextField('About text')

    def __str__(self):
        return self.text


class Product(models.Model):

    name = models.CharField('Product name', max_length=255)
    img = models.ImageField('Product image', upload_to='products')
    price = models.PositiveIntegerField('Product price')
    compound = models.TextField('Product compound')
    history = models.TextField('Product History')

    def __str__(self):
        return self.name

class Cart(models.Model):

    prod_item = models.ForeignKey(Product, on_delete=models.CASCADE)