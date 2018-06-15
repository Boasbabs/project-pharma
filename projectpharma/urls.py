"""projectpharma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from frontend.views import landing, retailer, wholesaler

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("frontend.urls", namespace="frontend")),
    path("drugs/", include("drugs.urls", namespace="drugs")),
    path("shopping_cart/", include("shopping_cart.urls", namespace="shopping_cart")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', landing.SignUpView.as_view(), name='user_signup'),
    path('accounts/signup/retailer/', retailer.RetailerSignUpView.as_view(), name='retailer_signup'),
    path('accounts/signup/wholesaler/', wholesaler.WholesalerSignUpView.as_view(), name='wholesaler_signup'),

]


# TODO
"""
1. authentication and authorization
2. retailer app
3. supplier app
4. product app
5. cart
6. order app *(maybe)
"""