from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('author','title','created_date')
    list_filter = ['author','created_date']
    search_fields = ['title']

admin.site.register(Post,PostAdmin)
