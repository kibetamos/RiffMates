from django.db import models

# Create your models here.]

class Venue(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"Venue(id={self.id}, name={self.name})"

class Room(models.Model):
    name = models.CharField(max_length=20)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return f"Room(id={self.id}, name={self.name})"

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()

class Band(models.Model):
    name = models.CharField(max_length=20) 
    
    musicians = models.ManyToManyField(Musician)
    
    def __str__(self):
        return f"Band(id={self.id}, name={self.name})"


