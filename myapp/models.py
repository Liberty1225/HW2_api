from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title} - {self.department}'


class Employee(models.Model):
    name = models.CharField(max_length=50)
    birth_year = models.DateField()
    salary = models.IntegerField(default=0)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.salary}'
