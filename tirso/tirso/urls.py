
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from etat_stock import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view(redirect_authenticated_user=True),name='login'),
    path('logout', LogoutView.as_view(),name='logout'),
    path('',views.stock,name="files_index"),
    path('files_index',views.stock,name="files_index"),
    path('master_data',views.master_data,name="master_data"),
    path('upload_file',views.upload_file,name="upload_file"),
    path('check/<int:id>', views.check_file,name="check_file"),
    path('delete/<int:id>', views.delete_file,name="delete_file"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)