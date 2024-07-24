from django.urls import path
from . import views

urlpatterns = [
    path("", views.overview_msg, name='land'),
    path("/grp", views.grp, name='grp'),
    path("/theme", views.theme, name='theme')
]