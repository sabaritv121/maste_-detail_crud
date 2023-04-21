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
        print("k")
        product_name = request.POST.get('product_name')
        print("product")
        print(product_name)
        # # Create a new project instance
        project = Product(category_id=category, product_name=product_name,is_active = True)
        project.save()

        response_data = {'status': 'success', 'message': 'Project type created successfully'}
    # else:
    #     response_data = {'status': 'error', 'message': 'Invalid request'}
        
        return JsonResponse(response_data)
    return render(request,'sub1/home.html',{'values':values})


def read1(request):
    readd = Product.objects.order_by('-id')
    context = {'readd':readd}
    return render(request, 'sub1/res.html', context)



@csrf_exempt
def toggle_button(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
        print(product)
        print("k")
    except Product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found'})
    
    product.is_active = not product.is_active
    product.save()
    
    return JsonResponse({'status': 'success', 'is_active': product.is_active})
