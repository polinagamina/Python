from django import forms
from .models import Agreement
from .models import Request
from .models import RegRequest
from .models import RegAgreement

class AgreementForm(forms.ModelForm):
    class Meta:
        model = Agreement
        fields = ('id', 'FIO', 'Service','Price','Kind','Type')
class Reply_registerForm(forms.ModelForm):
            class Meta:
                model = RegAgreement
                fields = ('id','created_date','FIO','OI','Kind','Type')

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('id', 'FIO', 'Service', 'Telephone', 'Email')



class RegRequestForm(forms.ModelForm):
    class Meta:
        model = RegRequest
        fields = ('id','created_date','FIO', 'Service','State')
