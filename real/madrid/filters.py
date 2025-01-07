from .models import Category,Product
from django_filters import FilterSet


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = {

            'category_name': ['exact'],


        }


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['gt', 'lt'],

        }
