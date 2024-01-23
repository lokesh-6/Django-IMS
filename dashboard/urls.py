from django.urls import path 
from . import views

urlpatterns=[
    path("dashboard/",views.index,name="index"),
    path("staff/",views.staff,name='staff'),
    path("stats/",views.stats,name='stats'),
    path("product/",views.products,name='product'),
    path("order/",views.order,name='order'),
    path("product/delete/<int:pk>/",views.product_delete,name='product_del'),
    path("product/update/<int:pk>/",views.product_edit,name='product_update'),
    path("product/detail/<int:pk>/",views.staff_detail,name='staff_detail'),
]