from login import views
from django.urls import path, include


urlpatterns = [
    
    path('home/', views.HomePage, name='home'),
    path('table/',views.Table,name='table'),
    path('add/',views.ADD,name='add'),
    # path('edit',views.Edit,name='edit'),
    path('update/<str:id>/',views.Update,name='update'),
    path('delete/<str:id>/',views.Delete,name='delete'),
    path('',views.LoginPage,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('signup/',views.Signup,name='signup'),
    path('adminlogin/',views.AdminLogin,name='adminlogin'),
    path('adminlogout',views.AdminLogout,name='adminlogout'),
    path('search/',views.Search,name='search'),
    
]