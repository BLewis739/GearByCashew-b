from django.db import models

# Create your models here.


class Wrestler(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=100)
    standardMaterialUsed = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GalleryItem(models.Model):
    shortName = models.CharField(max_length=100)
    wrestler = models.ForeignKey(
        Wrestler, on_delete=models.CASCADE, related_name='gallery_items')
    style = models.ForeignKey(
        Style, on_delete=models.CASCADE, related_name='gallery_items')
    photoUrl = models.CharField(max_length=300)

    def __str__(self):
        return self.shortName


class GearOrder(models.Model):
    shortName = models.CharField(max_length=100)
    wrestler = models.ForeignKey(
        Wrestler, on_delete=models.CASCADE, related_name='gear_orders')
    style = models.ForeignKey(
        Style, on_delete=models.CASCADE, related_name='gear_orders')
    description = models.TextField(max_length=1000)
    isComplete = models.BooleanField(default=False)
    hasPaid = models.BooleanField(default=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.shortName


class Testimonial(models.Model):
    wrestler = models.ForeignKey(
        Wrestler, on_delete=models.CASCADE, related_name='testimonials')
    testimonialText = models.TextField(max_length=1000)

    def __str__(self):
        return self.testimonialText
