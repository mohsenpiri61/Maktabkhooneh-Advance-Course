from django.urls import path, include


# app_name = "blog_app"

urlpatterns = [

    path("api/v1/", include("accounts.api.v1.urls")),
]