from django.shortcuts import render, redirect
from .models import Product, Tag
from .forms import ProductForm, TagForm
from django.http import HttpResponse

import csv


def products(request):

	products = Product.objects.all()
	return render(request,'products/products.html',context={'products':products})

def single_product(request,pk):

	product = Product.objects.get(id=pk)
	return render(request,'products/single-product.html',context={'product':product})

def add_product(request):

	form = ProductForm()
	if request.method == 'POST':

		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('all-products')

	return render(request,'products/product-form.html',context={'form':form})

def update_product(request,pk):
	product = Product.objects.get(id=pk)
	form = ProductForm(instance=product)
	if request.method == 'POST':
		form = ProductForm(request.POST,instance=product)
		if form.is_valid():
			form.save()
			return redirect('all-products')
	return render(request,'products/product-form.html',context={'form':form})
def delete_product(request,pk):
	product = Product.objects.get(id=pk)
	product.delete()

	return redirect('all-products')

def all_tags(request):

	tags = Tag.objects.all()
	return render(request,'products/tags.html',context={'tags':tags})

def add_tag(request):
	form = TagForm()
	if request.method == 'POST':
		form = TagForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('all-tags')

	return render(request, 'products/tag-form.html',context={'form':form})

def delete_tag(request,pk):
	tag = Tag.objects.get(id=pk)
	tag.delete()
	return redirect('all-tags')

def export_csv(request):
	products = Product.objects.all()
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=inventory_report.csv'

	fieldnames = ['Name','Total Amount','Tags','Expiry Date']
	writer = csv.writer(response)
	writer.writerow(fieldnames)

	tags = ''


	for product in products:
		for tag in product.prod_tags.all():
			tags = tags + tag.name + ','
		writer.writerow([product.prod_name,product.prod_amount,tags,product.prod_expires])

	return response
