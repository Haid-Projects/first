from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from decimal import Decimal
from .models import *


def main(request):
    return render(request, "main.html", {"main" : "main"})

###        ###
# Apartments #
###        ###

def apartments_type_options(request):
    return render(request, "apartment/apartment_type_options.html", {"main" : "main"})

def filter_apartments_form(request):
    return render(request, "apartment/filter_apartments_form.html")

def filter_apartments(request):
    size = request.POST["size"]
    price = request.POST["price"]
    floor = request.POST["floor"]

    type = request.POST["type"]
    
    apartments_for_renting = ApartmentForRenting.objects.filter(size__gt=0)

    if type == "selling" :
        result = None
        if  request.POST.get("size") :             
            if  request.POST.get("price") : 
                if  request.POST.get("floor") : 
                    result = ApartmentForSelling.objects.filter(size__range=(int(size)-10, int(size)+10),price__lte=price,floor=floor)
                else :
                    result = ApartmentForSelling.objects.filter(size__range=(int(size)-10, int(size)+10),price__lte=price)
            else :
                if  request.POST.get("floor") : 
                    result = ApartmentForSelling.objects.filter(size__range=(int(size)-10, int(size)+10),floor=floor)

                else :
                    result = ApartmentForSelling.objects.filter(size__range=(int(size)-10, int(size)+10))                    
       
        else :
            if  request.POST.get("price") : 
                if  request.POST.get("floor") : 
                    result = ApartmentForSelling.objects.filter(price__lte=price,floor=floor)
                else :
                    result = ApartmentForSelling.objects.filter(price__lte=price)
            else :
                if  request.POST.get("floor") : 
                    result = ApartmentForSelling.objects.filter(floor=floor)

                else :
                    result = ApartmentForSelling.objects.all()                
                    
        return render(request, "apartment/apartments_for_selling.html", {"apartments": list(result)})

    else :
        result = None
        if  request.POST.get("size") :             
            if  request.POST.get("price") : 
                result = ApartmentForRenting.objects.filter(size__range=(int(size)-10, int(size)+10),price__lte=price)
            else :
                result = ApartmentForRenting.objects.filter(size__range=(int(size)-10, int(size)+10))                    
       
        else :
            if  request.POST.get("price") : 
                result = ApartmentForRenting.objects.filter(price__lte=price)
            else :
                result = ApartmentForRenting.objects.all()             
        return render(request, "apartment/renting/apartments_for_renting.html", {"apartments": list(result)})

   

##
# Selling
##
    

def apartments_for_selling(request):
    apartments = ApartmentForSelling.objects.all()
    return render(request, "apartment/apartments_for_selling.html", {"apartments": list(apartments)})

def apartment_for_selling_details(request , id):
    apartment = ApartmentForSelling.objects.get(id=id)
    return render(request, "apartment/apartment_for_selling_details.html", {"apartment": apartment})

def create_apartment_for_selling_form(request):
    return render(request, "apartment/create_apartment_for_selling.html")

def create_apartment_for_selling(request):
    selling_apartment = ApartmentForSelling()
    selling_apartment.location = request.POST["location"]
    selling_apartment.size = request.POST["size"]
    selling_apartment.price = request.POST["price"]
    selling_apartment.phone_number = request.POST["phone_number"]
    selling_apartment.property = request.POST["property"]
    selling_apartment.view = request.POST["view"]
    selling_apartment.floor = request.POST["floor"]
    selling_apartment.cladding = request.POST["cladding"]
    selling_apartment.room_number = request.POST["room_number"]
    selling_apartment.bathrooms = request.POST["bathrooms"]
    selling_apartment.save()
    return apartments_for_selling(request)

