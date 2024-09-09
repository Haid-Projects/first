from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path("main/", views.main),
    ##
    # Apartments
    ##
    path("apartments-type-options/", views.apartments_type_options),
    path("filter-apartments-form/", views.filter_apartments_form),
    path("filter-apartments", views.filter_apartments),

    # Selling
    path("apartments-for-selling/", views.apartments_for_selling),
    path("create-apartment-for-selling-form/", views.create_apartment_for_selling_form),
    path("create-apartment-for-selling", views.create_apartment_for_selling),
    
    path("change-apartment-for-selling-state/<id>", views.change_apartments_for_selling_state),
    path("apartment-for-selling-details/<id>/", views.apartment_for_selling_details),

    path("update-apartment-for-selling-form/<id>/", views.update_apartment_for_selling_form),
    path("update-apartment-for-selling/<id>", views.update_apartment_for_selling),
    path("delete-apartment-for-selling/<id>/", views.delete_apartment_for_selling),
    
    
    # Renting
    path("apartments-for-renting/", views.apartments_for_renting),
    path("create-apartment-for-renting-form/", views.create_apartment_for_renting_form),
    path("create-apartment-for-renting", views.create_apartment_for_renting),
    
    path("change-apartment-for-renting-state/<id>", views.change_apartments_for_renting_state),
    path("apartment-for-renting-details/<id>/", views.apartment_for_renting_details),

    path("update-apartment-for-renting-form/<id>/", views.update_apartment_for_renting_form),
    path("update-apartment-for-renting/<id>", views.update_apartment_for_renting),
    path("delete-apartment-for-renting/<id>/", views.delete_apartment_for_renting),
    
    
    ##
    # Shops
    ##
    path("shops-type-options/", views.shops_type_options),

    path("filter-shops-form/", views.filter_shops_form),
    path("filter-shops", views.filter_shops),

    # Selling
  
    path("shops-for-selling/", views.shops_for_selling),
    path("shops-for-renting/", views.shops_for_renting),

    path("create-shop-for-selling-form/", views.create_shop_for_selling_form),
    path("create-shop-for-selling", views.create_shop_for_selling),
    
    path("update-shop-for-selling-form/<id>/", views.update_shop_for_selling_form),
    path("update-shop-for-selling/<id>", views.update_shop_for_selling),
    
    path("shop-for-selling-details/<id>/", views.shop_for_selling_details),
    path("change-shop-for-selling-state/<id>", views.change_shops_for_selling_state),
    path("delete-shop-for-selling/<id>/", views.delete_shop_for_selling),
    
    # Renting   
    
    path("shops-for-renting/", views.shops_for_renting),
    path("shops-for-renting/", views.shops_for_renting),

    path("create-shop-for-renting-form/", views.create_shop_for_renting_form),
    path("create-shop-for-renting", views.create_shop_for_renting),
    
    path("update-shop-for-renting-form/<id>/", views.update_shop_for_renting_form),
    path("update-shop-for-renting/<id>", views.update_shop_for_renting),
    
    path("shop-for-renting-details/<id>/", views.shop_for_renting_details),

    path("change-shop-for-renting-state/<id>", views.change_shops_for_renting_state),

    path("delete-shop-for-renting/<id>/", views.delete_shop_for_renting),
    
    
    ##
    # Lands
    ##
    path("filter-lands-form/", views.filter_lands_form),
    path("filter-lands", views.filter_lands),

    path("lands/", views.lands),

    path("create-land-form/", views.create_land_form),
    path("create-land", views.create_land),
    
    path("update-land-form/<id>/", views.update_land_form),
    path("update-land/<id>", views.update_land),
    
    path("land-details/<id>/", views.land_details),
    path("change-land-state/<id>", views.change_lands_state),
    path("delete-land/<id>/", views.delete_land),
    
    
]
