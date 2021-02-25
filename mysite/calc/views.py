from django.shortcuts import render
from django.http import HttpResponse
#from . models import QuestionDet
import jinja2
from jinja2 import Template
import os
import string
from django.db import models
from . models import *
from itertools import islice 
from tex import latex2pdf
import os  
import os
import pdflatex
import subprocess
from django.db.models import F
import time
from datetime import datetime
from django.core.files import File
from subprocess import call
import shutil, os
from django.core.files.base import ContentFile
import os
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import login




from django.http import JsonResponse
from datetime import date

# Create your views here.

def home(request):
    return render(request,'myfp.html')


from django.shortcuts import render
from django.http import HttpResponse
#from . models import QuestionDet
from django.contrib import admin
from django.core.management import call_command
from django.db import models
from mysite import settings
#from . models import Department
def home(request):


    return render(request,'SYSTEMPAGE.html')


def TeacherLoginLP(request):
    print("Inside teacher login here")
    return render(request,"TeacherLogForm.html")

def HODLoginLP(request):
    print("inside hod login")
    return render(request,"HodLogForm.html")



def DeanLoginLP(request):
    return render(request,"AdminLogForm.html")

def RAdminHomePage(request):
   

    if request.GET["username"]=='sysadmin' and request.GET["pass"]=='syspass':
        return render(request,'sysadmindb.html',{'Eusername':"SYSADMIN"})                                            # ADMIN LOGIN AND VERIFICATION

    return HttpResponse("Wrong USERNAME and PASSWORD")

def CreateDep(request):
   

    return render(request,'EnterDepInfo.html',{'Eusername':"SYSADMIN" })                                               # RENDER CREATE DEPARTMENT PAGE 


def UpdateDep(request):

    return HttpResponse("DONE")
    

def DeleteDep(request):
    return HttpResponse("DONE")

def InsertDepInfo(request):


    
    if Department.objects.filter(Dept_id=request.POST["did"]).exists():
        return HttpResponse("<h2>THIS DEPARTMENT ID ALREADY EXISTS PLEASE TRY A UNIQUE ONE<h2>")

    if Department.objects.filter(Dept_name=request.POST["dname"]).exists():
        return HttpResponse("<h2>THIS DEPARTMENT NAME ALREADY EXISTS PLEASE TRY A UNIQUE ONE<h2>")

    if Department.objects.filter(Dept_code=request.POST["dcode"]).exists():
        return HttpResponse("<h2>THIS DEPARTMENT CODE ALREADY EXISTS PLEASE TRY A UNIQUE ONE<h2>")

    if Teachers.objects.filter(Teach_id =request.POST["dhid"]).exists():
        return HttpResponse("<h2>The Teacher ID already exists<h2>")


                
                
    obj=Department()
    obj.Dept_id=request.POST["did"]
    obj.Dept_name=request.POST["dname"]
    obj.Dept_code=request.POST["dcode"]
    #obj.Dept_huname=request.POST["hname"]
    #obj.Dept_passkey=request.POST["passk"]
    obj.save()
    print("dep created")

    obj2=Teachers()
    obj2.Teach_name=request.POST["hodname"]
    obj2.Teach_uname=request.POST["hname"]
    obj2.Teach_id=request.POST["dhid"]
    obj2.Teach_pass=request.POST["passk"]
    obj2.Dept_id=request.POST["did"]
    obj2.Rights="HOD"

    obj2.save()

    
    obj3=Depart_Teach()

    obj3.Teach_id=request.POST["dhid"]
    obj3.Dept_id=request.POST["did"]
    



    return HttpResponse("<h2>Department Created<h2>")

def InsertCourse(request):
    if Courses.objects.filter(Course_code=request.POST["tid"]).exists():
        return HttpResponse("<h2>This Course code  already exists<h2>")

    
    
                
        
    obj=Courses()
    obj.Course_code=request.POST["tid"]
    #obj.Course_type=request.POST["G"]
    obj.Course_name=request.POST["tname"]
    #obj.Course_exam=request.POST["CourseE"]
    #obj.Course_marks=request.POST["marks"]  
    obj.Dept_id=  request.session["Dept_id"]
    
    obj.save()

    return HttpResponse("Course Created")


def InsertTeacher(request):

    if Teachers.objects.filter(Teach_id =request.POST["tid"]).exists():
        return HttpResponse("<h2>The Teacher ID already exists<h2>")
    if Teachers.objects.filter(Teach_uname =request.POST["uname"]).exists():
        return HttpResponse("<h2>This username already exists<h2>")    
        
    obj=Teachers()
    obj.Teach_id =request.POST["tid"]
    obj.Teach_name =request.POST["tname"]
    obj.Teach_uname =request.POST["uname"]
    obj.Teach_pass =request.POST["tpass"]
    obj.Dept_id=request.session["Dept_id"]
    obj.save()

    obj2=Depart_Teach()
    obj2.Dept_id=request.session["Dept_id"]
    obj2.Teach_id=request.POST["tid"]
    

    obj2.save()

    return HttpResponse("all done")



def AddmcqQues(request):
    
    obj=Quest_BankMCQ()
    print("The length of files are *********",request.FILES)
    if len(request.FILES) == 0:
        obj.Course_code=request.session["Course_code"]
        obj.Qtext=request.POST["qt"]
        obj.choice_1=request.POST["opt1"]
        obj.choice_2=request.POST["opt2"]
        obj.choice_3=request.POST["opt3"]
        obj.choice_4=request.POST["opt4"]
        obj.unit_num=request.POST["un"]
        obj.BloomL=request.POST["BL"]
    
        obj.Co=request.POST["CO"]
        obj.max_marks=request.POST["MXM"]
        obj.min_marks=request.POST["MIM"]
        obj.remarks=request.POST["rem"]
        obj.RefCount=0
        if request.session["Role"]=="CC":
            obj.State="V"
        elif request.session["Role"]=="CT": 
            obj.State="NV"    
        obj.save()
    else:
        obj.Course_code=request.session["Course_code"]
        obj.Qtext=request.POST["qt"]
        obj.choice_1=request.POST["opt1"]
        obj.choice_2=request.POST["opt2"]
        obj.choice_3=request.POST["opt3"]
        obj.choice_4=request.POST["opt4"]
        obj.unit_num=request.POST["un"]
        obj.BloomL=request.POST["BL"]
        obj.image=request.FILES['image']
        obj.RefCount=0
        obj.Co=request.POST["CO"]
        obj.max_marks=request.POST["MXM"]
        obj.min_marks=request.POST["MIM"]
        obj.remarks=request.POST["rem"]
        if request.session["Role"]=="CC":
            obj.State="V"
        elif request.session["Role"]=="CT": 
            obj.State="NV"    
        obj.save()
        
        print("Inside insert MCQ***********")
        print(obj)
        print("Inside InsertMCQ********")



    return HttpResponse("<h1>question inserted successfully <h1>")

    
   



