from django.urls import include, path

urlpatterns = [
    path('', include('api.foo.urls'))
]
