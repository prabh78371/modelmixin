from django.shortcuts import render
from .models import Product
from .serializers import productserializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# Create your views here.

# to see all data
class productlist(GenericAPIView,ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = productserializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args, **kwargs)

# to create new data
class productcreate(GenericAPIView,CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = productserializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args, **kwargs)

# get specific number of row
class productretrive(GenericAPIView,RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = productserializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args, **kwargs)

# update the data
class productupdate(GenericAPIView,UpdateModelMixin):
    queryset = Product.objects.all()
    serializer_class = productserializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args, **kwargs)

# to delete data
class productdelete(GenericAPIView,DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = productserializer

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args, **kwargs)



