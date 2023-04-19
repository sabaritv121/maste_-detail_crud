from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import JsonResponse
from category_app.models import Category,Product



@csrf_exempt
def create_project(request):
    values=Category.objects.all()

    if request.method == 'POST':
        category = request.POST.get('category')
        print(category)
        product_name = request.POST.get('product_name')
       
        # # Create a new project instance
        project = Product(category=category, product_name=product_name)
        project.save()

        response_data = {'status': 'success', 'message': 'Project type created successfully'}
    # else:
    #     response_data = {'status': 'error', 'message': 'Invalid request'}
        
        return JsonResponse(response_data)
    return render(request,'sub1/home.html',{'values':values})


def read1(request):
    readd = Product.objects.all()
    context = {'readd':readd}
    return render(request, 'sub1/res.html', context)