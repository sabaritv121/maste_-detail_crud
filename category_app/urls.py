from django.urls import path

from category_app import views,sub_views,product_views

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
    path('edit_row/<int:pk>/', views.edit_row, name='edit_row'),

    # path('edit1',views.edit1,name='edit1'),


    #sub1
    # path('new',views.new,name='new'),
    # path('index1', views.index1, name='index1'),
    path("create_project",sub_views.create_project,name="create_project"),
   
    path('read1',sub_views.read1, name='read1'),

    path('product/<int:product_id>/toggle-active/', sub_views.toggle_button, name='toggle_category_active'),

####CREATE PRODUCT 
    path("create_product",product_views.product,name="create_product"),
    path("view",product_views.view,name="view"),
    path('create/<int:create_id>/toggle-active/', product_views.toggle, name='toggle_category_active'),





]


