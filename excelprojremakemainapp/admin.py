from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Client)
admin.site.register(EmailOTP)
admin.site.register(Payment_id)
admin.site.register(Withdrawal_request)
admin.site.register(Transaction)
admin.site.register(Bonus)
admin.site.register(Minimum_withdrawal)
admin.site.register(Maximum_withdrawal)
admin.site.register(Video)
admin.site.register(Notification)
admin.site.register(Plan)
admin.site.register(Package)
admin.site.register(Wire_transfer_request)
admin.site.register(Cash_mailing_address)
