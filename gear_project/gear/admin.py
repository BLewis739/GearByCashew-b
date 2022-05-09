from django.contrib import admin
from .models import Wrestler, Style, GearOrder, GalleryItem, Testimonial

# Register your models here.

admin.site.register(Wrestler)
admin.site.register(Style)
admin.site.register(GearOrder)
admin.site.register(GalleryItem)
admin.site.register(Testimonial)
