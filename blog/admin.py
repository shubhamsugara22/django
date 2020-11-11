from django.contrib import admin
from . models import Post, Category
# Register your models here.

# adding post and category to admin page


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "created_on", "last_modified")
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
