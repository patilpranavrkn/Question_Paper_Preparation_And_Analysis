from django.db import models
from django.contrib.postgres.fields import ArrayField


'''
class Department(models.Model):
    Dept_id=models.CharField(max_length=10,primary_key=True)
    Dept_name=models.CharField(max_length=100)
    Dept_code=models.CharField(max_length=10)
    Dept_huname=models.CharField(max_length=100)
    Dept_passkey=models.CharField(max_length=100)

class Depart_Teach(models.Model):
    Dept_id=models.CharField(max_length=10)
    Teach_uname=models.CharField(max_length=50)
    Teach_pass=models.CharField(max_length=50)

class Teachers(models.Model):
    Teach_name=models.CharField(max_length=50)
    Teach_uname=models.CharField(max_length=50,primary_key=True)
    Teach_id=models.CharField(max_length=10)
    
    Teach_pass=models.CharField(max_length=50)
    Dept_id=models.CharField(max_length=10)
    Rights=models.CharField(max_length=10,null=True)
class Courses(models.Model):
    Course_code=models.CharField(max_length=15,primary_key=True)
    Course_type=models.CharField(max_length=3)
    Course_name=models.CharField(max_length=50)
    Course_exam=models.CharField(max_length=15)
    Dept_id=models.CharField(max_length=10)
    Course_marks=models.IntegerField()

class Teach_Course_MR(models.Model):
    Dept_id=models.CharField(max_length=10)
    Teach_uname=models.CharField(max_length=50)
    Course_code=models.CharField(max_length=15)
    Rights=models.CharField(max_length=5)
    Course_name=models.CharField(max_length=50)



class Course_outcome(models.Model):
    Course_code=models.CharField(max_length=15)
    Outcome_no=models.IntegerField()
    Outcome_Text=models.CharField(max_length=100)

class Course_units(models.Model):
    Course_code=models.CharField(max_length=15)
    Unit_num=models.CharField(max_length=100)
    Unit_name=models.CharField(max_length=50)
    Unit_Details=models.CharField(max_length=50)
    Unit_marks=models.IntegerField()

class Quest_BankMCQ(models.Model):
    Course_code=models.CharField(max_length=15)
    Qtext=models.TextField(null=True)
    choice_1=models.CharField(max_length=50,null=True)
    choice_2=models.CharField(max_length=50,null=True)
    choice_3=models.CharField(max_length=50,null=True)
    choice_4=models.CharField(max_length=50,null=True)
    image=models.ImageField(upload_to="diagrams/%Y/%m/%d",null=True)
    BloomL=models.IntegerField(blank=True, null=True)
    Co=models.IntegerField(blank=True, null=True)
    unit_num=models.IntegerField(blank=True, null=True)
    max_marks=models.IntegerField(blank=True, null=True)
    min_marks=models.IntegerField(blank=True, null=True)
    remarks=models.CharField(max_length=40,null=True)
    State=models.CharField(max_length=5)
    RefCount=models.IntegerField(blank=True,null=True)


class Quest_BankTHR(models.Model):
    Course_code=models.CharField(max_length=15)
    Qtext=models.TextField(null=True)
    image=models.ImageField(upload_to="diagrams/%Y/%m/%d",null=True)
    BloomL=models.IntegerField(blank=True, null=True)
    Co=models.IntegerField(blank=True, null=True)
    unit_num=models.IntegerField(blank=True, null=True)
    max_marks=models.IntegerField(blank=True, null=True)
    min_marks=models.IntegerField(blank=True, null=True)
    remarks=models.CharField(max_length=40,null=True)
    State=models.CharField(max_length=5)
    RefCount=models.IntegerField(blank=True,null=True)

class Theory_instance(models.Model):
    Question_id=models.IntegerField()
    Text=models.TextField(null=True)
    Exam_record=models.TextField(null=True)
    Exam_date=models.CharField(max_length=50,null=True)
    Course_code=models.CharField(max_length=15,null=True)


class Mcq_instance(models.Model):
    Question_id=models.IntegerField()
    Text=models.TextField(null=True)
    Exam_record=models.TextField(null=True)
    Exam_date=models.CharField(max_length=50,null=True)
    Course_code=models.CharField(max_length=15,null=True)






class GeneratedQpRec(models.Model):
    File_name=models.TextField(blank=True,null=True)
    File_loc=models.TextField(blank=True,null=True)
    File_author=models.CharField(max_length=30)
    Dept_id=models.CharField(max_length=10)
    Creation_Date=models.CharField(max_length=30,blank=True,null=True)
    
    
'''
from django.db import models

  

class Department(models.Model):
    Dept_id=models.CharField(max_length=10,primary_key=True)
    Dept_name=models.CharField(max_length=100)
    Dept_code=models.CharField(max_length=10)
    #Dept_huname=models.CharField(max_length=100)
    #Dept_passkey=models.CharField(max_length=100)




