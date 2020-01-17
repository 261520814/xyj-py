from django.urls import path

from adm.views import index, ditch, goods, order

app_name = 'adm'
urlpatterns = [
    path('', index.login, name='login'),
    path('login_c', index.login_c, name='login_c'),
    path('logout', index.logout, name='logout'),
    path('home', index.home, name='home'),
    path('welcome', index.welcome, name='welcome'),

    path('ditch_list', ditch.list, name='ditch_list'),
    path('ditch_add', ditch.add, name='ditch_add'),
    path('ditch_add_c', ditch.add_c, name='ditch_add_c'),
    path('ditch_del', ditch.del_c, name='ditch_del'),


    path('goods_list', goods.list, name='goods_list'),
    path('goods_del', goods.del_c, name='goods_del'),

    path('order_list', order.list, name='order_list'),
]