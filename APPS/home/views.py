from django.shortcuts import render
from APPS.home.models import *

def index(request):
    # 获取导航菜单数据
    navigations = Navigation.objects.all()
    #分类菜单的数据
    #三个表 category  sub_menu sub_menu2
    categories = Category.objects.all()
    for category in categories:
        category.subs = category.submenu_set.all()
        for sub in category.subs:
            sub.subs2 = sub.submenu2_set.all()
     #轮播图数据
    banners = Banner.objects.all()
    return render(request,'index.html',{'navigations':navigations,'banners':banners,'categories':categories})