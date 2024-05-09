from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView
from store.forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from store.models import Bikes,FavouriteItem,Brand,Order,OrderItems

# Create your views here.



class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"data":form})
   
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        return render(request,"login.html",{"data":form})
  


class SignInView(View):
    def get(slef,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"data":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=u_name,password=pwd)
            if user_object:
                login(request,user_object)
                return redirect("index")
        messages.error(request,"invalid credentials")
        return render(request,"login.html",{"data":form})
   
           
   

class IndexView(View):
    def get(self,request,*args,**kwargs):
        qs=Bikes.objects.all()
        brand=Brand.objects.all()

        selected_brand=request.GET.get("brand")
        if selected_brand:
            qs=qs.filter(brand_object__name=selected_brand)
        return render(request,"index.html",{"data":qs,"brand":brand})
    


class BikesDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        gs=Bikes.objects.get(id=id)
        return render(request,"detail.html",{"data":gs})



class AddToWishlistView(View):
    def post(self,request,*args,**kwargs): 
        id=kwargs.get("pk")
        bike_object=Bikes.objects.get(id=id)
        FavouriteItem.objects.create(
            Bikes_object=bike_object,
            Favourite_object=request.user.cart   
        )
        return redirect("index")
    


class WishlistListView(View):
    def get(self,request,*args,**kwargs):
        qs=request.user.cart.cartitem.all()
        return render(request,"wishlist.html",{"data":qs})


class RemoveWishlistItems(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        FavouriteItem.objects.get(id=id).delete()
        return redirect("wishlist")



class SlotBooking(View):
    def get(self,request,*args,**kwargs):
        return render(request,"book.html")
    
    def post(self,request,*args,**kwargs):
        email=request.POST.get("email")
        phone=request.POST.get("phone")

        Order.objects.create(
            user_object=request.user,
            email=email,
            phone=phone
        )
        return redirect("index")
        # favourite_objects=request.user.cart.cartitem
        # for b in favourite_objects:
        #     OrderItems.objects.create(
        #         order_object=booked_obj,
        #         basket_item_object=b,
        #     )
            

        # id=kwargs.get("pk")
        # car_obj=FavouriteItem.objects.get(id=id)
        # OrderItems.objects.create(
        #     order_object=booked_obj,
        #     basket_item_object=car_obj

        # )