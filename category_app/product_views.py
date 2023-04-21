from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import JsonResponse
from category_app.models import Category,Product,Create


@csrf_exempt
def product(request):
    data=Product.objects.all()
 

    if request.method == 'POST':
     
        
        subcategory = request.POST.get('subcategory')
        print(subcategory)
    
        print("k")
        product = request.POST.get('product')
        print(subcategory)

        price = request.POST.get('price')
        print(price)

        # # Create a new project instance
        project = Create(subcategory_id=subcategory, product=product,price = price,is_active= True)
        project.save()

        response_data = {'status': 'success', 'message': 'Product created successfully'}
    # else:
    #     response_data = {'status': 'error', 'message': 'Invalid request'}
        
        return JsonResponse(response_data)
    return render(request,'sub2/home2.html',{'data':data})



def view(request):
    object = Create.objects.all()
    print(object)
    context = {'object':object}
    return render(request, 'sub2/table.html', context)
    

@csrf_exempt
def toggle(request,create_id):
    try:
        create = Create.objects.get(id=create_id)
        
    except create.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found'})
    
    create.is_active = not create.is_active
    create.save()
    
    return JsonResponse({'status': 'success', 'is_active': create.is_active})
