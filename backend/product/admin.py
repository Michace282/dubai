from django.contrib import admin
from .models import Product, ProductSizeColor, ProductImage, Color, SizeChart, Size
from django_summernote.widgets import SummernoteWidget
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt
from django.urls import reverse
from django import forms
import json


class SizeChartModelForm(forms.ModelForm):
    class Meta:
        model = SizeChart
        fields = '__all__'
        widgets = {
            'table': SummernoteWidget(attrs={'summernote': {'toolbar': ['table']}}),
        }


class SizeInline(admin.StackedInline):
    model = Size


@admin.register(SizeChart)
class SizeChartAdmin(admin.ModelAdmin):
    inlines = (SizeInline,)
    form = SizeChartModelForm


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


class ProductSizeColorInline(admin.TabularInline):
    model = ProductSizeColor


class ProductImageInline(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'product_type', 'profile_type', 'price',)
    list_filter = ('status', 'product_type', 'ladies_type', 'mens_type', 'accessories_type', 'dance_shoes_type')
    inlines = (ProductSizeColorInline, ProductImageInline,)

    def profile_type(self, obj):
        if obj.product_type == 'ladies':
            return obj.get_ladies_type_display()
        if obj.product_type == 'mens':
            return obj.get_mens_type_display()
        if obj.product_type == 'accessories':
            return obj.get_accessories_type_display()
        if obj.product_type == 'dance_shoes':
            return obj.get_dance_shoes_type_display()
        return '-'

    fieldsets = (
        (None, {
            'fields': (
                'status',
                'article',
                ('name', 'product_type', 'ladies_type', 'mens_type', 'accessories_type', 'dance_shoes_type',),
                'price',
                'description',
                'size_chart'
            )
        }),
    )
