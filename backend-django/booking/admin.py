from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('nama_pemesan', 'lapangan', 'tanggal', 'jam_mulai', 'jam_selesai', 'created_at')
    search_fields = ('nama_pemesan', 'lapangan')
    list_filter = ('tanggal', 'lapangan')
