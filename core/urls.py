from django.urls import path

from .views import ajukan_pengaduan, detail, proses_selesai

app_name        ='core'
urlpatterns     = [
    path('ajukan-pengaduan', ajukan_pengaduan, name='ajukan-pengaduan'),
    path('laporan/<slugInput>', detail, name='detail'),
    path('selesai/<proses_id>', proses_selesai, name='proses-selesai')
]