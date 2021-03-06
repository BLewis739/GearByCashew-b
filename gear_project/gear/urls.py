from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [

    path('wrestlers/', views.WrestlerList.as_view(), name='wrestler_list'),
    path('wrestlers/<int:pk>', views.WrestlerDetail.as_view(),
         name='wrestler_detail'),

    path('testimonials/', views.TestimonialList.as_view(), name='testimonial_list'),
    path('testimonials/<int:pk>', views.TestimonialDetail.as_view(),
         name='testimonial_detail'),

    path('styles/', views.StyleList.as_view(), name='style_list'),
    path('styles/<int:pk>', views.StyleDetail.as_view(),
         name='style_detail'),

    path('gearorders/', views.GearOrderList.as_view(), name='gearOrder_list'),
    path('gearorders/<int:pk>', views.GearOrderDetail.as_view(),
         name='gearOrder_detail'),

    path('galleryitems/', views.GalleryItemList.as_view(), name='galleryItem_list'),
    path('galleryitems/<int:pk>', views.GalleryItemDetail.as_view(),
         name='galleryItem_detail'),

    path('galleryphotoitems/', views.GalleryPhotoItemList.as_view(),
         name='galleryPhotoItem_list'),
    path('galleryphotoitems/<int:pk>', views.GalleryPhotoItemDetail.as_view(),
         name='galleryPhotoItem_detail'),


    # # lists
    # path('wrestlers/', views.wrestler_list, name='wrestler_list'),
    # path('testimonials/', views.testimonial_list, name='testimonial_list'),
    # path('styles/', views.style_list, name='style_list'),
    # path('gearorders/', views.gearOrder_list, name='gearOrder_list'),
    # path('galleryitems/', views.galleryItem_list, name='galleryItem_list'),

    # # individual detail
    # path('wrestlers/<int:pk>', views.wrestler_detail, name='wrestler_detail'),
    # path('testimonials/<int:pk>', views.testimonial_detail,
    #      name='testimonial_detail'),
    # path('styles/<int:pk>', views.style_detail, name='style_detail'),
    # path('gearorders/<int:pk>', views.gearOrder_detail, name='gearOrder_detail'),
    # path('galleryitems/<int:pk>', views.galleryItem_detail,
    #      name='galleryItem_detail'),

    # # create new
    # path('wrestlers/new', views.wrestler_create, name='wrestler_create'),
    # path('testimonials/new', views.testimonial_create, name='testimonial_create'),
    # path('styles/new', views.style_create, name='style_create'),
    # path('gearorders/new', views.gearOrder_create, name='gearOrder_create'),
    # path('galleryitems/new', views.galleryItem_create, name='galleryItem_create'),

    # # edit
    # path('wrestlers/<int:pk>/edit', views.wrestler_edit, name='wrestler_edit'),
    # path('testimonials/<int:pk>/edit',
    #      views.testimonial_edit, name='testimonial_edit'),
    # path('styles/<int:pk>/edit', views.style_edit, name='style_edit'),
    # path('gearorders/<int:pk>/edit', views.gearOrder_edit, name='gearOrder_edit'),
    # path('galleryitems/<int:pk>/edit',
    #      views.galleryItem_edit, name='galleryItem_edit'),

    # # delete
    # path('wrestlers/<int:pk>/delete',
    #      views.wrestler_delete, name='wrestler_delete'),
    # path('testimonials/<int:pk>/delete',
    #      views.testimonial_delete, name='testimonial_delete'),
    # path('styles/<int:pk>/delete', views.style_delete, name='style_delete'),
    # path('gearorders/<int:pk>/delete',
    #      views.gearOrder_delete, name='gearOrder_delete'),
    # path('galleryitems/<int:pk>/delete',
    #      views.galleryItem_delete, name='galleryItem_delete'),
]
