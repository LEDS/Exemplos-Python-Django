from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('author','title','created_date','isImage')

admin.site.register(Post,PostAdmin)
