from django.db import models


from django.core.validators import MinValueValidator
# Create your models here.]

class Venue(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    venue = models.ForeignKey(Venue, related_name='rooms', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"{self.name} at {self.venue.name}"

        
# alternate short-cut version as there is only one "uniqueness"
# unique_together = ["name", "venue"]
    def __str__(self):
        return f"Room(id={self.id}, name={self.name})"

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()

    class Meta:
        ordering = ["last_name", "first_name"]

class Band(models.Model):
    name = models.CharField(max_length=20) 
    
    musicians = models.ManyToManyField(Musician)
    
    # def __str__(self):
    #     return f"Band(id={self.id}, name={self.name})"
    def __str__(self):
        return self.name