def AddTheoryQues(request):
    
    obj= Quest_BankTHR()
    print("The length of files are ",len(request.FILES))

    if len(request.FILES) == 0:
        print(request,request.POST)
        obj.Course_code=request.session["Course_code"]
        obj.Qtext=request.POST["qt"]
        print(request,request.POST)
        obj.BloomL=request.POST["BL"]
        #obj.image=request.FILES['image']

    
    
        obj.RefCount=0
        obj.Co=request.POST["CO"]
        obj.unit_num=request.POST["un"]
        obj.max_marks=request.POST["MXM"]
        obj.min_marks=request.POST["MIM"]
        obj.remarks=request.POST["rem"]
        if request.session["Role"]=="CC":
            obj.State="V"
        elif request.session["Role"]=="CT": 
            obj.State="NV"    

        obj.save()
    else :
        obj.Course_code=request.session["Course_code"]
        obj.Qtext=request.POST["qt"]
        obj.BloomL=request.POST["BL"]
        obj.image=request.FILES['image']

    
    
        obj.RefCount=0
        obj.Co=request.POST["CO"]
        obj.unit_num=request.POST["un"]
        obj.max_marks=request.POST["MXM"]
        obj.min_marks=request.POST["MIM"]
        obj.remarks=request.POST["rem"]
        if request.session["Role"]=="CC":
            obj.State="V"
        elif request.session["Role"]=="CT": 
            obj.State="NV"    

        obj.save()

    return HttpResponse("<h1>question inserted successfully.<h1>")


def RHodHomePage(request):
    print("Insert")
    if Department.objects.filter(Dept_huname=request.POST['username'],Dept_passkey=request.POST['pass']).exists():
    
        Dep_details=Department.objects.filter(Dept_huname=request.POST['username'],Dept_passkey=request.POST['pass']).values()
       # print(Dep_details)
        request.session["Dept_id"]=Dep_details[0]['Dept_id']
        request.session["Dept_code"]=Dep_details[0]['Dept_code']
        request.session["Dept_huname"]=Dep_details[0]['Dept_huname']
        request.session["Dept_name"]=Dep_details[0]['Dept_name']

        request.session["USERNAME"]=request.POST['username']


        print(request.session["USERNAME"],"dsadasdsa")
        #print("asdasads")
 
        vars=request.session["USERNAME"]
        #print(vars,"dsdssdd2")
        
       
        return render(request,'HODDB.html',{'Hod_uname':Dep_details[0]['Dept_huname'],'d_name':Dep_details[0]['Dept_name'],'d_code':Dep_details[0]['Dept_code'],'Eusername':request.session["USERNAME"] })
    return HttpResponse("<h2>Failed Login<h2>")   

def RinsertCourse(request):
    print(request.session["USERNAME"])

    return render(request,'InsertCourse.html',{'Eusername':request.session["USERNAME"]})     

def RinsertTeacher(request):

    return render(request,'InsertTeacher.html',{'Eusername':request.session["USERNAME"]})   

def RmapTc(request):
    
    Course_list=Courses.objects.filter(Dept_id=request.session["Dept_id"])
    Teacher_list=Teachers.objects.filter(Dept_id=request.session["Dept_id"])
   

    return render(request,'Map_CT.html',{'Course_list':Course_list,'Teacher_list':Teacher_list,'Eusername':request.session["USERNAME"]})   

def InsertMapTc(request):
    values=(request.POST["tname"]).split("#")
    if Teach_Course_MR.objects.filter(Course_code=request.POST["Ccode"],Teach_id=values[1],Rights=request.POST["role"]).exists():
        return HttpResponse("This Course to Teacher Mapping Already Exists")
    obj=Teach_Course_MR()
    obj.Course_code=request.POST["Ccode"]
    obj.Course_name=Courses.objects.filter(Course_code=request.POST["Ccode"]).values()[0]["Course_name"]

    
    
    obj.Teach_uname=values[0]
    obj.Teach_id=values[1]
    obj.Dept_id=request.session["Dept_id"]
    obj.Rights=request.POST["role"]

    obj.save()

    return HttpResponse("<h2>inserted<h2>")  

def RThomePage(request):
    '''
    if Teachers.objects.filter(Teach_uname=request.POST["username"] , Teach_pass=request.POST["pass"],Rights='adm').exists():
        request.session["USERNAME"]=request.POST["username"]
        return render(request,'sysadmindb.html',{'Eusername':request.session["USERNAME"]})

    '''
    
    if request.POST["username"]=='iamadmin' and request.POST["pass"]=='adminpass':
        
        return render(request,'sysadmindb.html',{'Eusername':"SYSADMIN"})

    if Teachers.objects.filter(Teach_uname=request.POST["username"] , Teach_pass=request.POST["pass"] , Rights='HOD').exists():
        #if Department.objects.filter(Dept_huname=request.POST['username'],Dept_passkey=request.POST['pass']).exists():
            Dep_details=Teachers.objects.filter(Teach_uname=request.POST['username'],Teach_pass=request.POST['pass']).values()

            print(Dep_details)
            request.session["Dept_id"]=Dep_details[0]['Dept_id']
            Dep_details_2=Department.objects.filter(Dept_id=Dep_details[0]['Dept_id']).values()
            request.session["Dept_code"]=Dep_details_2[0]['Dept_code']
            request.session["Dept_huname"]=Dep_details[0]['Teach_uname']
            request.session["Dept_name"]=Dep_details_2[0]['Dept_name']
            request.session["tuname1"]=request.POST["username"]

            print(request.session["tuname1"])
            
            request.session["USERNAME"]=request.POST["username"]
        

            return render(request,'HODDB.html',{'Hod_uname':Dep_details[0]['Teach_uname'],'d_name':Dep_details_2[0]['Dept_name'],'d_code':Dep_details_2[0]['Dept_code'],'Eusername':request.session["USERNAME"]})


        
    if Teachers.objects.filter(Teach_uname=request.POST["username"], Teach_pass=request.POST["pass"]).exists():
        teach_info=Teachers.objects.filter(Teach_uname=request.POST["username"], Teach_pass=request.POST["pass"]).values()
        deptId=teach_info[0]["Dept_id"]
        print(deptId)
        Dep_details=Department.objects.filter(Dept_id=deptId).values()
        tid=teach_info[0]["Teach_id"]
        request.session["Dept_id"]=Dep_details[0]['Dept_id']
        Dep_details_2=Department.objects.filter(Dept_id=Dep_details[0]['Dept_id']).values()
        request.session["Dept_code"]=Dep_details_2[0]['Dept_code']
        request.session["Dept_huname"]=teach_info[0]['Teach_uname']
        request.session["Dept_name"]=Dep_details_2[0]['Dept_name']
        request.session["USERNAME"]=request.POST["username"]

        if Teach_Course_MR.objects.filter(Dept_id=Dep_details[0]['Dept_id'],Teach_uname=request.POST["username"]).exists():
            course_ass_list=Teach_Course_MR.objects.filter(Dept_id=Dep_details[0]['Dept_id'],Teach_uname=request.POST["username"]).values()
            #print(course_ass_list,len(course_ass_list))
            print(len(course_ass_list),"is the length")
            if len(course_ass_list)==1:
                print("inside")
                course_code=course_ass_list[0]['Course_code']
                print("inside2")
                role=course_ass_list[0]['Rights']
                course_det=Courses.objects.filter( Course_code= course_code).values()
                request.session["Course_name"]=course_det[0]["Course_name"]
                request.session["Course_code"]=course_det[0]["Course_code"]
                #request.session["Course_type"]=course_det[0]["Course_type"]
                #request.session["Course_exam"]=course_det[0]["Course_exam"]
                #request.session["Course_marks"]=course_det[0]["Course_marks"]
                request.session["Role"]=role
                print("The course code is ", request.session["Course_code"],request.session["Role"])
                  





                if(role=="CC"):
                    return render(request,'CC_DS.html',{"Course_name":request.session["Course_name"],"Course_marks":request.session["Course_marks"],"Course_exam":request.session["Course_type"],'Eusername':request.session["USERNAME"]})

            


                elif(role=="CT"):
                    return render(request,'CT_DS.html',{"Course_name":request.session["Course_name"],"Course_marks":request.session["Course_marks"],"Course_exam":request.session["Course_type"],'Eusername':request.session["USERNAME"]})


            elif len(course_ass_list)>1:
                print("Inside greater than 2")
          
                   
                print(request.session["USERNAME"])
                return render(request,'MapMultiple.html',{'courses':course_ass_list,'teausername':request.POST["username"],'Eusername':request.session["USERNAME"]})





                

            else :
                return HttpResponse("Yet to be done")


        else:
           return HttpResponse("<h1>You are yet to be assigned an Course<h1>")    




    else :
        return HttpResponse("<h2>Invalid Login page<h2>")    

