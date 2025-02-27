"""
URL configuration for kochiusedbikes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.RegistrationView.as_view(),name='signup'),
    path('',views.SignInView.as_view(),name="signin"),
    path('index/',views.IndexView.as_view(),name="index"),
    path('bike/<int:pk>/detail/',views.BikesDetailView.as_view(),name="detail"),
    path('bike/<int:pk>/add_to_wishlist',views.AddToWishlistView.as_view(),name="add-to-wishlist"),
    path('bike/wishlist/',views.WishlistListView.as_view(),name="wishlist"),
    path('bike/wishlist/remove/<int:pk>',views.RemoveWishlistItems.as_view(),name="wishlist-remove"),
    path('bike/book/',views.SlotBooking.as_view(),name="book")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





