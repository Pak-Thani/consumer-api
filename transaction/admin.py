from django.contrib import admin

from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('created', 'status', 'pembayaran')

admin.site.register(Transaction, TransactionAdmin)