def RChooseQuest(request):

    return render(request,'ChooseQtype.html')

def ChooseTheory(request):
#    Unitd=Course_units.objects.filter(Course_code=request.session["Course_code"]).values()
#    Co=Course_outcome.objects.filter(Course_code=request.session["Course_code"]).values()
    
#    return render(request,'AddMcQQuest.html',{'Unitd':Unitd,'Co':Co,'Eusername':request.session["USERNAME"]})

    Unitd=Course_units.objects.filter(Course_code=request.session["Course_code"]).values()
    Co=Course_outcome.objects.filter(Course_code=request.session["Course_code"]).values()
    
    return render(request,'AddTheoryQuest.html',{'Unitd':Unitd,'Co':Co,'Eusername':request.session["USERNAME"]})  

def ChooseMcq(request):

#    Unitd=Course_units.objects.filter(Course_code=request.session["Course_code"]).values()
#    Co=Course_outcome.objects.filter(Course_code=request.session["Course_code"]).values()
    
#    return render(request,'AddTheoryQuest.html',{'Unitd':Unitd,'Co':Co,'Eusername':request.session["USERNAME"]})

    Unitd=Course_units.objects.filter(Course_code=request.session["Course_code"]).values()
    Co=Course_outcome.objects.filter(Course_code=request.session["Course_code"]).values()
    
    return render(request,'AddMcQQuest.html',{'Unitd':Unitd,'Co':Co,'Eusername':request.session["USERNAME"]})  
def RCreatePaper(request):

    Unitd=Course_units.objects.filter(Course_code=request.session["Course_code"]).values()
    Co=Course_outcome.objects.filter(Course_code=request.session["Course_code"]).values()
    print(Co)
    listud=[]
    listco=[]
    for i in Unitd:
        listud.append(int(i['Unit_num']))
    #print(listud)
   

    for i in Co:
        listco.append(int(i['Outcome_no']))

    #print(listco)
    #test_list = [int(i) for i in test_list]
    print(listud)
    print(listco)
    
  
    
    request.session["UDArray"]=listud
    request.session["COArray"]=listco
    return render(request,'UpdateQpTemplate.html',{'Eusername':request.session["USERNAME"]})  

def GetTemplateDetails(request):
   
    mcq_ques=Quest_BankMCQ.objects.filter(Course_code=request.session["Course_code"],State='V')
    thr_ques=Quest_BankTHR.objects.filter(Course_code=request.session["Course_code"],State='V')

    thrqnums= request.session["TQnums"]
    mcqnums=request.session["MQnums"]
    print(request.session['totalsub'])
    #request.session['totalm']=totalm
    #request.session['compulsoryQ']=Compulsory
    #request.session['totalsub']=subqc

    #request.session["UDArray"]=listud
    #request.session["COArray"]=listco
    varl=request.session["examSEM"].split("#")
    ExamSem=varl[0]+" "+varl[1]
    return render(request,'DisplayQuestNew.html',{'UDArray1':request.session["UDArray"],'ExamSem':ExamSem ,'COArray1':request.session["COArray"],'exam_name': request.session["examt"],'mcq_ques':mcq_ques,'thr_ques':thr_ques,'course_name':request.session["Course_name"],'Qnums':request.session["Qnums"],'total_quest':len(request.session["Qnums"]),'Exam_marks':request.session["examMxM"],'Eusername':request.session["USERNAME"],"Quesnos":request.session["Qnums"],"thrqnums": thrqnums,"mcqnums":mcqnums,'SubQR':request.session['totalsub'],'CompQ':request.session['compulsoryQ'],'MarksT':request.session["totalm"]})





def MapMults(request):
    course_details=request.POST["select_course"]
    course_code=course_details.split("#")[0]
    course_rights=course_details.split("#")[1]
    if(course_rights=='CC'):
        request.session["Role"]="CC"
    if(course_rights=='CT'):
        request.session["Role"]="CT"    

    course_det=Courses.objects.filter( Course_code= course_code).values()  # Gets the course CODE
    request.session["Course_name"]=course_det[0]["Course_name"]
    request.session["Course_code"]=course_det[0]["Course_code"]
    #request.session["Course_type"]=course_det[0]["Course_type"]
    #request.session["Course_exam"]=course_det[0]["Course_exam"]
    #request.session["Course_marks"]=course_det[0]["Course_marks"]

    if(course_rights=="CC"):
        return render(request,'CC_DS.html',{"Course_name":request.session["Course_name"],'Eusername':request.session["USERNAME"]})

            


    elif(course_rights=="CT"):
        return render(request,'CT_DS.html',{"Course_name":request.session["Course_name"],"Course_marks":request.session["Course_marks"],"Course_exam":request.session["Course_type"],'Eusername':request.session["USERNAME"]})


def RAddCo(request):
    Co=Course_outcome.objects.filter(Course_code=request.session["Course_code"]).values()
    print(Co)

    return render(request,'AddCopage.html',{'CO_DET':Co,'Course_name':request.session["Course_name"],'Eusername':request.session["USERNAME"]})

def RAddUD(request):
    Ud=Course_units.objects.filter(Course_code=request.session["Course_code"]).values()
    return render(request,'AddUDpage.html',{'Unit_det':Ud,'Course_name':request.session["Course_name"],'Eusername':request.session["USERNAME"]})

