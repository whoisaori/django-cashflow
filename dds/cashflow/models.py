from django.db import models
from django.utils import timezone
from django.urls import reverse


class Status(models.Model):
    name = models.CharField(max_length=100,
                            unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('status_edit', kwargs={'pk': self.pk})


class Type(models.Model):
    name = models.CharField(max_length=100,
                            unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('type_edit', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100,
                            unique=True)
    type = models.ForeignKey(Type,
                             on_delete=models.CASCADE,
                             related_name="cats",
                             blank=False,
                             null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cats_edit', kwargs={'pk': self.pk})


class SubCategory(models.Model):
    name = models.CharField(max_length=100,
                            unique=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name="subcats",
                                 blank=False,
                                 null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subcats_edit', kwargs={'pk': self.pk})


class Transaction(models.Model):
    date_created = models.DateField(default=timezone.now())
    status = models.ForeignKey(Status,
                               on_delete=models.SET_NULL,
                               null=True)
    type = models.ForeignKey(Type,
                             on_delete=models.SET_NULL,
                             null=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True)
    subcategory = models.ForeignKey(SubCategory,
                                    on_delete=models.SET_NULL,
                                    null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True)


    def __str__(self):
        return f"{self.date_created} | {self.type} | {self.amount}₽"

    def get_absolute_url(self):
        return reverse('transaction_edit', kwargs={'pk': self.pk})
