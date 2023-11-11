from django.contrib import admin
from .models import Movie, Booking

admin.site.site_header = "MovieGeek Booking Admin"
admin.site.site_title = "MovieGeek Booking Admin Area"
admin.site.index_title = "Welcome to the MovieGeek Booking admin area"

admin.site.register(Movie)
admin.site.register(Booking)

