1. Setting Up the Starting Project
```bash
    django-admin startproject my_site
```
<br>

2. Create New App
```bash
    python3 manage.py startapp blog
```
<br>

3. Run Development Server
```bash
    python3 manage.py runserver
```
<br>

4. Create urls.py in blog folder
```bash
    touch blog/urls.py
```
<br>

5. Create some paths at urls.py in blog folder
```bash
    from django.urls import path
    from . import views

    urlpatterns = [
        path("", views.starting_page, name="starting-page"),
        path("posts", views.posts, name="posts-page"),
        path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
    ]
```
<br>

6. Create some views at views.py in blog folder
```bash
    from django.shortcuts import render

    # Create your views here.
    def starting_page(request):
        pass

    def posts(request):
        pass

    def post_detail(request):
        pass
```
<br>

7. Create some views at views.py in blog folder
```bash
    from django.shortcuts import render

    # Create your views here.
    def starting_page(request):
        pass

    def posts(request):
        pass

    def post_detail(request):
        pass
```
<br>

8. Wire up the blog URLs to the project-wide URLs
```bash
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('blog.urls')),
        
    ]
```
<br>