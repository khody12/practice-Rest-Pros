from django.shortcuts import render
from django.forms.models import model_to_dict


from products.models import Product
from products.serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # basically what we have now, is our py_client is 
    
    data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save() creates an object from the serializer data
        #instance = form.save()
        print(serializer.data)
        return Response(serializer.data)

    return Response({"invalid": "not good data"})

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     # basically what we have now, is our py_client is 
#     instance = Product.objects.all().order_by("?").first() # this would give random data, but i have the same price for my 2 prods rn
#     data = {}
#     if instance:
#          #data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#          # productSerializer basically does what the above does. ^^
#          data = ProductSerializer(instance).data
         
#     return Response(data)


# the tedious way, aka the very very bad way
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
#     
# request is an HttpRequest from django
#     #request.body
#      # byte string of Json Data

#     print(request.GET) # url query params
#     print(request.POST)
#     body = request.body
    
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data)

    
#     return JsonResponse(data)



# # Create your views here.