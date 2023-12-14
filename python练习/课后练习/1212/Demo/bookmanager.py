from rest_framework import serializers

from Book.models import Book

#查询所以数据
class bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book #同models中BooK包
        fields = '__all__'