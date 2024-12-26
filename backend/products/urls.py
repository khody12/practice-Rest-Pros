from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductMixinView.as_view()),
    path("<int:pk>/update/", views.ProductUpdateAPIView.as_view()), # detail api view allows us to edit an obj
    path("<int:pk>/delete/", views.ProductDestroyAPIView.as_view()), 
    path("<int:pk>/", views.ProductMixinView.as_view())
]