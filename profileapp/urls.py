from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    #라우트하는 과정+primary key를 적어줘야함
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
]

