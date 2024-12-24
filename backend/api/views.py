from django.shortcuts import render
from django.forms.models import model_to_dict
#from django.http import JsonResponse
import json
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    # basically what we have now, is our py_client is 
    model_data = Product.objects.all().order_by("?").first() # this would give random data, but i have the same price for my 2 prods rn
    data = {}
    if model_data:
         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
         
    return Response(data)


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