def update_apartment_for_selling(request, id):
    selling_apartment = ApartmentForSelling(pk=id)
    selling_apartment.location = request.POST["location"]
    selling_apartment.size = request.POST["size"]
    selling_apartment.price = request.POST["price"]
    selling_apartment.phone_number = request.POST["phone_number"]
    selling_apartment.property = request.POST["property"]
    selling_apartment.view = request.POST["view"]
    selling_apartment.floor = request.POST["floor"]
    selling_apartment.cladding = request.POST["cladding"]
    selling_apartment.room_number = request.POST["room_number"]
    selling_apartment.bathrooms = request.POST["bathrooms"]
    selling_apartment.save()
    return apartments_for_selling(request)

def update_apartment_for_selling_form(request , id):
    apartment =  ApartmentForSelling.objects.get(id=id)
    return render(request, "apartment/update_apartment_for_selling_form.html", {"apartment": apartment})

def delete_apartment_for_selling(request , id):
    ApartmentForSelling.objects.filter(id=id).delete()
    apartments = ApartmentForSelling.objects.all()
    return render(request, "apartment/apartments_for_selling.html", {"apartments": list(apartments)})

# def apartments_for_selling(request):
#     apartments = ApartmentForSelling.objects.all()
#     return render(request, "apartment/apartments_for_selling.html", {"apartments": list(apartments)})

def change_apartments_for_selling_state(request, id):
    ApartmentForSelling.objects.filter(id=id).update(is_sold=request.GET["is_sold"])
    apartment = ApartmentForSelling.objects.get(id=id)
    return render(request, "apartment/apartment_for_selling_details.html", {"apartment": apartment})


##
# Renting
##

def apartments_for_renting(request):
    apartments = ApartmentForRenting.objects.all()
    return render(request, "apartment/renting/apartments_for_renting.html", {"apartments": list(apartments)})

def apartment_for_renting_details(request , id):
    apartment = ApartmentForRenting.objects.get(id=id)
    return render(request, "apartment/renting/apartments_for_renting_details.html", {"apartment": apartment})

def create_apartment_for_renting_form(request):
    return render(request, "apartment/renting/create_apartment_for_renting.html")

def create_apartment_for_renting(request):
    renting_apartment = ApartmentForRenting()
    renting_apartment.location = request.POST["location"]
    renting_apartment.size = request.POST["size"]
    renting_apartment.price = request.POST["price"]
    renting_apartment.phone_number = request.POST["phone_number"]
    renting_apartment.renting_period = request.POST["renting_period"]
    renting_apartment.view = request.POST["view"]
    renting_apartment.floor = request.POST["floor"]
    renting_apartment.cladding = request.POST["cladding"]
    renting_apartment.room_number = request.POST["room_number"]
    renting_apartment.bathrooms = request.POST["bathrooms"]
    renting_apartment.save()
    return apartments_for_renting(request)

def update_apartment_for_renting(request, id):
    renting_apartment = ApartmentForRenting(pk=id)
    renting_apartment.location = request.POST["location"]
    renting_apartment.size = request.POST["size"]
    renting_apartment.price = request.POST["price"]
    renting_apartment.phone_number = request.POST["phone_number"]
    renting_apartment.renting_period = request.POST["renting_period"]
    renting_apartment.view = request.POST["view"]
    renting_apartment.floor = request.POST["floor"]
    renting_apartment.cladding = request.POST["cladding"]
    renting_apartment.room_number = request.POST["room_number"]
    renting_apartment.bathrooms = request.POST["bathrooms"]
    renting_apartment.save()
    return apartments_for_renting(request)

def update_apartment_for_renting_form(request , id):
    apartment =  ApartmentForRenting.objects.get(id=id)
    return render(request, "apartment/renting/update_apartment_for_renting_form.html", {"apartment": apartment})

def delete_apartment_for_renting(request , id):
    ApartmentForRenting.objects.filter(id=id).delete()
    apartments = ApartmentForRenting.objects.all()
    return render(request, "apartment/renting/apartments_for_renting.html", {"apartments": list(apartments)})

# def apartments_for_renting(request):
#     apartments = ApartmentForRenting.objects.all()
#     return render(request, "apartment/renting/apartments_for_renting.html", {"apartments": list(apartments)})