def AddCo(request):
    if Course_outcome.objects.filter(Course_code=request.session["Course_code"],Outcome_no=int(request.POST["NO"])).exists():
        return HttpResponse("The Outcome Number for this Course Already exists")
    obj=Course_outcome()
    obj.Course_code=request.session["Course_code"]
    obj.Outcome_no=int(request.POST["NO"])
    obj.Outcome_Text=request.POST["OD"]
    print(obj.Outcome_Text,"This is the text")

    obj.save()
    return redirect('RAddCo')
    return HttpResponse("<h2>Successfully Inserted<h2>")



def AddUd(request):
    if Course_units.objects.filter(Course_code=request.session["Course_code"],Unit_num=int(request.POST["nu"])).exists():
        return HttpResponse("The UNIT Number for this Course  Already exists")
    obj=Course_units()
    obj.Course_code=request.session["Course_code"]
    obj.Unit_num=int(request.POST["nu"])
    obj.Unit_name=request.POST["uname"]
    obj.Unit_Details=request.POST["udet"]
    obj.Unit_marks=int(request.POST["marks"])
    obj.save()
    return redirect('RAddUD')
    return HttpResponse("<h2>Successfully Inserted<h2>")

def AnalyzeCQ(request):

    
    print("HEyyyyyyyyyyy")
    mcq_ques=Quest_BankMCQ.objects.filter(Course_code=request.session['Course_code'],State='NV').values()
    thr_ques=Quest_BankTHR.objects.filter(Course_code=request.session['Course_code'],State='NV').values()
    return render(request,'AnalyzeQuestCC.html',{'course_name':request.session['Course_name'],'mcq_ques':mcq_ques,'thr_ques':thr_ques,'Eusername':request.session["USERNAME"]})    

def VerQuests(request):
    
    print("Inside Verify Questions")
    mcqidl=request.POST.getlist('mcqid[]')
    thridl=request.POST.getlist('thrid[]')
    print(mcqidl)
    print(thridl)
    for i in mcqidl:
        Quest_BankMCQ.objects.filter(id=i).update(State='V')

    for j in thridl:
        Quest_BankTHR.objects.filter(id=j).update(State='V') 

    print()
    print("Outside verify Questions")
    return JsonResponse({
                'success': True,
                
            })            

def DelQuest(request):
    
    mcqidl=request.POST.getlist('mcqid[]')
    thridl=request.POST.getlist('thrid[]')
    
    for i in mcqidl:
        Quest_BankMCQ.objects.filter(id=i).delete()

    for j in thridl:
        Quest_BankTHR.objects.filter(id=j).delete()

    return JsonResponse({
                'success': True,
                
            })  

def convert(lst, var_lst): 
    it = iter(lst) 
    return [list(islice(it, i)) for i in var_lst]         

def AddTemplQuest(request):
    print("Inside here")
    
    
   
    subqc=request.POST.getlist('SubQC[]')
    
    Compulsory=request.POST.getlist('CompC[]')

    totalm=request.POST.getlist('totalm[]')

    request.session['totalm']=totalm
    request.session['compulsoryQ']=Compulsory
    request.session['totalsub']=subqc
   

    print("These are compulsory",str(Compulsory))
    


    subsr=[]
    print("The value of subqc is",subqc)
    mcqsubq=[]
    thrsubq=[]

    d = dict(enumerate(string.ascii_uppercase, 1))
    for i in range(0,int(subqc[0])):
        mcqsubq.append("1."+d[i+1])

       
    print(mcqsubq)
    for i in range(1,len(subqc)):
        for j in range(int(subqc[i])):
            thrsubq.append(str(i+1)+"."+d[j+1])  

    Qnums=mcqsubq+thrsubq
    request.session["TQnums"]=thrsubq
    request.session["MQnums"]=mcqsubq

    print("The value of QNUS+MS IS ********",Qnums)

    
       

   # print(Qnums)     

    request.session["Qnums"]=Qnums   
    request.session["subqsr"]=subsr
    #request.session["totatlsub"]=subqc

    print("The value of Qunums is *******",request.session["Qnums"])
    print("********************TOTAL SUBQUESTIONS******************",request.session["totalsub"])
    return JsonResponse({
                'success': True,
                
            })        



    
    

def HodSelCourse(request):
    print("tHE DETails are",request.session["Dept_id"],request.session["tuname1"])
    if Teach_Course_MR.objects.filter(Dept_id=request.session["Dept_id"],Teach_uname=request.session["tuname1"]).exists():
            course_ass_list=Teach_Course_MR.objects.filter(Dept_id=request.session["Dept_id"],Teach_uname=request.session["tuname1"]).values()
            #print(course_ass_list,len(course_ass_list))
            print(len(course_ass_list),"is the length")
            if len(course_ass_list)==1:
                print("inside")
                course_code=course_ass_list[0]['Course_code']
                print("inside2")
                role=course_ass_list[0]['Rights']
                course_det=Courses.objects.filter( Course_code= course_code).values()
                request.session["Course_name"]=course_det[0]["Course_name"]
                request.session["Course_code"]=course_det[0]["Course_code"]
               
             
                request.session["Role"]=role
                print("The course code is ", request.session["Course_code"],request.session["Role"])
                  





                if(role=="CC"):
                    return render(request,'CC_DS.html',{"Course_name":request.session["Course_name"],'Eusername':request.session["USERNAME"]})

            


                elif(role=="CT"):
                    return render(request,'CT_DS.html',{"Course_name":request.session["Course_name"],'Eusername':request.session["USERNAME"]})


            elif len(course_ass_list)>1:
                print("Inside greater than 2")
          
                   

                return render(request,'MapMultiple.html',{'courses':course_ass_list,'teausername':request.session["tuname1"],'Eusername':request.session["USERNAME"]})






                

            else :
                return HttpResponse("Yet to be done")

    return HttpResponse("<h2>No Course assigned to you YET<h2>")
    

def NewTempl1(request):


    request.session["examt"]=request.POST["examtype"]
    request.session["examMxM"]=request.POST["marks"]
    request.session["IFMCQ"]=request.POST["papertype"]
    request.session["examSEM"]=request.POST["examSEM"]

    if(request.session["IFMCQ"]=="MCQ"):
    
        return render(request,'UpdateQpsectempl.html',{'Eusername':request.session["USERNAME"],'maxm':request.session["examMxM"]})
    
    elif (request.session["IFMCQ"]=="NOMCQ"):
        return render(request,'UpdateQpsectemplNOmcq.html',{'Eusername':request.session["USERNAME"],'maxm':request.session["examMxM"]})

    else :
        return HttpResponse("PLEASE SELECT the mcq or no mcq")
    

    




