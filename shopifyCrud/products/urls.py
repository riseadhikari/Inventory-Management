from django.urls import path, include  
from . import views 
urlpatterns = [
    path('',views.products,name='all-products'),
    path('all-tags/',views.all_tags, name='all-tags'),
    path('add-product/', views.add_product, name='add-product'),
    path('add-tag/', views.add_tag, name='add-tag'),
    path('delete-product/<uuid:pk>/',views.delete_product,name='delete-product'),
    path('delete-tag/<uuid:pk>/',views.delete_tag,name='delete-tag'),
    path('single-product/<uuid:pk>/', views.single_product,name='single-product'),
    path('update-product/<uuid:pk>/',views.update_product,name='update-product'),
    path('export/',views.export_csv,name='export-csv'),
]