from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

# Create your views here.
from category_app.models import Category,Product
from .forms import ProductForm


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
    return render(request, 'resultt.html', context)


def edit(request, id):
    data = Category.objects.get(id=id)
    context = {'data': data}
    return render(request, 'edit.html', context)
    # return redirect('/')
    


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

# def index1(request):
#     return render(request,'sub1/index.html')


# #createdetail
# def new(request):
#     return render(request,'sub1/new.html')




#subcategory creation

#add subcategory
# @csrf_exempt
# def create_project(request):
#     values=Category.objects.all()

#     if request.method == 'POST':
#         category = request.POST.get('category')
#         print(category)
#         product_name = request.POST.get('product_name')
       
#         # # Create a new project instance
#         project = Product(category=category, product_name=product_name)
#         project.save()

#         response_data = {'status': 'success', 'message': 'Project type created successfully'}
#     # else:
#     #     response_data = {'status': 'error', 'message': 'Invalid request'}
        
#         return JsonResponse(response_data)
#     return render(request,'sub1/index.html',{'values':values})





   



