from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
]


class Node(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    birthdate = models.DateField()
    spouse = models.OneToOneField(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="spouses",
    )
    parent = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
    )
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.spouse and self.spouse.spouse != self:
            self.spouse.spouse = self
            self.spouse.save()
