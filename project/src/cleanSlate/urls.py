"""cleanSlate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from joblist.views import jobs_list_view, current_job_view
from pages.views import home_view, contact_view, about_view, recents_view
from report.views import report_place
from signup.views import register_user
from login.views import user_login
from logout.views import logout_view
from account.views import account_summary_view


urlpatterns = [
    path('', home_view, name="home"),
    path('home/', home_view, name="home"),
    path('contact/', contact_view, name="contact"),
    path('about/', about_view, name="about"),
    path('jobs/', jobs_list_view, name="jobs"),
    path('current/', current_job_view, name="current"),
    path('report/', report_place, name="report"),
    path('login/', user_login, name="login"),
    path('logout/', logout_view, name="logout"),
    path('account/', account_summary_view, name="summary"),
    path('reg/', register_user, name="reg"),
    path('admin/', admin.site.urls),
    path('recents/', recents_view, name="recents"),
    path('', include('joblist.urls')),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