def genLatex(request):
    #mcq_ques=Quest_BankMCQ.objects.filter(Course_code=request.session["Course_code"])
    #thr_ques=Quest_BankTHR.objects.filter(Course_code=request.session["Course_code"])

    IDmcq=request.POST.getlist('idM[]')
    IDthr=request.POST.getlist('idT[]')
    Qtmcq=request.POST.getlist('QtextM[]')
    Qthr=request.POST.getlist('QtextT[]')
    Cot=request.POST.getlist('COT[]')
    Com=request.POST.getlist('COM[]')
    Blt=request.POST.getlist('BLT[]')
    Blm=request.POST.getlist('BLM[]')
    UnT=request.POST.getlist('UnumT[]')
    Unm=request.POST.getlist('UnumM[]')
    SelT=request.POST.getlist('SelT[]')
    SelM=request.POST.getlist('SelM[]')
    chch1=request.POST.getlist('chch1[]')
    chch2=request.POST.getlist('chch2[]')
    chch3=request.POST.getlist('chch3[]')
    chch4=request.POST.getlist('chch4[]')
    ImageFieldT=[]
    ImageFieldM=[]
    BImageFieldT=[]
    BImageFieldM=[]
    print("The total marks are ",request.session["totalm"])
    print("SelT is ",SelT)
    print("SelM is check it..",SelM)
    

    for i in IDthr:
        temp1=(Quest_BankTHR.objects.filter(Course_code=request.session["Course_code"],id=i).values())
        print(temp1)
        temp=temp1[0]["image"]
        if(len(temp)>1):
            ImageFieldT.append(temp)
            BImageFieldT.append(True)
        else:
            ImageFieldT.append('')
            BImageFieldT.append(False)

        
        #print(Quest_BankTHR.objects.filter(Course_code=request.session["Course_code"],id=i).values())
    
    for j in IDmcq:
        temp1=(Quest_BankMCQ.objects.filter(Course_code=request.session["Course_code"],id=j).values())
        temp=temp1[0]["image"]
        if(len(temp)>1):
            ImageFieldM.append(temp)
            BImageFieldM.append(True)
        else:
            ImageFieldM.append('')
            BImageFieldM.append(False)

    
    print(ImageFieldT,BImageFieldT,ImageFieldM,BImageFieldM) 
    print(request.session["totalsub"])
    print(IDmcq,IDthr)
    print(Qtmcq,Qthr) 
    nlistOfmcq=[]
    for i in range(0,len(Qtmcq)):
        tmp_list=[]
        tmp_list.append(chch1[i])
        tmp_list.append(chch2[i])
        tmp_list.append(chch3[i])
        tmp_list.append(chch4[i])

        nlistOfmcq.append(tmp_list)

    print(nlistOfmcq)   
    print(request.session['Qnums'])

    print(request.session["TQnums"])
    print(request.session["MQnums"])
    subqc= request.session["totalsub"]
    subqci = [int(numeric_string) for numeric_string in subqc]
    print(subqci)
    print(subqci[1:])

    Qthr2= convert(Qthr,subqci[1:])
    Cot2=convert(Cot,subqci[1:])
    Blt2=convert(Blt,subqci[1:])
    Selt2=convert(SelT,subqci[1:])
    Qthrarry=convert(request.session["TQnums"],subqci[1:])
    print("The converted array is ",Qthrarry)


           
    examType=request.session["examt"]
          

     

    print("The value of selected theory marks is is ",Selt2)
    print("The selM is---------",SelM)
    print("The SelT2 is........",SelT)
    print("The first subqc",subqc[1:])
    latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.')))
    print("The first subqc",subqc[1:])
    template = latex_jinja_env.get_template('WithMCQ.tex')
    template_vars  = {}
    template_vars['subt']=request.session["Course_name"]+" ("+request.session["Course_code"]+")"
    template_vars['maxm']= request.session["examMxM"]
    template_vars['mcQuest']=len(Qtmcq)
    template_vars['compulsorym']= request.session['compulsoryQ'][0]
    template_vars['firstqmax']=request.session['totalm'][0]
    template_vars['Subq']=subqc[0]
    template_vars['mcQuestArr']=request.session["MQnums"]
    print(template_vars['mcQuestArr'])
    template_vars['questMCq']=Qtmcq
    template_vars['mcqoptsL']=len(nlistOfmcq)
    template_vars['mcqList']=nlistOfmcq
    print(template_vars['mcqList'])
    template_vars['bloomM']=Blm
    template_vars['coM']=Com
    template_vars['selM']=SelM
    template_vars['thrQuestArr']=Qthrarry
    template_vars['questTHr']=Qthr2
    template_vars['bloomT']=Blt2
    template_vars['coT']=Cot2
    template_vars['selT']=Selt2
    template_vars['thrQuest']=len(Qthr2)
    template_vars['compthr']=request.session['compulsoryQ']
    #ImageFieldT,BImageFieldT,ImageFieldM,BImageFieldM
    template_vars['ImageFieldM']=ImageFieldM
    template_vars['BImageFieldM']=BImageFieldM
    subqci = [int(numeric_string) for numeric_string in subqc]
    template_vars['BImageFieldT']=convert(BImageFieldT,subqci)
    template_vars['ImageFieldT']=convert(ImageFieldT,subqci)
    template_vars["mxm"]=(request.session["totalm"])[1:]
    #template_vars["mcqnum"]=request.session["mcqnum"]
    subqci = [int(numeric_string) for numeric_string in subqc]

    template_vars['subthr']=subqci[1:]

    print("The first subqc",subqci[1:])
    '''
    ExamI= request.session["Course_exam"]
    if(ExamI[4]=='1' or  ExamI[4]=='2'):
        template_vars["exam"]="First Year BTech"
    if(ExamI[4]=='3' or  ExamI[4]=='4'):
        template_vars["exam"]="Second Year BTech"
    if(ExamI[4]=='5' or  ExamI[4]=='6'):
        template_vars["exam"]="Third Year BTech"        
    if(ExamI[4]=='7' or  ExamI[4]=='8'):
        template_vars["exam"]="Fourth Year BTech"
    '''
    print("The exam is ",request.session["examt"])    
    examType=request.session["examt"]
    template_vars["ExamType"]=request.session["examt"]
    SemInfo=request.session["examSEM"].split("#")

    template_vars["exam"]=SemInfo[0]
    semnum=SemInfo[1]
  
    file_name=template_vars['subt']+template_vars["exam"]+request.session["examt"]+" "+semnum+" "+(str(time.time()))[-1]
    texfname=file_name+".tex"
    pdfname=file_name+".pdf"
  
  
    output_file = open(texfname, 'w')
   

    output_file.write( template.render( template_vars ) )
    
    
    output_file.close()
    call(['pdflatex', texfname])

    thres=dict(zip(IDthr, Qthr)) 
    thmcq=dict(zip(IDmcq,Qtmcq))
    
    '''
    for i in IDmcq:
        Quest_BankMCQ.objects.filter(id=i).update(RefCount=F('RefCount')+1)
        obj=Mcq_instance()
        obj.Question_id=i
        obj.Text=thmcq[i]
        obj.Exam_record=template_vars['subt']+" "+template_vars["exam"]+" "+request.session["examt"]
        obj.Exam_date=str(date.today())
        obj.Course_code=request.session["Course_code"]
        obj.save()


    for j in IDthr:  
        Quest_BankTHR.objects.filter(id=j).update(RefCount=F('RefCount')+1)
        obj= Theory_instance()
        obj.Question_id=j
        obj.Text=thres[j]
        obj.Exam_record=template_vars['subt']+" "+template_vars["exam"]+" "+request.session["examt"]
        obj.Exam_date=str(date.today())
        obj.Course_code=request.session["Course_code"]
        obj.save()
  
    '''
    request.session["IDTHR"]=" ".join(str(x) for x in IDthr)
    request.session["IDMCQ"]=" ".join(str(x) for x in IDmcq)

    request.session["CreatedFileName"]=pdfname
    


    return JsonResponse({
                'success': True,
                
            })          


