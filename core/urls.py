from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/',view=views.cars_view,name="cars_list" ),
    path('new_car/',view=views.new_car_view,name="new_car" ),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
