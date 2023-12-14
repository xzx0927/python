from django.contrib import admin

from Book.models import Book, BookLei


# Register your models here.
@admin.register(Book)  # 创建实体类
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'publish', 'price', 'cover')  # 列出要展示的字段（cover为数据库参数）
    search_fields = ('name', 'author', 'publish', 'price', 'cover')#搜索


@admin.register(BookLei)
class BookLeiAdmin(admin.ModelAdmin):
    list_display = ('name', 'miaoshu')
