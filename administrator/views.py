from django.shortcuts import redirect, render
from django.views import View
from .form import *
from django.http import HttpResponse

# Create your views here. 
class login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        login_obj= Logintable.objects.get(username=username,password=password)
        if login_obj.usertype == "admin":
            return HttpResponse('''<script>alert("welcome to adminhome");window.location="admindashboard"</script>''')
        
class addpolicestation(View):
    def get(self,request):
        return render(request,'admin/addpolicestation.html')
    def post(self,request):
        form=policestationform(request.POST)
        if form.is_valid():
            login_instance=Logintable.objects.create(
            usertype='policestation',
            username=request.POST['username'],
            password=request.POST['password'],
        )
        reg_form=form.save(commit=False)
        reg_form.LOGIN_ID =login_instance
        reg_form.save()
        return HttpResponse('''<script>alert("Registered successfully!");window.location="/"</script>''')      
        
class editpolicestation(View):
    def get(self,request):
        return render(request,'editpolicestation.html')
class admindashboard(View):
    def get(self,request):
        return render(request,'admin/admindashboard.html')
class viewcomplaints(View):
    def get(self,request):
        c=complaints.objects.all()
        return render(request,'admin/viewcomplaints.html',{'c':c})
class viewlabours(View):
    def get(self,request):
        m=labourprofile.objects.all()
        return render(request,'admin/viewlabours.html',{'m':m})
class policestation(View):
    def get(self,request):
        o=viewpolicestation.objects.all()
        return render(request,'admin/viewpolicestation.html',{'o':o})
class sendnotification(View):
    def get(self,request):
        return render(request,'admin/sendnotification.html')
class viewfeedback(View):
    def get(self,request):
        f=viewfeedback.objects.all()
        return render(request,'admin/viewfeedback.html',{'f':f})
class replycomplaint(View):
    def get(self,request):
        return render(request,'admin/replycomplaint.html')
class viewcriminallist(View):
    def get(self,request):
        h=viewcriminallist.objects.all()
        return render(request,'admin/viewcriminallist.html')        
class policestationdashboard(View):
    def get(self,request):
        return render(request,'policestation/policestationdashboard.html')
class addcriminals(View):
    def get(self,request):
        return render(request,'policestation/addcriminals.html')
class criminallistmanagement(View):
    def get(self,request):
        h=viewfeedback.objects.all()
        return render(request,'policestation/criminallistmanagement.html',{'h':h})
class editcriminals(View):
    def get(self,request):
        return render(request,'policestation/editcriminals.html')
class editlabours(View):
    def get(self,request):
        return render(request,'policestation/editlabours.html')
class addlabours(View):
    def get(self,request):
        return render(request,'policestation/addlabours.html')
class viewnotification(View):
    def get(self,request):
        g=viewfeedback.objects.all()
        return render(request,'policestation/viewnotification.html',{'g':g})             
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
        n=viewfeedback.objects.all()
        return render(request,'labours/viewworkrequest.html',{'n':n})










                                    

               

                

