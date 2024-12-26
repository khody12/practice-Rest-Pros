from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product

from .serializers import ProductSerializer

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs): # HTTP -> Get
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) #create is within CreateModelMixin.
    
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_create(self, serializer): # if we want to assign something, 
        #say content is default blank, we can specifically assign it to something within this method
        print(serializer)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)



class ProductDetailAPIView(generics.RetrieveAPIView):
    # basically whats going on here is that within one of our py_clients, we now want to send a link
    #to an endpoint that pertains to a specific product. so we have a url that has a <int:pk> to support generic products.
    # this ProductDetailAPIview basically automates a lot of the process and allows us to simply set the queryset
    # we also set the serializer, and that is it! now it will automatically send back the correct product when we go to the correct url. 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

class ProductUpdateAPIView(generics.UpdateAPIView):
    # basically whats going on here is that within one of our py_clients, we now want to send a link
    #to an endpoint that pertains to a specific product. so we have a url that has a <int:pk> to support generic products.
    # this ProductDetailAPIview basically automates a lot of the process and allows us to simply set the queryset
    # we also set the serializer, and that is it! now it will automatically send back the correct product when we go to the correct url. 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductDestroyAPIView(generics.DestroyAPIView):
    # basically whats going on here is that within one of our py_clients, we now want to send a link
    #to an endpoint that pertains to a specific product. so we have a url that has a <int:pk> to support generic products.
    # this ProductDetailAPIview basically automates a lot of the process and allows us to simply set the queryset
    # we also set the serializer, and that is it! now it will automatically send back the correct product when we go to the correct url. 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
            


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()


# using a function view rather than the given generic class views. This is probably a good way to get started
#when learning. just to have a bit more of a granular understanding of whats going on here, class API views def easier tho

@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            #detail view
            #queryset = Product.objects.filter(pk=pk)
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data

            
            return Response(data)

        else: 
            #list view
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)
        
        #url_args??
        #get request -> detailview
        #get request -> detail view
        #list view
    if method == "POST":
        # basically what we have now, is our py_client is 
    
    
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer)
            # these two title and content lines are if we need to manually adjust something, in the real world
            # we might just have if serializer.is_valid, and then serializer.save
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)


# Create your views here.
