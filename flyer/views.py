from django.shortcuts import render,HttpResponse,redirect
from .endpoints import get_category,get_page_format,get_stopper_format,get_poster_format,get_project_list,get_project_pdf
import requests
from  .redirects import *
# Create your views here.
def create_flyer(request):
  if request.method == 'POST':
    name=request.POST.get('name')
    page_format = request.POST.get('page_format')
    stopper_format = request.POST.get('stopper_format')
    poster_format = request.POST.get('poster_format')
    category=request.POST.get('category')
    number_of_pages=request.POST.get('number_of_pages')
    number_of_products = request.POST.get("number_of_products")
    client=1
    url = 'http://127.0.0.1:8000/api/create_project/'
    headers={'Authorization':'Token 2766efb8f49305ec9d797feb2efc3b85725055fb'}
    payload = {'name':name,'page_format':page_format,'stopper_format':stopper_format,'poster_format':poster_format,'category':category,'number_of_pages':number_of_pages,'client':client, "number_of_products":number_of_products}
    r = requests.post(url, data=payload, headers=headers)
    url_go=redirect_url()
    if r.status_code == 200:
      data = r.json()
      return HttpResponse("success")

  context = {}
  categories=get_category()
  page_format=get_page_format()
  stopper_format=get_stopper_format()
  poster_format=get_poster_format()
  context={'categories':categories,'page_format':page_format,'stopper_format':stopper_format,'poster_format':poster_format}
  return render(request,'flyer/index.html',context)


def project_list(request):
  project_list=get_project_list()
  project_pdf=get_project_pdf()
  return render(request,'flyer/project_list.html',{'project_list':project_list,'project_pdf':project_pdf})

