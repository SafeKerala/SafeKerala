from django.forms import ModelForm
from .models import *


class Logintableform(ModelForm):
    class Meta:
        model=Logintable
        fields=['username','password','usertype']
class policestationform(ModelForm):
    class Meta:
        model=Policestation
        fields=['policestationname','phonenumber','location','email']
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
        fields=['userid','username','feedback','date']
class notificationform(ModelForm):
    class Meta:
        Model=notification
        fields=['LOGIN_ID','username','notification','date'] 
class labourprofileform(ModelForm):
    class Meta:
        Model=labourprofile
        fields=['LOGIN_ID','phonenumber','skills','email'] 
class criminallistmanagementform(ModelForm):
    class Meta:
        Model=criminallistmanagement
        fields=['criminalname','criminalcase','location','status']
class requesttableform(ModelForm):
    class Meta:
        Model=requesttable
        fields=['LOGIN_ID','Labourid','Requeststatus','Requestdate']
class viewpolicestationform(ModelForm):
    class Meta:
        Model=viewpolicestation
        fields=['stationid','stationname','location','contact','email']
class viewworkrequestform(ModelForm):
    class Meta:
        Model=viewworkrequest
        fields=['LOGIN_ID','Phoneno','Description','Priority','Status']


               
