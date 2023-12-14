from django.shortcuts import render

from Book.models import Book#Book（同views中方法名一致）下面方法


def index(request):
    books = Book.objects.all().values('id', 'name')  # 返回表中（与数据库交互）所有数据并转换为字典型
    return render(request, 'index.html', {'books': books})#后台传输数据到前台这里是传输books(自定义参数)books上行赋值的数据


def detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'detail.html', {'book': book})






def TestView(ModelViewset):
    quserset=Book.objects.all()
