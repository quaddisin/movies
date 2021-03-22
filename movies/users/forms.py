from django import forms

class RegisterForm(forms.Form):

    username = forms.CharField(label="Username",max_length=50)
    password = forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput)
    confirm = forms.CharField(label="Confirm Password",max_length=50,widget=forms.PasswordInput)
    
    def clean(self):

        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if username and password and confirm and password != confirm:

            raise forms.ValidationError("Error")
        else:

            values = {
                "username":username,
                "password":password,
            }

            return values

class LoginForm(forms.Form):

    username = forms.CharField(label="Username",max_length=50)
    password = forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput)