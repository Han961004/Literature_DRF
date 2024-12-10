from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings  

import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('v1.accounts.urls')),
    path('', include('v1.posts.urls')),
]

if settings.DEBUG:
    '''
    로컬 환경 디버그용 
    '''
    urlpatterns += [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
