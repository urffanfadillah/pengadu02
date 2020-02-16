from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import Pengaduan, Tanggapan

User    = get_user_model()

class SignUpForm(UserCreationForm):
    nama        = forms.CharField(max_length=50, required=True)
    nik         = forms.CharField(max_length=16, required=True)
    telp        = forms.CharField(max_length=13, required=True) 
    class Meta:
        model   = User
        fields  = ('username', 'nama', 'nik', 'telp', 'password1', 'password2')

class AjukanPengaduanForm(forms.ModelForm):
    class Meta:
        model       = Pengaduan
        fields      = ('judul', 'isi_laporan', 'foto')

class TanggapanForm(forms.ModelForm):
    class Meta:
        model       = Tanggapan
        fields      = ('isi_tanggapan',)