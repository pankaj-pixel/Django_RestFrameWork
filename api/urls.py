from django.urls import path
from .views import BookView,BookViewDetails
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('api/v1',BookView.as_view(),name='BooksView'),
    path('api/v1/<int:pk>',BookViewDetails.as_view(),name='BooksView'),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    

]
