from django.shortcuts import render
from rest_framework.views import APIView

from smallshop.models import user, place, shop


# Create your views here.

def shouye(request):
    detailed_address = place.objects.all()
    return render(request, 'shouye.html', {'detailed': detailed_address})


def shangpi(request):
    detailed_address = place.objects.all()
    for pl in detailed_address:
        pl.list = shop.objects.filter(place_id=pl).values('name', 'price')
    return render(request, 'yonghu.html', {'detailed': detailed_address})


def zuce1(request):
    detailed_address = place.objects.all()
    return render(request, 'zhuce.html', {'detailed': detailed_address})


#
# def denglu(request):
#     name = request.GET.get('username')
#     password = request.GET.get('password')
#     user_message = user.objects.filter(username=name, password=password).count()
#     if user_message == 1:
#         return render(request, 'yonghu.html')
#     else:
#         return render(request, 'shouye.html')


class denglu(APIView):
    def get(self, request):
        name = request.GET.get('username')
        password = request.GET.get('password')
        place_a = request.GET.get('place_')
        print(name, password, place_a)
        detailed_address = place.objects.all()
        place_1 = place.objects.get(place_name=place_a)
        sop = shop.objects.filter(place_id=place_1)
        ser_message = user.objects.filter(name=name, password=password, place=place_1).count()
        print(ser_message)
        if ser_message == 1:
            return render(request, 'yonghu.html', {'sop': sop}, )
        else:
            return render(request, 'shouye.html', {'detailed': detailed_address})

    def post(self, request):
        pass


class zuce(APIView):
    def get(self, request):
        name = request.GET.get('username')
        us = user.objects.filter(username=name).count()
        detailed_address = place.objects.all()
        if us == 1:
            print('用户名重复')
            return render(request, 'zhuce.html', {'detailed': detailed_address}, 'utf-8')
        else:
            user_user = user()
            user_user.name = name
            user_user.password = request.GET.get('password')
            place_ = request.GET.get('place_')
            place1 = place.objects.get(place_name=place_)
            user_user.place = place1
            user_user.save()
            detailed_address = place.objects.all()
            return render(request, 'shouye.html', {'detailed': detailed_address})

    def post(self, request):
        pass


class goumai(APIView):
    def get(self, request):
        name = request.GET.get('name')
        place_ = request.GET.get('place')
        place1 = place.objects.get(place_name=place_)
        sop = shop.objects.filter(place_id=place1)
        shuliang = shop.objects.filter(name=name, place_id=place1)
        for i in shuliang:
            x=i.residual_quantity
            i.residual_quantity = x-1
            i.save()
        return render(request, 'yonghu.html', {'sop': sop}, )

    def post(self, request):
        pass