def genLatexNoMcq(request):
   
    IDthr=request.POST.getlist('idT[]')
  
    Qthr=request.POST.getlist('QtextT[]')
    Cot=request.POST.getlist('COT[]')
  
    Blt=request.POST.getlist('BLT[]')
  
    UnT=request.POST.getlist('UnumT[]')

    SelT=request.POST.getlist('SetThr[]')
    '''
    Qthr=[]
    k=Quest_BankTHR.objects.filter(id=int("11")).values()
    print(type(k[0]["Qtext"]))
    for i in IDthr:
       var=Quest_BankTHR.objects.filter(id=int(i)).values()[0]
       Qthr.append(str([var["Qtext"]]))
    '''
    print(request.session["totalsub"])
    subqc=request.session["totalsub"]
    ImageFieldT=[]
   
    BImageFieldT=[]
    
    print("Were INSIDE")
    for i in IDthr:
        temp1=(Quest_BankTHR.objects.filter(Course_code=request.session["Course_code"],id=i).values())
        print(temp1)
        temp=temp1[0]["image"]
        if(len(temp)>1):
            ImageFieldT.append(temp)
            BImageFieldT.append(True)
        else:
            ImageFieldT.append('')
            BImageFieldT.append(False)

    latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))) 

    template = latex_jinja_env.get_template('NOMCQtempPr2.tex')

    template_vars  = {}
    template_vars['subt']=request.session["Course_name"]+" ("+request.session["Course_code"]+")"
    template_vars['maxm']= request.session["examMxM"]
    subqci = [int(numeric_string) for numeric_string in subqc]
    template_vars['BImageFieldT']=convert(BImageFieldT,subqci)
    template_vars['ImageFieldT']=convert(ImageFieldT,subqci)

    print(convert(Cot,subqci))
    print(convert(Blt,subqci))
    print(convert(SelT,subqci))
   # print("The selected marks are ",selT)

    template_vars["QT"]=convert(Qthr,subqci)
    template_vars["CoT"]=convert(Cot,subqci)
    template_vars["Blt"]=convert(Blt,subqci)
    template_vars["UnT"]=convert(UnT,subqci)
    template_vars["SelT"]=convert(SelT,subqci)
    template_vars["Qnos"]=convert(request.session["thrsubq"],subqci)
    template_vars["Comp"]=request.session["comp"]
    template_vars["subq"]=subqci
    template_vars["mxm"]=request.session["totalm"]
    
    print(len(subqc))
    template_vars["mainQuest"]=len(subqci)
    #print(request.session["totalsub"])
   # print(request.session["thrsubq"])
    #print(request.session["comp"])
    #print(request.session["totalm"])

    print(template_vars['BImageFieldT'])
    print(template_vars['ImageFieldT'])

    examType=request.session["examt"]
    print("The exam is ",request.session["examt"])  
    template_vars["ExamType"]=request.session["examt"]

 
    print("exam t IS ------",examType)
    '''
    ExamI= request.session["Course_exam"]
    if(ExamI[4]=='1' or  ExamI[4]=='2'):
        template_vars["exam"]="First Year BTech"
    if(ExamI[4]=='3' or  ExamI[4]=='4'):
        template_vars["exam"]="Second Year BTech"
    if(ExamI[4]=='5' or  ExamI[4]=='6'):
        template_vars["exam"]="Third Year BTech"        
    if(ExamI[4]=='7' or  ExamI[4]=='8'):
        template_vars["exam"]="Fourth Year BTech"
    '''
    SemInfo=request.session["examSEM"].split("#")
   # print(SemInfo)
    template_vars["exam"]=SemInfo[0]

    semnum=SemInfo[1]
    file_name=template_vars['subt']+template_vars["exam"]+request.session["examt"]+" "+semnum+" "+(str(time.time()))[-1]
    texfname=file_name+".tex"
    pdfname=file_name+".pdf"
    output_file = open(texfname, 'w')

   
    request.session["IDTHR"]=" ".join(str(x) for x in IDthr)
    request.session["IDMCQ"]="empty"
    
   

    output_file.write( template.render( template_vars ) )
    
    print("The textfname is ###################",texfname)
    print(output_file)
    
    output_file.close()
    call(['pdflatex', texfname])

    thres = dict(zip(IDthr, Qthr)) 

    

    '''

    for j in IDthr:  
        Quest_BankTHR.objects.filter(id=j).update(RefCount=F('RefCount')+1)
        obj= Theory_instance()
        obj.Question_id=j
        obj.Text=thres[j]
        obj.Exam_record=template_vars['subt']+" "+template_vars["exam"]+" "+request.session["examt"]
        obj.Exam_date= str(date.today())
        obj.Course_code=request.session["Course_code"]
        obj.save()

    '''      
    request.session["CreatedFileName"]=pdfname

    
  
    
    return JsonResponse({
                'success': True,
                
            })          

def AddTemplQuestNoMCQ(request) :
    print("Inside here")
    
    print("Inside the template 1")
   
    subqc=request.POST.getlist('SubQC[]')
    
    Compulsory=request.POST.getlist('CompC[]')

    totalm=request.POST.getlist('totalm[]')

    print("The subquestion array is ",subqc)
    print("The compulsory question array is ",Compulsory)
    print("The totalmarks area is ",totalm)

    thrsubq=[]
    print("Inside the template 2")

    d = dict(enumerate(string.ascii_uppercase, 1))

    for i in range(0,len(subqc)):
        for j in range(int(subqc[i])):
            thrsubq.append(str(i+1)+"."+d[j+1])  

    print(thrsubq)        

    request.session["comp"]=Compulsory
    request.session["totalm"]=totalm
    request.session["thrsubq"]=thrsubq 
    #request.session["subqsr"]=subsr
    request.session["totalsub"]=subqc

    print("********************TOTAL SUBQUESTIONS******************",request.session["totalsub"])
    print("Inside the template 2")
    return JsonResponse({
                'success': True,
                
            })        

