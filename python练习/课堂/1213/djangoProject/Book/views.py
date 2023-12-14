from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from Book.models import Book
from serializers import Bookserializer


def index(request):
    books = Book.objects.all().values('id', 'name')  # ORM
    return render(request, 'index.html', {'books': books})


def detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'detail.html', {'book': book})


class Test2View(APIView):
    def get(self, request):
        key = request.GET.get('name', '')
        books = Book.objects.filter(name__contains=key)
        # 增加书
        category = Book()
        category.name = '新书'
        category.author = '张三'
        category.price = '25'
        # 修改书
        for book in books:
            book.price = 50
            book.save()
        # 删除书
        for book in Book.objects.all():
            if book.price == '1212':
                book.delete()

        ss = Bookserializer(books, many=True)
        return Response(ss.data)


class TestView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Bookserializer
