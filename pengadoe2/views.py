from django.shortcuts import render

from core.models import Pengaduan

def home(request):
    template    = 'home.html'
    context     = {
        'pengaduans':Pengaduan.objects.filter(status_pengaduan=True),
        'pengaduan_saya':Pengaduan.objects.filter(user=request.user),
        'pengaduan_terverifikasi':Pengaduan.objects.filter(status_verifikasi=True),
        'pengaduan_proses_selesai':Pengaduan.objects.filter(status_selesai=True).order_by('-tgl_pengaduan')
    }
    return render(request, template, context)