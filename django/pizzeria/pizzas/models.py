from django.db import models

# Create your models here.
class Pizza(models.Model):
    """ pizza模型 """
    name = models.CharField(max_length=100)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name


class Topping(models.Model):
    """ 配料模型 """
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Toppings'

    def __str__(self):
        return self.name