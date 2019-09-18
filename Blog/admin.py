from django.contrib import admin
from Blog.models import Category,Tag,Blog


# @admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

# @admin.site.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name')

# @admin.site.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','excerpt','created_time','modified_time','views','category')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Blog,BlogAdmin)
'''
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)
'''