from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=30)
    create = models.DateTimeField('created')
    
    def __str__(self):
        return self.name


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField('date')
    actionType = models.CharField(max_length=10) 
    description = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=14, decimal_places=2)
    
    def __str__(self):
        return self.description