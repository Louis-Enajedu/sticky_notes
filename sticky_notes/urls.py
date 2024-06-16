from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),  # Including the URLs from the posts app
    path('', include('notes.urls')),  # Including the URLs from the notes app, assuming you have a notes app as well
]
