from django.forms import ModelForm
from .models import *


class Logintableform(ModelForm):
    class Meta:
        model=Logintable
        fields=['username','password','usertype']
class policestationform(ModelForm):
    class Meta:
        Model=Policestation
        fields=['LOGIN_ID','policestationname','phonenumber','location','email']
class userform(ModelForm):
    class Meta:
        Model=user
        fields=['LOGIN_ID','phonenumber','email']
class complaintsform(ModelForm):
    class Meta:
        Model=complaints
        fields=['userid','complaints','replycomplaints','complaintdate']  
class viewfeedbackform(ModelForm):
    class Meta:
        Model=viewfeedback
        fields=['userid','feedback']
class notificationform(ModelForm):
    class Meta:
        Model=notification
        fields=['LOGIN_ID','notification'] 
class labourprofileform(ModelForm):
    class Meta:
        Model=labourprofile
        fields=['LOGIN_ID','phonenumber','skills','email'] 
class criminallistmanagementform(ModelForm):
    class Meta:
        Model=criminallistmanagement
        fields=['criminalname','criminalcase']
class requesttableform(ModelForm):
    class Meta:
        Model=requesttable
        fields=['Userid','Labourid','Requeststatus','Requestdate']



               
