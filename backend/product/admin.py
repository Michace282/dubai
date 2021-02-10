from django.contrib import admin
from .models import Product, ProductSizeColor, ProductImage, Color, SizeChart, Size, Feedback, FeedbackImage
from django_summernote.widgets import SummernoteWidget
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt
from django.urls import reverse
from django import forms
from django.template.loader import render_to_string
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
    show_change_link = True

    def render_inline_actions(self, obj=None):
        render = render_to_string('admin/render_inline_actions.html', {'obj': obj if obj else None})
        return mark_safe(render)

    render_inline_actions.short_description = 'Images'
    render_inline_actions.allow_tags = True

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        fields = list(fields)
        if obj:
            fields.append('render_inline_actions')
        return fields


class ProductImageInline(admin.StackedInline):
    model = ProductImage


@admin.register(ProductSizeColor)
class ProductSizeColorAdmin(admin.ModelAdmin):
    inlines = (ProductImageInline,)

    def get_model_perms(self, *args, **kwargs):
        perms = admin.ModelAdmin.get_model_perms(self, *args, **kwargs)
        perms['list_hide'] = True
        return perms


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'product_type', 'profile_type', 'price',)
    list_filter = ('status', 'product_type', 'ladies_type', 'mens_type', 'accessories_type', 'dance_shoes_type')
    inlines = (ProductSizeColorInline,)
    autocomplete_fields = ('works_best_with',)
    search_fields = ('name', 'data', 'description', 'model_description')

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
                'size_chart',
                'works_best_with'
            )
        }),
    )

    class Media:
        js = ("js/product.js",)


class FeedbackImageInline(admin.StackedInline):
    model = FeedbackImage


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    inlines = (FeedbackImageInline,)
