from django.contrib import admin
from .models import Company, Gig

# Register your models here.
@admin.register(Company)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Gig)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}