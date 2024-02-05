from django.urls import path
from . import views
from .views import HomeView, DolgozoView

urlpatterns = [
    path('login/', views.bejelentkezes, name ='login'),
    path('logout/', views.logout_page, name='logout'),
       
    path('dolgozo/', DolgozoView.as_view(), name= 'dolgozo'),
    
    path('',views.home, name = 'home'),
    #path('',HomeView.as_view(), name = 'home'),
    path('megrendelesek/', HomeView.as_view(), name= 'home'),
    #path('dolgozo/',views.dolgozo, name = 'dolgozo'),
    # path('bevitel/' ,views.bevitel, name='bevitel')
      

    path('raktar/' ,views.bevitel, name = "raktar"),
]   