from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *



@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',  'map')
    search_fields = ('name',)




@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image', )
    save_as = True
    search_fields = ('name',)

    def get_image(self, obj):
        return mark_safe(f"<img scr = {obj.image.url } width ='50' height='60'")

    get_image.short_description = 'Картинка Писателя'



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    save_as = True
    search_fields = ('title', )




@admin.register(ReviewBook)
class ReviewBookAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'book')