class Teachers(models.Model):
    
    Teach_id=models.CharField(max_length=10,primary_key=True)
    Teach_name=models.CharField(max_length=50)
    Teach_uname=models.CharField(max_length=50)
    
    Teach_pass=models.CharField(max_length=50)
    Dept_id=models.CharField(max_length=10,null=True)
    Rights=models.CharField(max_length=10,null=True)
class Depart_Teach(models.Model):
    
    Teach_id=models.CharField(max_length=10)
    Dept_id=models.CharField(max_length=10)   
class Courses(models.Model):
    Course_code=models.CharField(max_length=15,primary_key=True)
    #Course_type=models.CharField(max_length=3)
    Course_name=models.CharField(max_length=50)
    #Course_exam=models.CharField(max_length=15)
    Dept_id=models.CharField(max_length=10)
    #Course_marks=models.IntegerField()

class Teach_Course_MR(models.Model):
    #Teach_id=models.CharField(max_length=10)
    #Teach_uname=models.CharField(max_length=50)
    #Course_code=models.CharField(max_length=15)
    #Rights=models.CharField(max_length=5)
    Course_name=models.CharField(max_length=50,null=True)
    Teach_uname=models.CharField(max_length=50,null=True)
    Teach_id=models.CharField(max_length=10,null=True)
    Course_code=models.CharField(max_length=15)
    Dept_id=models.CharField(max_length=10,null=True)
    Rights=models.CharField(max_length=5)  



class Course_outcome(models.Model):
    Course_code=models.CharField(max_length=15)
    Outcome_no=models.IntegerField()
    Outcome_Text=models.CharField(max_length=100)

class Course_units(models.Model):
    Course_code=models.CharField(max_length=15)
    Unit_num=models.CharField(max_length=100)
    Unit_name=models.CharField(max_length=50)
    Unit_Details=models.CharField(max_length=50)
    Unit_marks=models.IntegerField()

class Quest_BankMCQ(models.Model):
    Course_code=models.CharField(max_length=15)
    Qtext=models.TextField(null=True)
    choice_1=models.CharField(max_length=50,null=True)
    choice_2=models.CharField(max_length=50,null=True)
    choice_3=models.CharField(max_length=50,null=True)
    choice_4=models.CharField(max_length=50,null=True)
    image=models.ImageField(upload_to="diagrams/%Y/%m/%d",null=True)
    BloomL=models.IntegerField(blank=True, null=True)
    Co=models.IntegerField(blank=True, null=True)
    unit_num=models.IntegerField(blank=True, null=True)
    max_marks=models.IntegerField(blank=True, null=True)
    min_marks=models.IntegerField(blank=True, null=True)
    remarks=models.CharField(max_length=40,null=True)
    State=models.CharField(max_length=5)
    RefCount=models.IntegerField(blank=True,null=True)


class Quest_BankTHR(models.Model):
    Course_code=models.CharField(max_length=15)
    Qtext=models.TextField(null=True)
    image=models.ImageField(upload_to="diagrams/%Y/%m/%d",null=True)
    BloomL=models.IntegerField(blank=True, null=True)
    Co=models.IntegerField(blank=True, null=True)
    unit_num=models.IntegerField(blank=True, null=True)
    max_marks=models.IntegerField(blank=True, null=True)
    min_marks=models.IntegerField(blank=True, null=True)
    remarks=models.CharField(max_length=40,null=True)
    State=models.CharField(max_length=5)
    RefCount=models.IntegerField(blank=True,null=True)

class Theory_instance(models.Model):
    Question_id=models.IntegerField()
    
    Exam_record=models.TextField(null=True)
    Exam_date=models.CharField(max_length=50,null=True)
    Course_code=models.CharField(max_length=15,null=True)


class Mcq_instance(models.Model):
    Question_id=models.IntegerField()
   
    Exam_record=models.TextField(null=True)
    Exam_date=models.CharField(max_length=50,null=True)
    Course_code=models.CharField(max_length=15,null=True)






class GeneratedQpRec(models.Model):
    File_name=models.TextField(blank=True,null=True)
    File_loc=models.TextField(blank=True,null=True)
    File_author=models.CharField(max_length=30)
    Dept_id=models.CharField(max_length=10)
    Creation_Date=models.CharField(max_length=30,blank=True,null=True)
    Course_code=models.CharField(max_length=15,null=True)
    mcqArray=models.CharField(max_length=100,null=True)
    thrArray=models.CharField(max_length=100,null=True)
    Exam_type=models.CharField(max_length=100,null=True)
    verify=models.CharField(max_length=10,null=True)
   
    











   



    


    





# Create your models here.
