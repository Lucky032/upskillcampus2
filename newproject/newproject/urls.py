from django.contrib import admin
from django.urls import path
from saverapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-password/', views.add_password, name='add_password'),
    path('retrieve_accounts/', views.retrieve_accounts, name='retrieve_accounts'),
    path('logout/', views.logout_user, name='logout'),  # Renamed view
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
