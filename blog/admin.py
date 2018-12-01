from django.contrib import admin
from .models import Agreement
from .models import Request
from .models import RegAgreement
from .models import RegRequest

admin.site.register(Agreement)
admin.site.register(Request)
admin.site.register(RegAgreement)
admin.site.register(RegRequest)
