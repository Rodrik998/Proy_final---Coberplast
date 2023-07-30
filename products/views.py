import pandas as pd

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Value
from django.db.models.functions import Concat
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage

from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny

from admin_settings.models import Category, SubCategory

from products.models import Product


def Create_product(request):
    if request.method == 'POST' and request.FILES['']:      
        myfile = request.FILES['']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)              
        empexceldata = pd.read_excel(filename)        
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            obj = Product.objects.create(name=dbframe.name,SKU=dbframe.SKU,price=dbframe.price,description=dbframe.description)           
            obj.save()
        return render(request, 'Products/catalogue.html', {
            'uploaded_file_url': uploaded_file_url
        })   
    return render(request, 'Products/catalogue.html',{})


class ListProducts(APIView):
    pass