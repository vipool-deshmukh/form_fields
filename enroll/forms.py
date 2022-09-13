from django import forms
from django.core import validators
class StudentRegistration(forms.Form):
    name=forms.CharField(min_length=5 ,max_length=5,strip=False)
    #name = forms.CharField(error_messages={'required':'Enter a your name'})
   # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])  built in valid..

    # name=forms.CharField() shows this field is required
    # name=forms.CharField(empty values="vipul')
    roll=forms.IntegerField(max_value=5,min_value=4)
    price = forms.IntegerField(max_value=5, min_value=4,max_digits=4,decimal=3)
    rate =forms.FloatField()
    #agree=forms.BooleanField(label_suffix=' ',label=' I agree')
#strip=for space
#requred=
#slug field=consist of letter,nos,hyphes or underscore


#Cleaning and Validating Specific Form Field in Django

'''class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    Password=forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        varname=self.cleaned_data['name']
        if len(varname)<5:
            raise forms.ValidationError("enter more than 4 char")
        return varname

super().clean()==to call super().clean() ensures that any validdation logic in parent class is maintained


#Validating Complete Django Form at Once in Django (Hindi)
class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()

    def clean(self):
        clean_data=super().clean()
        varname=self.cleaned_data['name']
        varemail = self.cleaned_data['email']
        if len(varname)<5:
            raise forms.ValidationError("enter name more than 5 char")


        if len(varemail)<10:
            raise forms.ValidationError("enter email more than 10 char")
'''

#built-in validators
#cutom validation

#from django import forms
#from django.core import validators

#def startwith_s(value):
 #   if value[0]!='s':
  #      raise forms.ValidationError('name should start with s'

#class StudentRegistration(forms.Form):
 #   name=forms.CharField(validators= [startwith_s])
  #  email=forms.EmailField()






#Match Password and Re Enter Password Field in Django

#from django import forms
#from django.core import validators
#class StudentRegistration(forms.Form):
 #   name=forms.CharField()
  #  email=forms.EmailField()
  #  Password=forms.CharField(widget=forms.PasswordInput)
#    rPassword = forms.CharField(label=Password(Again),    widget=forms.PasswordInput)


#def clean(self):
 ##   clean_data = super().clean()
   # valpwd=self.cleaned_data['password']
    #valrpwd=self.cleaned_data['rpassword']
    #if valpwd!=valrpwd:
     #   raise forms.ValidationError('pass not match')






#Styling Django Form Errors and Field Error in Django

#from django import forms
#from django.core import validators
#class StudentRegistration(forms.Form):
 #   name=forms.CharField(error_messages={'required':'Enter a your name'})
  #  email=forms.EmailField(error_messages={'required':'Enter a your email'})
  #  Password=forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Enter a your email})



#style in the html file

