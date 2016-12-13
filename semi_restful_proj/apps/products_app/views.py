from django.shortcuts import render, redirect
from models import Product
# Functions here will delegate to the correct method based on the HTTP verb
def users(request):
    if request.method == "POST":
        return create(request)
    # Else it's a GET, send to index method to return HTML
    return index(request)

def users_w_id(request, id):
    if request.method == "POST":
        return update(request, id)
    return show(request, id)
# *************************************************************************

# GET /users
def index(request):
    # Retrieve all products to display in template
    products = Product.objects.all()
    return render(request, 'products_app/index.html', { 'products': products })

# POST /users
def create(request):
    Product.objects.create(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
    return redirect('/products')

# GET /users/new
def new(request):
    return render(request, 'products_app/new.html')

# GET /users/<id>
def show(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products_app/show.html', { 'product' : product })

# POST /users/<id>
# Note: generally this route will use the PUT or PATCH HTTP verb...
def update(request, id):
    # Outsource the update logic to Product.manager
    Product.objects.update(id, request.POST)
    return redirect('/products')

# GET /users/<id>/edit
def edit(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products_app/edit.html', { 'product' : product })

# POST /users/<id>/destroy
def destroy(request, id):
    Product.objects.get(id=id).delete()
    return redirect('/products')