def NoMcqTemplateDetails(request):
    mcq_ques=Quest_BankMCQ.objects.filter(Course_code=request.session["Course_code"],State='V')
    thr_ques=Quest_BankTHR.objects.filter(Course_code=request.session["Course_code"],State='V')

    print(request.session["totalsub"])
    print(request.session["thrsubq"])
    print(request.session["comp"])
    print(request.session["totalm"])
    varl=request.session["examSEM"].split("#")
    ExamSem=varl[0]+" "+varl[1]

    return render(request,'DisplayQuestNewNoMCQ.html',{'UDArray1':request.session["UDArray"],'COArray1':request.session["COArray"],'thr_ques':thr_ques,'course_name':request.session["Course_name"],'Qnums':request.session["thrsubq"],'total_quest':len(request.session["thrsubq"]),'exam_name': request.session["examt"],'Exam_marks':  request.session["examMxM"],"Quesnos":request.session["thrsubq"],'Eusername':request.session["USERNAME"],'SubQR':request.session["totalsub"],'CompQ':request.session["comp"],'ExamSem':ExamSem ,'MarksT':request.session["totalm"]})





def Logout(request):

    logout(request)
    request.session.flush()
    #return redirect('HODLoginLP')
  
  
    return render(request,'TeacherLogafterLO.html')


def Dep_det_all(request):

    return render(request,'Dept_det_1.html',{'Eusername':request.session["USERNAME"]})

def Delete_questions(request):
    mcq_ques=Quest_BankMCQ.objects.filter(Course_code=request.session['Course_code']).values()
    thr_ques=Quest_BankTHR.objects.filter(Course_code=request.session['Course_code']).values()
    return render(request,'DeleteQuestCC.html',{'course_name':request.session['Course_name'],'mcq_ques':mcq_ques,'thr_ques':thr_ques,'Eusername':request.session["USERNAME"]}) 
    #return render(request,'DeleteQuestCC.html',{'Eusername':request.session["USERNAME"]})

def Staffdetails(request):
    
    StaffDet=Teachers.objects.filter(Dept_id=request.session["Dept_id"]).values()

    return render(request,'StaffDetails.html',{'StaffDet':StaffDet,'Eusername':request.session["USERNAME"]})

def CourseMapdet(request):

    TeachMR=Teach_Course_MR.objects.filter(Dept_id=request.session["Dept_id"]).values()
    return render(request,'CourseMapDetails.html',{'TeachMR':TeachMR,'Eusername':request.session["USERNAME"]})


