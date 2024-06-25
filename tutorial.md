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

9. Add Blog App definition on settings.py 
```bash
    INSTALLED_APPS = [
        ...,
        'blog',
    ]
```
<br>

10. Create general templates
```bash
    mkdir templates
    touch templates/base.html
```
📂 ./templates/base.html
```bash 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{% block title %}{% endblock %}</title>
        {% block css_file %}{% endblock %}
    </head>
    <body>
        {% block content %}
        {% endblock %}
    </body>
    </html>
```
<br>

11. Add BASE_DIR/templates at my_site settings.py
```bash
    TEMPLATES = [
        {
            ...,
            'DIRS': [
                BASE_DIR / "templates"
            ],
        },
    ]
```
<br>

12. Create index.html for Blog Template
```bash
    mkdir blog/templates
    mkdir blog/templates/blog
    touch blog/templates/blog/index.html
```
📂 ./blog/templates/blog/index.html
```bash
    {% extends "base.html" %}

    {% block title %}
        My Blog
    {% endblock %}

    {% block content %}
        <h1>Welcome to my blog</h1>
    {% endblock %}
```
<br>

13. Render index.html for blog starting_page

📂 ./blog/views.py
```bash
    def starting_page(request):
        return render(request, "blog/index.html")
```
<br>

14. Create content in index.html for blog starting_page
```bash
    // Do your own
```
<br>


15. Create global static folder and app.css
```bash
    mkdir static
    touch static/app.css
``` 
📂 ./static/app.css
```bash
    // Do your own css
```
<br>

16. Add STATICFILES_DIRS in settings.py
```bash
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        BASE_DIR / "static"
]
```
<br>

17. Load static css in base.html template
```bash
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        ...
        <link rel="stylesheet" href="{% static 'app.css' %}">
    </head> 
    </html>
```
<br>


18. Create blog static folder and index.css
```bash
    mkdir blog/static
    mkdir blog/static/blog
    touch blog/static/blog/index.css
```
📂 ./blog/static/blog/index.css
```bash
    // Do your own css
```
<br>

19. Load static css in blog index.html template
```bash
    {% extends "base.html" %}
    {% load static %}

    ...

    {% block css_file %}
        <link rel="stylesheet" href="{% static 'blog/index.css' %}">
    {% endblock %}

    ...
```
<br>

20. Create Page, Template and Static file with your own way