@csrf_exempt
def create(request):
    values=Products.objects.all()

    if request.method == 'POST':
     
        
        product = request.POST.get('category')
        print(category)
        print("k")
        product_name = request.POST.get('product_name')
        print("product")
        print(product_name)
        # # Create a new project instance
        project = Product(category_id=category, product_name=product_name)
        project.save()

        response_data = {'status': 'success', 'message': 'Project type created successfully'}
    # else:
    #     response_data = {'status': 'error', 'message': 'Invalid request'}
        
        return JsonResponse(response_data)
    return render(request,'sub1/home.html',{'values':values})