from django.urls import path
from amanda_testerman_profile.views import HomeView

urlpatterns = [
    
    path("", HomeView.as_view(), name='home' ),

]