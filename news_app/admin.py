from django.contrib import admin
from .models import Category, News, Contact

admin.site.register(Category)
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_time', 'category', 'status')
    list_filter = ('status', 'publish_time')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status']


admin.site.register(Contact)