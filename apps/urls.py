from django.urls import include, path


urlpatterns = [
    path('', include("apps.codeAnalyzer.urls")),
    path('pentest-api/', include("apps.pentest.urls")),
]