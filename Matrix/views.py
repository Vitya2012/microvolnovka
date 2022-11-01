
from django.shortcuts import render
import numpy as np

# from Matrix.forms import divan
from Matrix.models import MatrixDB

from django.views import View

from django.shortcuts import redirect


def divan(permenaya = 1):
    return permenaya



def main(request):
    a = np.array([[54768,7966,234231],
    [54765875768,7978,236231]])
    form = divan()
    return render(request,'alsabt.html',{"alliymun":a,"form":form})



class Cbolxoubykvireview(View):
    def get(self,request):
        peremennaya = MatrixDB.objects.all()         
        form = divan()

        a = np.array([[54768,7966,234231],
        [54765875768,7978,236231]])

        return render(request,'alsabt.html',{"alliymun":a,"form":form})
            

    def post(self,request):
        form = divan(request.POST)
        # if form.is_valid():
            
        #     vesJSONnecovcemOtvet = form.cleaned_data
        #     m = vesJSONnecovcemOtvet.get("m") 
        #     m1 = vesJSONnecovcemOtvet.get("m1")
        #     m2 = vesJSONnecovcemOtvet.get("m2")
        #     m3 = vesJSONnecovcemOtvet.get("m3")
        #     m4 = vesJSONnecovcemOtvet.get("m4")
        #     m5 = vesJSONnecovcemOtvet.get("m5")


        #     MatrixDB.objects.create(m1=m1,m2=m2,m3=m3,m4=m4,m5=m5)
           


            
        #     print(vesJSONnecovcemOtvet)
           

        return redirect("cat")

# Create your views here.





































































class Jhgfdsa(View):
    def get(self,request):   
        form = divan()

        

        return render(request,'Idalgo7let.html',{"form":form})
            

    def post(self,request):
        form = divan(request.POST)
       
           

        return redirect("Idalgo7")


        