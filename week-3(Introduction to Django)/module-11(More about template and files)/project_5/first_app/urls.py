from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = 'home'),
    path('about/',views.about, name = 'about'), # when integer value is unknown
    # path('about/page/<int:id>/',views.about, name = 'about'),
]