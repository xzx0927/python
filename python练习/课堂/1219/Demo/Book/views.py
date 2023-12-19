from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from Book.models import Book, BookLei  # Book（同views中方法名一致）下面方法
from bookmanager import bookserializer


def index(request):
    type = BookLei.objects.all().values('name','id')# 返回表中（与数据库交互）所有数据并转换为字典型
    he ={}
    for x in type:
        books = Book.objects.filter(type_id=x.get('id'))#
        he.setdefault(x.get('name'),books)#
    return render(request, 'index.html', {'he': he})  # 后台传输数据到前台这里是传输books(自定义参数)books上行赋值的数据


def detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'detail.html', {'book': book})




class Testview(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]#认证后才可以访问
    authentication_classes = [JSONWebTokenAuthentication]#认证方式是jwt
    queryset = Book.objects.all()  # 将python对象转换为json对象，序列化
    serializer_class = bookserializer  # 从bookmanager导包


class Test2View(APIView):
    permission_classes = [permissions.IsAuthenticated]  # 认证后才可以访问
    authentication_classes = [JSONWebTokenAuthentication]  # 认证方式是jwt
    def get(self, requset):
        key = requset.GET.get('name', '')  # name=''或者为空时
        books = Book.objects.filter(name__contains=key)  # 查找
        # books=Book.objects.filter(name__contains='程序')#查找程序
        # 增加
        # c = requset.GET()  # 获取url全部参数
        # category = Book()
        # category.name = c.name
        # category.author = c.author
        # category.price = c.price
        # category.save()
        # # 修改书
        # for book in books:
        #     book.price = 50
        #     book.save()
        # # 删除书
        # for book in Book.objects.all():
        #     if book.price == '1212':
        #         book.delete()

        ss = bookserializer(books, many=True)
        return Response(ss.data)  # from rest_framework.response import Response

    def post(self, request):
        pass
