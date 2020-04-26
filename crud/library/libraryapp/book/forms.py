#Django makes it so much easier to make forms for models. We just need to use our models and we can easily make forms.

#Make a new file forms.py inbook directory. Paste this code in this forms.py.


from django import forms
from .models import book
#DataFlair
class bookCreate(forms.ModelForm):
    class Meta:
        model =book
        fields = '__all__'