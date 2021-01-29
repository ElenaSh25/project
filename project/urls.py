from django.urls import include, path


urlpatterns = [
    path('', include('homepage.urls')),
    path('user/', include('user.urls'))
    path('posts/', include('posts.urls'))
]