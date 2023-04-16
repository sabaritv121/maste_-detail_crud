from django.shortcuts import render, redirect

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
    read = Category.objects.all()
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



#sub1



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