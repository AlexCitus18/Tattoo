from django.shortcuts import render, redirect

from prices.models import Category_service
from .models import Photography, Category, Consultation
from .serializers import PhotographySerializer, CategorySerializer
from rest_framework import generics
from rest_framework.views import APIView
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.views import View

from artists.models import Artist


class IndexRenderView(View):

    def get(self, requset, *args, **kwargs):
        return render(requset, 'index.html', context={
            "artists": Artist.objects.all(),
            "categories_service": Category_service.objects.all(),
            "categories": Category.objects.all(),
            "photos": Photography.objects.all(),
        })


class ConsultationCreateView(View):

    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if value == 'on':
                Consultation.objects.create(
                    name=request.POST['name'],
                    number=request.POST['phone'],
                    communication_method=request.POST[key + str(1)],
                    file=request.FILES['file'],
                )
        return redirect('index')


class PhotographyByCategoryListView(APIView):

    def get(self, requset, *args, **kwargs):
        photos = Photography.objects.all()
        return JsonResponse(
            {
                "photos": PhotographySerializer(
                    photos if requset.GET['active'] == "ALL" else Photography.objects.filter(
                        category__name__icontains=requset.GET['active']), many=True).data
            }, status=200
        )


class PhotographyList(generics.ListAPIView):
    queryset = Photography.objects.all()
    serializer_class = PhotographySerializer
    filter_backends = [filters.OrderingFilter,
                       DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']


class PhotographyDetail(generics.RetrieveAPIView):
    queryset = Photography.objects.all()
    serializer_class = PhotographySerializer


class PhotographyUpdate(generics.RetrieveUpdateAPIView):
    queryset = Photography.objects.all()
    serializer_class = PhotographySerializer


class PhotographyCreate(generics.CreateAPIView):
    queryset = Photography.objects.all()
    serializer_class = PhotographySerializer


class PhotographyDelete(generics.DestroyAPIView):
    queryset = Photography.objects.all()
    serializer_class = PhotographySerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdate(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDelete(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
