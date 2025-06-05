from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'nama_pemesan', 'lapangan', 'tanggal', 'jam_mulai', 'jam_selesai']