from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import SignUpForm, AjukanPengaduanForm, TanggapanForm
from .models import Pengaduan, Tanggapan

def signup(request):
    if request.method == 'POST':
        form    = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username        = form.cleaned_data.get('username')
            raw_password    = form.cleaned_data.get('password1')
            user            = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form    = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def ajukan_pengaduan(request):
    form        = AjukanPengaduanForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance        = form.save(commit=False)
        instance.user   = request.user
        instance.save()
        return redirect('home')
    template    = 'ajukan_pengaduan.html'
    context     = {
        'form':form
    }
    return render(request, template, context)

def detail(request, slugInput):
    qs_model            = get_object_or_404(Pengaduan, slug=slugInput)
    tanggapan           = qs_model.tanggapan_set.all()
    template            = 'detail.html'
    form_tanggapan      = TanggapanForm(request.POST or None)
    if form_tanggapan.is_valid():
        instance                    = form_tanggapan.save(commit=False)
        instance.user               = request.user
        instance.pengaduan          = qs_model
        qs_model.status_verifikasi  = True
        qs_model.status_pengaduan   = False
        qs_model.save()
        instance.save()
        return redirect('core:detail', slugInput=qs_model.slug)
    context             = {
        'obj':qs_model,
        'form':form_tanggapan,
        'tanggapans':tanggapan
    }
    return render(request, template, context)

def proses_selesai(request, proses_id):
    qs_model                    = Pengaduan.objects.get(id=proses_id)
    qs_model.status_verifikasi  = False
    qs_model.status_selesai     = True
    qs_model.save()
    return redirect('home')