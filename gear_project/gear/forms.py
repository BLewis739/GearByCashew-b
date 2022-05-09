# tunr/forms.py
from django import forms
from .models import Wrestler, Testimonial, Style, GearOrder, GalleryItem


class WrestlerForm(forms.ModelForm):

    class Meta:
        model = Wrestler
        fields = ('name',)


class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        fields = ('wrestler', 'testimonialText',)


class StyleForm(forms.ModelForm):

    class Meta:
        model = Style
        fields = ('name', 'standardMaterialUsed',)


class GearOrderForm(forms.ModelForm):

    class Meta:
        model = GearOrder
        fields = ('shortName', 'wrestler', 'style',
                  'description', 'hasPaid', 'price', 'isComplete')


class GalleryItemForm(forms.ModelForm):

    class Meta:
        model = GalleryItem
        fields = ('shortName', 'wrestler', 'style', 'photoUrl',)
