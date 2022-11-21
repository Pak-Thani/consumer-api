from django.contrib import admin
import csv
from django.http import HttpResponse
# from csvexport.actions import csvexport

from .models import Transaction

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields
            if field.name not in ['nomorWhatsapp', 'detailAlamat']    
        ]
        queryset = queryset.prefetch_related('transactionproduct_set')


        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names + ['product_slug', 'quantity'])
        for rule in queryset:
            for prod in rule.transactionproduct_set.all():
                row = [getattr(rule, field) for field in field_names]
                row.append(prod.product_slug)
                row.append(prod.quantity)
                writer.writerow(row)
            
        return response

    export_as_csv.short_description = "Export Selected"
class TransactionAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('created', 'namaPembeli', 'status', 'pembayaran')
    actions = ["export_as_csv"]  

    def has_add_permission(self, request, obj=None):
        return False     
    
admin.site.register(Transaction, TransactionAdmin)
