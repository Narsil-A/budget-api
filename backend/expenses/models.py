from django.db import models

"""
Models to represent the economic issues of a home, such as expenses, income, budget
"""
class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

class Income(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

class Budget(models.Model):
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)