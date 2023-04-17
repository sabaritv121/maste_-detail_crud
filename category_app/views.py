from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

# Create your views here.
from category_app.models import Category, Product


def home(request):
    return render(request,'home.html')


def index(request):
    return render(request,'index.html')


def create(request):
    data = Category(name=request.POST['name'] )
    data.is_active = False
    data.save()
    return redirect('/')

def read(request):
    read = Category.objects.order_by('-id')
    context = {'read':read}
    return render(request, 'result.html', context)


def edit(request, id):
    data = Category.objects.get(id=id)
    context = {'data': data}
    return render(request, 'edit.html', context)
    


def update(request, id):
    data = Category.objects.get(id=id)
    data.name = request.POST['name']
    data.is_active = False
    data.save()
    return redirect('/')


def delete(request, id):
    obj = Category.objects.get(id=id)
    obj.delete()
    return redirect('/')




# def category_enable(request, id):
#     data = get_object_or_404(Category, id=id)
#     if data.is_active == True:
#         data.is_active = False
#         data.save()
#     else:
#         pass
#     return category_view(request)

# def category_enable(request,id):
#     data=Category.objects.get(id=id)
#     if data.is_active:
#         data.is_active=False

#     else:

#         data.is_active=True
    
#     data.save()         
#     return redirect(read)
#sub1

@csrf_exempt
def toggle_category_active(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Category not found'})
    
    category.is_active = not category.is_active
    category.save()
    
    return JsonResponse({'status': 'success', 'is_active': category.is_active})

def index1(request):
    return render(request,'sub1/index.html')


def create1(request):
    data = Product(name=request.POST['name'] )
    
    data.is_active = False
    data.save()
    return redirect('/')

def read1(request):
    read = Product.objects.all()
    context = {'read':read}
    return render(request, 'result.html', context)


def edit1(request, id):
    data = Product.objects.get(id=id)
    context = {'data': data}
    return render(request, 'edit.html', context)


def update1(request, id):
    data = Product.objects.get(id=id)
    data.name = request.POST['name']
    data.is_active = False
    data.save()
    return redirect('/')


def delete1(request, id):
    obj = Product.objects.get(id=id)
    obj.delete()
    return redirect('/')