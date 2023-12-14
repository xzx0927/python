from django.contrib import admin

from Book.models import Book, BookLei


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'publish', 'price', 'cover')
    search_fields = ('name', 'author', 'publish', 'price', 'cover')

@admin.register(BookLei)
class BookLeiAdmin(admin.ModelAdmin):
    list_display = ('name', 'miaoshu')