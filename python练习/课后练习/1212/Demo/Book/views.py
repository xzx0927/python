from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Book.models import Book#Book（同views中方法名一致）下面方法
from bookmanager import bookserializer


def index(request):
    books = Book.objects.all().values('id', 'name')  # 返回表中（与数据库交互）所有数据并转换为字典型
    return render(request, 'index.html', {'books': books})#后台传输数据到前台这里是传输books(自定义参数)books上行赋值的数据


def detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'detail.html', {'book': book})

class Testview(ModelViewSet):
    queryset = Book.objects.all()#将python对象转换为json对象，序列化
    serializer_class =bookserializer#从bookmanager导包