def change_apartments_for_renting_state(request, id):
    ApartmentForRenting.objects.filter(id=id).update(is_sold=request.GET["is_sold"])
    apartment = ApartmentForRenting.objects.get(id=id)
    return render(request, "apartment/renting/apartments_for_renting_details.html", {"apartment": apartment})


###   ###
# Shops #
###   ###
def shops_type_options(request):
    return render(request, "shop/shop_type_options.html", {"main" : "main"})

def filter_shops_form(request):
    return render(request, "shop/filter_shops_form.html")

def filter_shops(request):
    size = request.POST["size"]
    price = request.POST["price"]
    type = request.POST["type"]
    
    if type == "selling" :
        result = None
        if  request.POST.get("size") :             
            if  request.POST.get("price") : 
                result = ShopForSelling.objects.filter(size__range=(int(size)-10, int(size)+10),price__lte=price)
            else :
                result = ShopForSelling.objects.filter(size__range=(int(size)-10, int(size)+10))                    
       
        else :
            if  request.POST.get("price") : 
                result = ShopForSelling.objects.filter(price__lte=price)
            else :
                result = ShopForSelling.objects.all()             
        return render(request, "shop/selling/shops_for_selling.html", {"shops": list(result)})


    else :
        result = None
        if  request.POST.get("size") :             
            if  request.POST.get("price") : 
                result = ShopForRenting.objects.filter(size__range=(int(size)-10, int(size)+10),price__lte=price)
            else :
                result = ShopForRenting.objects.filter(size__range=(int(size)-10, int(size)+10))                    
    
        else :
            if  request.POST.get("price") : 
                result = ShopForRenting.objects.filter(price__lte=price)
            else :
                result = ShopForRenting.objects.all()             
        return render(request, "shop/renting/shops_for_renting.html", {"shops": list(result)})


##
# Selling
##

def shops_for_selling(request):
    shops = ShopForSelling.objects.all()
    return render(request, "shop/selling/shops_for_selling.html", {"shops": list(shops)})


def shop_for_selling_details(request , id):
    shop = ShopForSelling.objects.get(id=id)
    return render(request, "shop/selling/shop_for_selling_details.html", {"shop": shop})



def create_shop_for_selling_form(request):
    return render(request, "shop/selling/create_shop_for_selling.html")


def create_shop_for_selling(request):
    selling_shop = ShopForSelling()
    selling_shop.location = request.POST["location"]
    selling_shop.size = request.POST["size"]
    selling_shop.price = request.POST["price"]
    selling_shop.phone_number = request.POST["phone_number"]
    selling_shop.property = request.POST["property"]
    selling_shop.save()
    
    #shops = ApartmentForSelling.objects.all()
    return shops_for_selling(request)

def update_shop_for_selling(request, id):
    selling_shop = ShopForSelling(pk=id)
    selling_shop.location = request.POST["location"]
    selling_shop.size = request.POST["size"]
    selling_shop.price = request.POST["price"]
    selling_shop.phone_number = request.POST["phone_number"]
    selling_shop.property = request.POST["property"]
    selling_shop.save()
    return shops_for_selling(request)

def update_shop_for_selling_form(request , id):
    shop =  ShopForSelling.objects.get(id=id)
    return render(request, "shop/selling/update_shop_for_selling_form.html", {"shop": shop})


def delete_shop_for_selling(request , id):
    ShopForSelling.objects.filter(id=id).delete()
    shops = ShopForSelling.objects.all()
    return render(request, "shop/selling/shops_for_selling.html", {"shops": list(shops)})

def change_shops_for_selling_state(request, id):
    ShopForSelling.objects.filter(id=id).update(is_sold=request.GET["is_sold"])
    shop = ShopForSelling.objects.get(id=id)
    return render(request, "shop/selling/shop_for_selling_details.html", {"shop": shop})


##
# Renting
##

def shops_for_renting(request):
    shops = ShopForRenting.objects.all()
    return render(request, "shop/renting/shops_for_renting.html", {"shops": list(shops)})

