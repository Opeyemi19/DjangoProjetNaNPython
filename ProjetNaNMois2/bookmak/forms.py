from django import forms

from bookmak.models import PariSport


class PariForm(forms.ModelForm):
    model = PariSport
    class Meta:
        fields = ('cagnote','coteEquip1','miseEquip1','coteEquip2','miseEquip2')
        
    def clean(self):
        if self.is_valid():
            cagnote = self.cleaned_data['cagnote']
            coteEquip1 = self.cleaned_data['coteEquip1']
            miseEquip1 = self.cleaned_data['miseEquip1']
            coteEquip2 = self.cleaned_data['coteEquip2']
            miseEquip2 = self.cleaned_data['miseEquip2']

   
    def calcul_gain1(self):
        cagnote = self.cleaned_data['cagnote']
        coteEquip1 = self.cleaned_data['coteEquip1']
        miseEquip1 = self.cleaned_data['miseEquip1']
        coteEquip2 = self.cleaned_data['coteEquip2']
        miseEquip2 = self.cleaned_data['miseEquip2']
        
        gainEquip1 = (coteEquip1*miseEquip1)
        beneficeEquip1 = (gainEquip1 - cagnote)
        gainEquip2 = (coteEquip2*miseEquip2)
        beneficeEquip2 = (gainEquip2 - cagnote)
















			
    

        
    
        
