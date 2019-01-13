from django.db import models

class ToDoList(models.Model):
    item = models.CharField(max_length=200, blank=False, null=False)
    completed = models.BooleanField(default=False)
    user = models.CharField(max_length=20)
    
    def __str__(self):
        return self.item + ' | ' + str(self.completed)+ ' | ' + str(self.user)

class Address(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	phone = models.CharField(max_length=15)
	address = models.CharField(max_length=200)
	zipcode = models.CharField(max_length=8)
	city = models.CharField(max_length=50)
