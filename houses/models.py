from django.db import models

# Create your models here.
class House(models.Model):

    # Model for House

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveBigIntegerField(
        verbose_name="Price", help_text="Only +"
    )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True,
        help_text="Does this place allow pets?",
        verbose_name="Pets allowed?",
    )

    def __str__(self):
        return self.name
