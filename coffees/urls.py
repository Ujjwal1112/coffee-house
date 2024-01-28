from django.urls import path
import coffees.views as views

urlpatterns = [
    path("coffee_detail/<int:coffee_id>", views.coffee_detail, name="coffee_detail"),
    path("cart", views.shopping_cart, name="cart"),
    path("add_to_cart/<int:coffee_id>", views.add_to_cart, name="add_to_cart")
    ]

