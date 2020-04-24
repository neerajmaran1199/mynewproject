from django.urls import path

from .views import ( HomePage,
                    Page,
                    PostCreateView,
                    PostListView, 
                    PostDetailView,
                    PostDeleteView,
                    PostUpdateView,

                    )
                    

urlpatterns = [
    path('secont/' , HomePage, name="home-page"),
    path('page/' , Page, name="page"),
    path('', PostListView.as_view(), name='home_page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk/', PostDeleteView.as_view(), name='post_create'),
    path('post/new/', PostUpdateView.as_view(), name='post_create'),
    ]
