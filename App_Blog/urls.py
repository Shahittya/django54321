from django.urls import path
from App_Blog import views
app_name='App_Blog'
urlpatterns=[
path('',views.BlogList.as_view(),name='blog_list'),
path('write/',views.CreateBlog.as_view(),name='create_blog'),
path('details/<int:id>/',views.blog_details,name='blog_details'),
path('liked/<int:id>/',views.liked,name='liked_post'),
path('unliked/<int:id>/',views.unliked,name='unliked_post'),
path('my_blog/',views.MyBlog.as_view(),name='my_blog'),
path('edit/<pk>/',views.UpdateBlog.as_view(),name='edit_blog'),
path('delete/<pk>/',views.DeleteBlog.as_view(),name='delete_blog'),

]
