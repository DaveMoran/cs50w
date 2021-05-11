from djange.urls import path

from . import views
urlpatterns = [
  path("", views.index, name="index")
]