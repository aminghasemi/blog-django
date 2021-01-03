from django.contrib import admin
from .models import Article, Category
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','slug','publish','author', 'status','category_to_str')
    list_filter=('publish','status')
    search_fields=('title', 'description')
    prepopulated_fields={'slug':('title',)}
    ordering=['status','publish']

    def category_to_str(category, obj):
        return ", ".join([category.title for category in obj.category.active()])
    category_to_str.short_description='Categories'      
admin.site.register(Article, ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','slug','position','parent', 'status')
    list_filter=(['status'])
    search_fields=('title', 'slug')
    prepopulated_fields={'slug':('title',)}

  
admin.site.register(Category, CategoryAdmin)