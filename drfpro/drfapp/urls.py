from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'roleview', views.RsmRole,basename='roleview'),
router.register(r'userview', views.RsmUser,basename='userview'),

urlpatterns = [
    path('', include(router.urls)),

    #register/login/logout
    path('roleall/', views.Rolegetall.as_view(),name='roleall'),
    path('userall/', views.Usergetall.as_view(),name='userall'),
    path('rolecreate/', views.RoleCreate.as_view(),name='rolecreate'),
    path('usercreate/', views.UserCreate.as_view(),name='usercreate'),

    path('roleget/<int:pk>/', views.RoleGet.as_view() ,name='getr'),
    path('roleupdate/<int:pk>/', views.RoleUpdate.as_view() ,name='updater'),
    path('roledelete/<int:pk>/', views.RoleDelete.as_view() ,name='deleter'),

    path('userget/<int:pk>/', views.UserGet.as_view() ,name='getu'),
    path('userupdate/<int:pk>/', views.UserUpdate.as_view() ,name='updateu'),
    path('userdelete/<int:pk>/', views.UserDelete.as_view() ,name='deleteu'),

]
''' path('register/',views.RegisterUserApi.as_view(),name = 'register'),
    path('login/', views.LoginUserApi.as_view(), name='login'),
    path('logout/', views.LogoutUserApi.as_view(), name='logout'),
'''