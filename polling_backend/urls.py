# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('polls/', include('polls.urls')),
# ]
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # add this

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),
    path("", lambda request: redirect("polls/")),  # redirect root to /polls/
]
