from django.urls import path

from category_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('read/',views.read,name='read'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    # path('category_enable/<int:id>', views.category_enable, name='category_enable'),
    path('category/<int:category_id>/toggle-active/', views.toggle_category_active, name='toggle_category_active'),

    path('edit1',views.edit1,name='edit1'),


    #sub1

    path('index1', views.index1, name='index'),
    path('create1/', views.create1, name='create'),
    path('read1/', views.read1, name='read'),
    path('edit1/<int:id>', views.edit1, name='edit'),
    path('edit1/update1/<int:id>', views.update1, name='update'),
    path('delete1/<int:id>', views.delete1, name='delete'),
]