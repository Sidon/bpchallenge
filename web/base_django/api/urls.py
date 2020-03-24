from django.urls import path, include

app_name = 'graphql'

urlpatterns = (
    path('', include('rest_framework.urls')),
)
