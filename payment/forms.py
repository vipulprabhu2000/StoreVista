from .models import ShippingAddress
from django import forms



class Shippingform(forms.ModelForm):
    Shipping_full_name=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full name'}),required=True)
    Shipping_email=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email '}),required=True)
    Shipping_address1=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'address1'}),required=True)
    Shipping_address2=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'address2'}),required=True)
    Shipping_state=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'state'}),required=False)
    Shipping_country=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'country'}),required=True)
    Shipping_zipcode=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'zipcode'}),required=True)

    class Meta:
        model=ShippingAddress
        fields=["Shipping_full_name","Shipping_email","Shipping_address1","Shipping_address2","Shipping_state","Shipping_country","Shipping_zipcode"]
        exclude=['user',]



class Payment_form(forms.Form):
    card_name=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Card name'}),required=True)
    card_number=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Card Number'}),required=True)
    card_exp_date=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Card Expiry Date'}),required=True)
    card_cvv=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Card CVV'}),required=True)
    card_address1=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Card Address1'}),required=True)
    card_address2=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Card Address 2'}),required=False)
    card_city=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Card City'}),required=True)
    card_state=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Card state'}),required=True)
    card_zipcode=forms.CharField(label=" ",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Card zipcode'}),required=True)