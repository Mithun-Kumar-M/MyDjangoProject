from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calc.urls')),  # ✅ Correct usage with string
    path('',include('data.urls'))
]
