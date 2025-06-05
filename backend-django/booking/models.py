from django.db import models

class Booking(models.Model):
    nama_pemesan = models.CharField(max_length=100)
    lapangan = models.CharField(max_length=50)
    tanggal = models.DateField()
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama_pemesan} - {self.lapangan} ({self.tanggal})"

    class Meta:
        verbose_name_plural = "Booking"