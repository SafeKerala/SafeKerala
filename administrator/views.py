from django.shortcuts import redirect, render
from django.views import View
from .form import *

# Create your views here. 
class login(View):
    def get(self,request):
        return render(request,'login.html')
class admindashboard(View):
    def get(self,request):
        return render(request,'admin/admindashboard.html')
class viewcomplaints(View):
    def get(self,request):
        return render(request,'admin/viewcomplaints.html')
class viewlabours(View):
    def get(self,request):
        return render(request,'admin/viewlabours.html')
class viewpolicestation(View):
    def get(self,request):
        return render(request,'admin/viewpolicestation.html') 
class sendnotification(View):
    def get(self,request):
        return render(request,'admin/sendnotification.html') 
class viewfeedback(View):
    def get(self,request):
        return render(request,'admin/viewfeedback.html')
class replycomplaint(View):
    def get(self,request):
        return render(request,'admin/replycomplaint.html')
class viewcriminallist(View):
    def get(self,request):
        return render(request,'admin/viewcriminallist.html')        
class policestationdashboard(View):
    def get(self,request):
        return render(request,'policestation/policestationdashboard.html')
class addcriminals(View):
    def get(self,request):
        return render(request,'policestation/addcriminals.html')
class criminallistmanagement(View):
    def get(self,request):
        return render(request,'policestation/criminallistmanagement.html')
class editcriminals(View):
    def get(self,request):
        return render(request,'policestation/editcriminals.html')
class editlabours(View):
    def get(self,request):
        return render(request,'policestation/editlabours.html')
class viewnotification(View):
    def get(self,request):
        return render(request,'policestation/viewnotification.html')             
class sendsolution(View):
    def get(self,request):
        return render(request,'policestation/sendsolution.html')
class userdashboard(View):
    def get(self,request):
        return render(request,'user/userdashboard.html')        
class addcomplaint(View):
    def get(self,request):
        return render(request,'user/addcomplaint.html')  
    def post(self,request):
        form=complaintsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewcomplaints')    
class sendfeedback(View):
    def get(self,request):
        return render(request,'user/sendfeedback.html')        
class sendrequestforlabours(View):
    def get(self,request):
        return render(request,'user/sendrequestforlabours.html')                
class viewrequeststatus(View):
    def get(self,request):
        return render(request,'user/viewrequeststatus.html')
class labourdashboard(View):
    def get(self,request):
        return render(request,'labours/labourdashboard.html')      
class addandmanagepersonalissue(View):
    def get(self,request):
        return render(request,'labours/addandmanagepersonalissue.html') 
class addandmanageskills(View):
    def get(self,request):
        return render(request,'labours/addandmanageskills.html')  
class sendcomplaintsandviewreply(View):
    def get(self,request):
        return render(request,'labours/sendcomplaintsandviewreply.html')  
class updateworkrequeststatus(View):
    def get(self,request):
        return render(request,'labours/updateworkrequeststatus.html')
class viewfeedback(View):
    def get(self,request):
        return render(request,'labours/viewfeedback.html')
class viewworkrequest(View):
    def get(self,request):
        return render(request,'labours/viewworkrequest.html')










                                    

               

                

