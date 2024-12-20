from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars import views
from accounts.views import register_view,login_view,logout_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/',view=views.cars_view,name="cars_list" ),
    path('new_car/',view=views.new_car_view,name="new_car" ),
    path('register/',view=register_view,name="register" ),
    path('login/',view=login_view,name="login" ),
    path('logout/',view=logout_view,name="logout" ),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
