from django.urls import path
from customer import views

urlpatterns = [
    path('home', views.CustomerIndex.as_view(), name='customerhome'),
    path('accounts/register', views.SignupView.as_view(), name='signup'),
    path('accounts/login', views.SigninView.as_view(), name='signin'),
    path('accounts/logout', views.signout, name='signout'),
    path('accounts/password/reset', views.PasswordRestView.as_view(), name='reset'),
    path('carts/items/add/<int:id>', views.add_to_cart, name="addtocart"),
    path('carts/all',views.View_my_Cart.as_view(),name = "viewsmycart")
]
