from django.urls import path
from .views import Login_View, Signup_View, Profile_View, Home_View, Update_View, Delete_View, UserLogout
# from tasks import views

urlpatterns = [
    path('', Home_View),

    path('login/', Login_View, name = 'userlogin'),
    path('signup/', Signup_View, name='usersignup'),
    path('profile/', Profile_View, name = 'userprofile'),
    path('<int:id>/', Update_View, name = 'userupdate'),
    path('del/<int:id>/', Delete_View, name = 'userdelete'),
    path('logout/', UserLogout, name= 'logout')
]