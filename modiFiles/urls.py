from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *

# admin.site.site_header = "My_Home Admin"
# admin.site.site_title = "My_Home Admin"
# admin.site.index_title = "Welcome To My_Home Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('', include('csv_all.urls')),
    path('', include('pdf_all.urls')),
    path('', include('xls_all.urls')),

    # path('privacy', privacy, name='privacy'),
    # path('page401', page401, name='page401'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 401 Unauthorized
# 403 Forbidden
# 404 Not Found
# 415 Unsupported Media Type
# 500 Internal Server Error
# 501 Not Implemented
# 502 Bad Gateway
