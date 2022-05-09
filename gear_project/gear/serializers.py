from rest_framework import serializers
from .models import Wrestler, Style, GearOrder, GalleryItem, Testimonial


class WrestlerSerializer(serializers.HyperlinkedModelSerializer):
    galleryItems = serializers.HyperlinkedRelatedField(
        view_name='gallery_item_detail',
        many=True,
        read_only=True
    )

    testimonials = serializers.HyperlinkedRelatedField(
        view_name='testimonial_detail',
        many=True,
        read_only=True
    )

    gearOrders = serializers.HyperlinkedRelatedField(
        view_name='gear_order_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Wrestler
        fields = ('id', 'name', 'galleryItems', 'testimonials', 'gearOrders')
