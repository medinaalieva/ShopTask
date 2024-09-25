from django.urls import path
from .views import  CategoryListView, CategoryRetrieve, CategoryCreate, CategoryDelete,CategoryPatch


urlpatterns = [
    path('list/', CategoryListView.as_view()),
    path('retrieve/<int:pk>', CategoryRetrieve.as_view()),
    path('create/', CategoryCreate.as_view()),
    path('delete/<int:pk>/', CategoryDelete.as_view()),
    path('update/<int:pk>/',CategoryPatch.as_view())
]