from django.urls import path
from . import views   

urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blospost-view-create"),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name="blogpost-retreive-update-delete    ")
]