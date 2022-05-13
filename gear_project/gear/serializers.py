from rest_framework import serializers
from .models import Wrestler, Style, GearOrder, GalleryItem, Testimonial, GalleryPhotoItem


class TestimonialSerializer(serializers.HyperlinkedModelSerializer):
    wrestler = serializers.HyperlinkedRelatedField(
        view_name='wrestler_detail',
        read_only=True
    )

    class Meta:
        model = Testimonial
        fields = ('id', 'wrestler', 'testimonialText',)


class StyleSerializer(serializers.HyperlinkedModelSerializer):

    gallery_items = serializers.HyperlinkedRelatedField(
        view_name='galleryItem_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Style
        fields = ('id', 'name', 'standardMaterialUsed', 'gallery_items')


class GearOrderSerializer(serializers.HyperlinkedModelSerializer):
    # wrestler = serializers.StringRelatedField(
    #     read_only=False
    # )

    # style = serializers.StringRelatedField(
    #     read_only=False
    # )

    class Meta:
        model = GearOrder
        fields = ('id', 'shortName', 'wrestler', 'style',
                  'price', 'hasPaid', 'isComplete', 'description')


class GalleryItemSerializer(serializers.HyperlinkedModelSerializer):
    wrestler = serializers.StringRelatedField(
        read_only=True
    )

    style = serializers.HyperlinkedRelatedField(
        view_name='style_detail',
        read_only=True
    )

    gallery_photo_items = serializers.StringRelatedField(
        read_only=True,
        many=True
    )

    class Meta:
        model = GalleryItem
        fields = ('id', 'wrestler', 'style',
                  'gallery_photo_items', 'shortName')


class GalleryPhotoItemSerializer(serializers.HyperlinkedModelSerializer):
    galleryItems = serializers.HyperlinkedRelatedField(
        view_name='galleryItem_detail',
        read_only=True
    )

    class Meta:
        model = GalleryPhotoItem
        fields = ('id', 'galleryItems', 'photoName', 'photoUrl')


class WrestlerSerializer(serializers.HyperlinkedModelSerializer):
    gallery_items = serializers.HyperlinkedRelatedField(
        view_name='galleryItem_detail',
        many=True,
        read_only=True
    )

    testimonials = serializers.HyperlinkedRelatedField(
        view_name='testimonial_detail',
        many=True,
        read_only=True
    )

    # gear_orders = serializers.HyperlinkedRelatedField(
    #     view_name='gearOrder_detail',
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = Wrestler
        fields = ('id', 'name', 'gallery_items', 'testimonials')
