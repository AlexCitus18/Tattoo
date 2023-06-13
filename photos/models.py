from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Photography(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.image)


class Consultation(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    number = models.CharField(max_length=12, verbose_name="Номер телефона")
    communication_method = models.CharField(max_length=30, verbose_name="Способ связи")
    file = models.ImageField(upload_to='consultation/', verbose_name='Эскиз')

    def __str__(self):
        return self.name + " " + self.number