def Done_paper(request):
    
    print("The session object is ",request.session["CreatedFileName"])
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    shutil.copy(request.session["CreatedFileName"], os.path.join(BASE_DIR,'QuestionPapers'))

    obj=GeneratedQpRec()

    obj.File_name=request.session["CreatedFileName"]
    #obj.File_loc=os.path.join(BASE_DIR,'QuestionPapers')
   # obj.File_loc=BASE_DIR+"/QuestionPapers/"+request.session["CreatedFileName"]
    obj.File_author=request.session["USERNAME"]
    obj.Dept_id=request.session["Dept_id"]
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    obj.Creation_Date=  dt_string
    obj.mcqArray=request.session["IDMCQ"]
    obj.thrArray=request.session["IDTHR"]
    obj.verify="NO"
    obj.Exam_type=request.session["examt"]
    obj.save()
    #request.session["IDTHR"]=" ".join(str(x) for x in IDthr)
    #request.session["IDMCQ"]="empty"
      
    with open(os.path.join(BASE_DIR,request.session["CreatedFileName"] ), 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/pdf")
        response['Content-Disposition'] = 'attachment; filename='+request.session["CreatedFileName"]

       
        return response
    
    
    return HttpResponse("Done with the paper")


def Done_Ver(request):
    return redirect('AnalyzeCQ')
    return HttpResponse("Questions have been verified")


def Staffdetails(request):

    staffd=Teachers.objects.filter(Dept_id=request.session["Dept_id"]).values()
    return render(request,'StaffDetails.html',{'StaffDet':staffd,'Eusername':request.session["USERNAME"]})

def CourseMapdet(request):

    coursemapd=Teach_Course_MR.objects.filter(Dept_id=request.session["Dept_id"]).values()
    print(coursemapd)
    return render(request,'CourseMapDetails.html',{'TeachMR':coursemapd,'Eusername':request.session["USERNAME"]})

                                                      
def DoneDeleting(request):

    return redirect('Delete_questions')
    return HttpResponse("Successfully Deleted")
                      
def Downloadpdfsys(request):

    Downloadpdf=GeneratedQpRec.objects.filter(verify="NO").values()
    Downloadpdf2=GeneratedQpRec.objects.filter(verify="YES").values()
    print(Downloadpdf)
    print("Insid Donload")
    return render(request,'Syspdfdownload.html',{'DownloadTable':Downloadpdf,'DownloadTable2': Downloadpdf2})

def Hodownloadpdf(request):

    Downloadpf=GeneratedQpRec.objects.filter(Dept_id=request.session["Dept_id"]).values()

    return HttpResponse("sdsds")        

def DownloadingFromNet(request):
    request.session["CreatedFileName"]=request.POST['Filename']
    print("here we are")
    return JsonResponse({
                'success': True,
                
            })          
    
   
    
def Download_paper_sys(request):
    
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    
    #k=Quest_BankTHR.objects.filter(id=int("11")).values()
    #print(k[0]["Qtext"])
    
    #obj.File_loc=os.path.join(BASE_DIR,'QuestionPapers')
   # obj.File_loc=BASE_DIR+"/QuestionPapers/"+request.session["CreatedFileName"]
    print("now now")
    os.path.exists(os.path.join(BASE_DIR,request.session["CreatedFileName"] ))
    with open(os.path.join(BASE_DIR,"QuestionPapers\\",request.session["CreatedFileName"] ), 'rb') as fh:
       
        response = HttpResponse(fh.read(), content_type="application/pdf")
        print(fh.readlines())
        response['Content-Disposition'] = 'attachment; filename='+request.session["CreatedFileName"]

       
        return response    

   

    
    
     
    



def DonDownloading(request):
    return HttpResponse("Done Downloading")    

def DonePDF(request):
    return HttpResponse("Done Downloading")   


def DeleteCO(request):
    Co=Course_outcome.objects.filter(Course_code=request.session["Course_code"]).values()
    print(Co)

    return render(request,'DeleteCO.html',{'CO_DET':Co,'Course_name':request.session["Course_name"],'Eusername':request.session["USERNAME"]})

def DeleteUD(request):
    Ud=Course_units.objects.filter(Course_code=request.session["Course_code"]).values()
    return render(request,'Delete_UD.html',{'Unit_det':Ud,'Course_name':request.session["Course_name"],'Eusername':request.session["USERNAME"]})

def DoneDeletingCO(request):
    return redirect('DeleteCO')
    return HttpResponse("<h2>COURSE OUTCOMES DELETED<h2>")

def DoneDeletingUD(request):
    return redirect('DeleteUD')
    return HttpResponse("<h2>UNIT DETAILS DELETED<h2>")

def DeleteNowUD(request):
    mcqidl=request.POST.getlist('mcqid[]')
   
    
    for i in mcqidl:
        Course_units.objects.filter(id=i).delete()

  

    return JsonResponse({
                'success': True,
                
            })  


    
def DeleteNowCO(request):

    mcqidl=request.POST.getlist('mcqid[]')
    print(mcqidl)
    
    for i in mcqidl:
        Course_outcome.objects.filter(id=i).delete()

  

    return JsonResponse({
                'success': True,
                
            })  
def DoneDelCMP(request):
    print("hewy")
    return redirect('CourseMapdet')
    return HttpResponse("<h2>DONE DELETING COURSE MAPPING<h2>")

def DoneDelStaff(request):
    return redirect('Staffdetails')
    return HttpResponse("<h2>DELETED STAFF RECORD<h2>")


def DeleteStaffD(request):
    Id=request.POST.getlist('mcqid[]')

    for i in Id:
        Teachers.objects.filter(Teach_id=i).delete()
        Teach_Course_MR.objects.filter(Teach_id=i).delete()

  

    return JsonResponse({
                'success': True,
                
            })  


def DeleteCourseMap(request):
    Id=request.POST.getlist('mcqid[]')
    print(Id)
    print("Inside here")
    for i in Id:
        Teach_Course_MR.objects.filter(id=i).delete()

  

    return JsonResponse({
                'success': True,
                
            })  


def DisplayInstance(request):

    thrinst=Theory_instance.objects.filter(Course_code=request.session["Course_code"]).values()
    mcqinst=Mcq_instance.objects.filter(Course_code=request.session["Course_code"]).values()
    return render(request,'InstanceDisplay.html',{"thrinst":thrinst,"mcqinst":mcqinst})    


def displayinstanceid(request):

    Id=request.POST["id"]
    request.session["instID"]=Id
    return JsonResponse({
                'success': True,
                
            })  

def displaybyid2(request):
    thrinst=Theory_instance.objects.filter(Question_id=request.session["instID"]).values()
    print(thrinst)
    return render(request,'InstanceDisplaythr.html',{"thrinst":thrinst,'Eusername':request.session["USERNAME"]})

def displayinstanceidm(request):

    Id=request.POST["id"]
    request.session["instID"]=Id
    return JsonResponse({
                'success': True,
                
            })      
def displaybyid2m(request):
    mcqinst=Mcq_instance.objects.filter(Question_id=request.session["instID"]).values()
    return render(request,'InstanceDisplaymcq.html',{"mcqinst":mcqinst,'Eusername':request.session["USERNAME"]})


def ViewDeptDetails(request):

    #DeptDetails=Department.objects.filter().values()
    DeptDetails=Teachers.objects.filter(Rights="HOD").values()

    return render(request,'ViewDeptDet.html',{'DeptDetails':DeptDetails,'Eusername':"SYSADMIN"})    

def changePW(request):

    return render(request,'ChangePW.html',{'Eusername':request.session["USERNAME"]})  

def changePWUP(request):

    oldpw=request.POST["oldpw"]
    newPW=request.POST["newpw1"]

    if(Teachers.objects.filter(Teach_uname=request.session["USERNAME"],Teach_pass=oldpw)).exists():
        Teachers.objects.filter(Teach_uname=request.session["USERNAME"]).update(Teach_pass=newPW)
        return HttpResponse("<h2>PASSWORD CHANGED SUCCESSFULLY<h2>")
    else:
        return HttpResponse("<h2>WRONG PASSWORD ENTERED<h2>")    
def Verify_pdf(request):

    ID=request.POST['id']
    RECORD=GeneratedQpRec.objects.filter(id=ID).values()[0]
    mcqarray=RECORD['mcqArray']
    thrarray=RECORD['thrArray']
    Course_code=RECORD['Course_code']
    ExamT=RECORD["Exam_type"]
    if(mcqarray!='empty'):
        mcqList=[int(x) for x in mcqarray.split(' ')]
        for j in mcqList:
            Quest_BankMCQ.objects.filter(id=j).update(RefCount=F('RefCount')+1)
            obj=Mcq_instance()
            obj.Question_id=j
            obj.Exam_record=ExamT
            obj.Exam_date=str(datetime.now())
            obj.Course_code=Course_code
            obj.save()
        
    thrarray=[int(x) for x in thrarray.split(' ')]
    for j in thrarray:
        Quest_BankTHR.objects.filter(id=j).update(RefCount=F('RefCount')+1) 
        obj=Theory_instance()
        obj.Question_id=j
        obj.Exam_record=ExamT
        obj.Exam_date=str(datetime.now())
        obj.Course_code=Course_code  
        obj.save()
    GeneratedQpRec.objects.filter(id=ID).update(verify="YES")  

    return JsonResponse({
                'success': True,
                
            })      

def CreateCourseAdmin(request):

    Dep_details=Department.objects.filter().values()
    return render(request,'InsertCourseSysad.html',{'Dep_details':Dep_details})

def InsertCourseSysad(request):

    
    if Courses.objects.filter(Course_code=request.POST["cid"]).exists():
        return HttpResponse("<h2>A Course with this Course Code already exists<h2>")
    obj=Courses()
    obj.Course_code=request.POST["cid"]
    obj.Course_name=request.POST["cname"]
    obj.Dept_id=request.POST["depid"]

    obj.save()

    return HttpResponse("<h2>New Course has been Successfuly added <h2>")
def Done_verify(request):

    return HttpResponse("<h2>The PAPER WAS Successfully Finalized<h2>")
        

def Deletepdf1(request):
    Deletepdf=GeneratedQpRec.objects.filter().values()

    return render(request,'Deletepdf.html',{'DeleteTable':Deletepdf})

def Deletepdf2(request):
    Id=request.POST.getlist('mcqid[]')

    for i in Id:
        GeneratedQpRec.objects.filter(id=i).delete()

  

    return JsonResponse({
                'success': True,
                
            })  


def DoneDeleting(request):

    return HttpResponse("<h2> PAPERS DELETED SUCCESSFULLY<h2>")

def Done_del_courses(request):
    return HttpResponse("<h2> SUCCESSFULLY DELETED<h2>")

def DelCourses(request):
    Id=request.POST.getlist('mcqid[]')
    for i in Id:
        Courses.objects.filter(Course_code=i).delete()
        Teach_Course_MR.objects.filter(Course_code=i).delete()
        Course_outcome.objects.filter(Course_code=i).delete()
        Course_units.objects.filter(Course_code=i).delete()
        Quest_BankMCQ.objects.filter(Course_code=i).delete()
        Quest_BankTHR.objects.filter(Course_code=i).delete()
    return JsonResponse({
                'success': True,
                
            })      
def DeleteCourses(request):
    courses=Courses.objects.filter(Dept_id=request.session["Dept_id"])
    return render(request,'DeleteCourses.html',{'Course':courses})

def AnyQMCQ(request):

    Subq=[2,2,2,3]
    Qnum=[['1.A','1.B'],['2.A','2.B'],['3.A','3.B'],['4.A','4.B','4.C']]
    