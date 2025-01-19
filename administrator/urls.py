
from django.urls import path
from .views import *

urlpatterns = [
    path('',login.as_view(),name='login'),
    path('addpolicestation',addpolicestation.as_view(),name='addpolicestation'),
    path('editpolicestation',editpolicestation.as_view(),name='editpolicestation'),
    path('admindashboard',admindashboard.as_view(),name='admindashboard'),
    path('viewcomplaints',viewcomplaints.as_view(),name='viewcomplaints'),
    path('viewlabours',viewlabours.as_view(),name='viewlabours'),
    path('policestation',policestation.as_view(),name='policestation'),
    path('sendnotification',sendnotification.as_view(),name='sendnotification'),
    path('viewfeedback',viewfeedback.as_view(),name='viewfeedback'),
    path('replycomplaint',replycomplaint.as_view(),name='replycomplaint'),
    path('viewcriminallist',viewcriminallist.as_view(),name='viewcriminallist'),
    path('policestationdashboard',policestationdashboard.as_view(),name='policestationdashboard'),
    path('addcriminals',addcriminals.as_view(),name='addcriminals'),
    path('criminallistmanagement',criminallistmanagement.as_view(),name='criminallistmanagement'),
    path('editcriminals',editcriminals.as_view(),name='editcriminals'),
    path('editlabours',editlabours.as_view(),name='editlabours'),
    path('addlabours',editlabours.as_view(),name='addlabours'),
    path('viewnotification',viewnotification.as_view(),name='viewnotification'),
    path('sendsolution',sendsolution.as_view(),name='sendsolution'),
    path('userdashboard',userdashboard.as_view(),name='userdashboard'),
    path('addcomplaint',addcomplaint.as_view(),name='addcomplaint'),
    path('sendfeedback',sendfeedback.as_view(),name='sendfeedback'),
    path('sendrequestforlabours',sendrequestforlabours.as_view(),name='sendrequestforlabours'),
    path('viewrequeststatus',viewrequeststatus.as_view(),name='viewrequeststatus'),
    path('labourdashboard',labourdashboard.as_view(),name='labourdashboard'),
    path('addandmanagepersonalissue',addandmanagepersonalissue.as_view(),name='addandmanagepersonalissue'),
    path('addandmanageskills',addandmanageskills.as_view(),name='addandmanageskills'),
    path('sendcomplaintsandviewreply',sendcomplaintsandviewreply.as_view(),name='sendcomplaintsandviewreply'),
    path('updateworkrequeststatus',updateworkrequeststatus.as_view(),name='updateworkrequeststatus'),
    path('viewfeedback',viewfeedback.as_view(),name='viewfeedback'),
    path('viewworkrequest',viewworkrequest.as_view(),name='viewworkrequest'),



    

]

