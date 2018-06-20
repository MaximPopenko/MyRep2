from django.urls import re_path, include
from products import views

urlpatterns = [
    re_path(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
    # path('', include('landing.urls')),
    # path('/products', include('products.urls')),
    # path('/orders', include('orders.urls')),
]
