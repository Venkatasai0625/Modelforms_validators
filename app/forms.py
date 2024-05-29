
from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'
        
    def clean(self):
        t=self.cleaned_data['topic_name']
        if t[-1]=="z":
            raise forms.ValidationError("Ended with z")
    # def clean_topic_name(self):
    #     cut=self.cleaned_data
class WebpageForm(forms.ModelForm):
    mobile=forms.CharField(max_length=10,min_length=10,validators=[RegexValidator('[6-9]\d{9}')])
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)
    class Meta:
        model=Webpage
        fields='__all__'
        
    def clean_botcatcher(self):
        cb=self.cleaned_data['botcatcher']
        if len(cb)>0:
            raise forms.ValidationError("Invalid Bot data")
        
class AccessRecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'
        
        