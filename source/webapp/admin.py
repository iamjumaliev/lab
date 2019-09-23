from django.contrib import admin
from webapp.models import Product


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name','description']
    list_filter = ['category']
    list_display_links = ['pk',]
    search_fields = ['description']
    fields = ['name','description', 'category','amount','price']


admin.site.register(Product, ArticleAdmin)
