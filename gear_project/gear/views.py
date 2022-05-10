# from django.shortcuts import render, redirect
from .models import Wrestler, Style, GearOrder, GalleryItem, Testimonial
# from .forms import TestimonialForm, WrestlerForm, StyleForm, GearOrderForm, GalleryItemForm
from .serializers import WrestlerSerializer, TestimonialSerializer, StyleSerializer, GearOrderSerializer, GalleryItemSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class WrestlerList(generics.ListCreateAPIView):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer


class WrestlerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wrestler.objects.all()
    serializer_class = WrestlerSerializer


class TestimonialList(generics.ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class TestimonialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class StyleList(generics.ListCreateAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


class StyleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


class GearOrderList(generics.ListCreateAPIView):
    queryset = GearOrder.objects.all()
    serializer_class = GearOrderSerializer
    permission_classes = [IsAuthenticated]


class GearOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GearOrder.objects.all()
    serializer_class = GearOrderSerializer
    permission_classes = [IsAuthenticated]


class GalleryItemList(generics.ListCreateAPIView):
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryItemSerializer


class GalleryItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryItemSerializer

# def wrestler_list(request):
#     wrestlers = Wrestler.objects.all()
#     return render(request, 'gear/wrestler_list.html', {'wrestlers': wrestlers})


# def testimonial_list(request):
#     testimonials = Testimonial.objects.all()
#     return render(request, 'gear/testimonial_list.html', {'testimonials': testimonials})


# def style_list(request):
#     styles = Style.objects.all()
#     return render(request, 'gear/style_list.html', {'styles': styles})


# def gearOrder_list(request):
#     gearOrders = GearOrder.objects.all()
#     return render(request, 'gear/gearOrder_list.html', {'gearOrders': gearOrders})


# def galleryItem_list(request):
#     galleryItems = GalleryItem.objects.all()
#     return render(request, 'gear/galleryItem_list.html', {'galleryItems': galleryItems})


# def wrestler_detail(request, pk):
#     wrestler = Wrestler.objects.get(id=pk)
#     return render(request, 'gear/wrestler_detail.html', {'wrestler': wrestler})


# def testimonial_detail(request, pk):
#     testimonial = Testimonial.objects.get(id=pk)
#     return render(request, 'gear/testimonial_detail.html', {'testimonial': testimonial})


# def style_detail(request, pk):
#     style = Style.objects.get(id=pk)
#     return render(request, 'gear/style_detail.html', {'style': style})


# def gearOrder_detail(request, pk):
#     gearOrder = GearOrder.objects.get(id=pk)
#     return render(request, 'gear/gearOrder_detail.html', {'gearOrder': gearOrder})


# def galleryItem_detail(request, pk):
#     galleryItem = GalleryItem.objects.get(id=pk)
#     return render(request, 'gear/galleryItem_detail.html', {'galleryItem': galleryItem})


# def wrestler_create(request):
#     if request.method == 'POST':
#         form = WrestlerForm(request.POST)
#         if form.is_valid():
#             wrestler = form.save()
#             return redirect('wrestler_detail', pk=wrestler.pk)
#     else:
#         form = WrestlerForm()
#     return render(request, 'gear/wrestler_form.html', {'form': form})


# def testimonial_create(request):
#     if request.method == 'POST':
#         form = TestimonialForm(request.POST)
#         if form.is_valid():
#             testimonial = form.save()
#             return redirect('testimonial_detail', pk=testimonial.pk)
#     else:
#         form = TestimonialForm()
#     return render(request, 'gear/testimonial_form.html', {'form': form})


# def style_create(request):
#     if request.method == 'POST':
#         form = StyleForm(request.POST)
#         if form.is_valid():
#             style = form.save()
#             return redirect('style_detail', pk=style.pk)
#     else:
#         form = StyleForm()
#     return render(request, 'gear/style_form.html', {'form': form})


# def gearOrder_create(request):
#     if request.method == 'POST':
#         form = GearOrderForm(request.POST)
#         if form.is_valid():
#             gearOrder = form.save()
#             return redirect('gearOrder_detail', pk=gearOrder.pk)
#     else:
#         form = GearOrderForm()
#     return render(request, 'gear/gearOrder_form.html', {'form': form})


# def galleryItem_create(request):
#     if request.method == 'POST':
#         form = GalleryItemForm(request.POST)
#         if form.is_valid():
#             galleryItem = form.save()
#             return redirect('galleryItem_detail', pk=galleryItem.pk)
#     else:
#         form = GalleryItemForm()
#     return render(request, 'gear/galleryItem_form.html', {'form': form})


# def wrestler_edit(request, pk):
#     wrestler = Wrestler.objects.get(pk=pk)
#     if request.method == "POST":
#         form = WrestlerForm(request.POST, instance=wrestler)
#         if form.is_valid():
#             wrestler = form.save()
#             return redirect('wrestler_detail', pk=wrestler.pk)
#     else:
#         form = WrestlerForm(instance=wrestler)
#     return render(request, 'gear/wrestler_form.html', {'form': form})


# def testimonial_edit(request, pk):
#     testimonial = Testimonial.objects.get(pk=pk)
#     if request.method == "POST":
#         form = TestimonialForm(request.POST, instance=testimonial)
#         if form.is_valid():
#             testimonial = form.save()
#             return redirect('testimonial_detail', pk=testimonial.pk)
#     else:
#         form = TestimonialForm(instance=testimonial)
#     return render(request, 'gear/testimonial_form.html', {'form': form})


# def style_edit(request, pk):
#     style = Style.objects.get(pk=pk)
#     if request.method == "POST":
#         form = StyleForm(request.POST, instance=style)
#         if form.is_valid():
#             style = form.save()
#             return redirect('style_detail', pk=style.pk)
#     else:
#         form = StyleForm(instance=style)
#     return render(request, 'gear/style_form.html', {'form': form})


# def gearOrder_edit(request, pk):
#     gearOrder = GearOrder.objects.get(pk=pk)
#     if request.method == "POST":
#         form = GearOrderForm(request.POST, instance=gearOrder)
#         if form.is_valid():
#             gearOrder = form.save()
#             return redirect('gearOrder_detail', pk=gearOrder.pk)
#     else:
#         form = GearOrderForm(instance=gearOrder)
#     return render(request, 'gear/gearOrder_form.html', {'form': form})


# def galleryItem_edit(request, pk):
#     galleryItem = GalleryItem.objects.get(pk=pk)
#     if request.method == "POST":
#         form = GalleryItemForm(request.POST, instance=galleryItem)
#         if form.is_valid():
#             galleryItem = form.save()
#             return redirect('galleryItem_detail', pk=galleryItem.pk)
#     else:
#         form = GalleryItemForm(instance=galleryItem)
#     return render(request, 'gear/galleryItem_form.html', {'form': form})


# def wrestler_delete(request, pk):
#     Wrestler.objects.get(id=pk).delete()
#     return redirect('wrestler_list')


# def testimonial_delete(request, pk):
#     Testimonial.objects.get(id=pk).delete()
#     return redirect('testimonial_list')


# def style_delete(request, pk):
#     Style.objects.get(id=pk).delete()
#     return redirect('style_list')


# def gearOrder_delete(request, pk):
#     GearOrder.objects.get(id=pk).delete()
#     return redirect('gearOrder_list')


# def galleryItem_delete(request, pk):
#     GalleryItem.objects.get(id=pk).delete()
#     return redirect('galleryItem_list')
