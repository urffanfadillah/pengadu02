from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

LEVEL_CHOICES   = (
    ('masyarakat', 'masyarakat'),
    ('petugas', 'petugas'),
    ('admin', 'admin')
)
# Create your models here.
class User(AbstractUser):
    nik         = models.CharField(max_length=16, null=True)
    nama        = models.CharField(max_length=50, null=False)
    telp        = models.CharField(max_length=13, null=False) 
    level       = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='masyarakat')

    def __str__(self):
        return self.nama

class Pengaduan(models.Model):
    tgl_pengaduan       = models.DateTimeField(auto_now_add=True)
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    judul               = models.CharField(max_length=100, null=True)
    isi_laporan         = models.TextField(blank=False)
    foto                = models.ImageField(upload_to='image', blank=False)
    slug                = models.SlugField(blank=True, editable=False)
    status_pengaduan    = models.BooleanField(default=True)
    status_verifikasi   = models.BooleanField(default=False)
    status_selesai      = models.BooleanField(default=False)

    def save(self):
        self.slug       = slugify(self.judul)
        super(Pengaduan, self).save()

    def __str__(self):
        return self.judul

class Tanggapan(models.Model):
    pengaduan           = models.ForeignKey(Pengaduan, on_delete=models.CASCADE)
    tgl_tanggapan       = models.DateTimeField(auto_now_add=True)
    isi_tanggapan       = models.TextField(blank=False)
    user                = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return str(self.pengaduan)
        return "dari laporan aduan '{}' oleh {}".format(self.pengaduan, self.user)