def shop_for_renting_details(request , id):
    shop = ShopForRenting.objects.get(id=id)
    return render(request, "shop/renting/shop_for_renting_details.html", {"shop": shop})



def create_shop_for_renting_form(request):
    return render(request, "shop/renting/create_shop_for_renting.html")

def create_shop_for_renting(request):
    renting_shop = ShopForRenting()
    renting_shop.location = request.POST["location"]
    renting_shop.size = request.POST["size"]
    renting_shop.price = request.POST["price"]
    renting_shop.phone_number = request.POST["phone_number"]
    renting_shop.renting_period = request.POST["renting_period"]
    renting_shop.save()
    
    #shops = ApartmentForrenting.objects.all()
    return shops_for_renting(request)

def update_shop_for_renting(request, id):
    renting_shop = ShopForRenting(pk=id)
    renting_shop.location = request.POST["location"]
    renting_shop.size = request.POST["size"]
    renting_shop.price = request.POST["price"]
    renting_shop.phone_number = request.POST["phone_number"]
    renting_shop.renting_period = request.POST["renting_period"]
    renting_shop.save()
    return shops_for_renting(request)

def update_shop_for_renting_form(request , id):
    shop =  ShopForRenting.objects.get(id=id)
    return render(request, "shop/renting/update_shop_for_renting_form.html", {"shop": shop})


def delete_shop_for_renting(request , id):
    ShopForRenting.objects.filter(id=id).delete()
    shops = ShopForRenting.objects.all()
    return render(request, "shop/renting/shops_for_renting.html", {"shops": list(shops)})

def change_shops_for_renting_state(request, id):
    ShopForRenting.objects.filter(id=id).update(is_sold=request.GET["is_sold"])
    shop = ShopForRenting.objects.get(id=id)
    return render(request, "shop/renting/shop_for_renting_details.html", {"shop": shop})


###   ###
# Lands #
###   ###

def filter_lands_form(request):
    return render(request, "land/filter_lands_form.html")

def filter_lands(request):
    size = request.POST["size"]
    price = request.POST["price"]    
    result = None
    
    if  request.POST.get("size") :             
        if  request.POST.get("price") : 
            result = Land.objects.filter(size__range=(int(size)-10, int(size)+10),price__lte=price)
        else :
            result = Land.objects.filter(size__range=(int(size)-10, int(size)+10))                    
    
    else :
        if  request.POST.get("price") : 
            result = Land.objects.filter(price__lte=price)
        else :
            result = Land.objects.all()             
    return render(request, "land/lands.html", {"lands": list(result)})



def lands(request):
    lands = Land.objects.all()
    return render(request, "land/lands.html", {"lands": list(lands)})


def land_details(request , id):
    land = Land.objects.get(id=id)
    return render(request, "land/land_details.html", {"land": land})

def create_land_form(request):
    return render(request, "land/create_land.html")


def create_land(request):
    land = Land()
    land.location = request.POST["location"]
    land.size = request.POST["size"]
    land.price = request.POST["price"]
    land.phone_number = request.POST["phone_number"]
    land.property = request.POST["property"]
    land.save()
    
    return lands(request)

def update_land(request, id):
    land = Land(pk=id)
    land.location = request.POST["location"]
    land.size = request.POST["size"]
    land.price = request.POST["price"]
    land.phone_number = request.POST["phone_number"]
    land.property = request.POST["property"]
    land.save()
    return lands(request)

def update_land_form(request , id):
    land =  Land.objects.get(id=id)
    return render(request, "land/update_land_form.html", {"land": land})


def delete_land(request , id):
    Land.objects.filter(id=id).delete()
    lands = Land.objects.all()
    return render(request, "land/lands.html", {"lands": list(lands)})

def change_lands_state(request, id):
    Land.objects.filter(id=id).update(is_sold=request.GET["is_sold"])
    land = Land.objects.get(id=id)
    return render(request, "land/land_details.html", {"land": land})
