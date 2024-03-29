from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns=[
    #path('',views.home,name='home'),
    path('',views.TeacherLoginLP,name='TeacherLoginLP'),
    path('Logagain',views.TeacherLoginLP,name='TeacherLoginLP'),
  
    path('HODLoginLP',views.HODLoginLP,name='HODLoginLP'),
    path('DeanLoginLP',views.DeanLoginLP,name='DeanLoginLP'),
    path('TeacherLogout',views.Logout,name='TeacherLogout'),
    path('AdminHomePage',views.RAdminHomePage,name='RAdminHomePage'),
    path('CreateDep',views.CreateDep,name='CreateDep'),
    path('UpdateDep',views.UpdateDep,name='UpdateDep'),
    path('DeleteDep',views.DeleteDep,name='DeleteDep'),
    path('InsertDepInfo',views.InsertDepInfo,name='InsertDepInfo'),
    path('InsertCourse',views.InsertCourse,name='InsertCourse'),
    path('InsertTeacher',views.InsertTeacher,name='InsertTeacher'),
    path('AddmcqQues',views.AddmcqQues,name='AddmcqQues'),
    path('AddTheoryQues',views.AddTheoryQues,name='AddTheoryQues'),
    path('HodHomePage',views.RHodHomePage,name='RHodHomePage'),
    path('RinsertCourse',views.RinsertCourse,name='RinsertCourse'),
    path('RinsertTeacher',views.RinsertTeacher,name='RinsertTeacher'),
    path('MapTC',views.RmapTc,name='RmapTc'),
    path('InsertMapCT',views.InsertMapTc,name='InsertMapTc'),
    path('TeacherHomePage',views.RThomePage,name='RThomePage'),
    path('ChooseQtype',views.RChooseQuest,name='RChooseQuest'),
    path('ChooseTheory',views.ChooseTheory,name='ChooseTheory'),
    path('ChooseMcq',views.ChooseMcq,name='ChooseMcq'),
    path('CreatePaper',views.RCreatePaper,name='RCreatePaper'),
    path('template_details',views.GetTemplateDetails,name='GetTemplateDetails'),
    path('template_details_noMCQ',views.NoMcqTemplateDetails,name='NoMcqTemplateDetails'),
    
    path('mapmults',views.MapMults,name='MapMults'),
    path('AddCO',views.RAddCo,name='RAddCo'),
    path('AddUD',views.RAddUD,name='RAddUD'),
    path('InsertCo',views.AddCo,name='AddCo'),
    path('InsertUd',views.AddUd,name='AddUd'),
    path('AnalyzeCQ',views.AnalyzeCQ,name='AnalyzeCQ'),
    path('ver_quests',views.VerQuests,name='VerQuests'),
    path('gen_templ',views.AddTemplQuest,name='AddTemplQuest'),
    path('Hod_Courses',views.HodSelCourse,name='HodSelCourse'),
    path('NewTempl1',views.NewTempl1,name='NewTempl1'),
    path('gen_latex',views.genLatex,name='genLatex'),
    path('gen_latex_no_mcq',views.genLatexNoMcq,name='genLatexNoMcq'),
    path('gen_templ_no_mcq',views.AddTemplQuestNoMCQ,name='AddTemplQuestNoMCQ'),
    path('Logout',views.Logout,name='Logout'),
    path('Dep_det_all',views.Dep_det_all,name='Dep_det_all'),
    path('Delete_questions',views.Delete_questions,name='Delete_questions'),
    path('See_staff_details',views.Staffdetails,name='Staffdetails'),
    path('Course_map_details',views.CourseMapdet,name='CourseMapdet'),
    path('del_quests',views.DelQuest,name='DelQuest'),
    path('Done_Latex',views.Done_paper,name='Done_paper'),
    path('Done_ver',views.Done_Ver,name='Done_Ver'),
    path('Staffdetails',views.Staffdetails,name='Staffdetails'),
    path('CourseMapdet',views.CourseMapdet,name='CourseMapdet'),
    path('Done_Deleting',views.DoneDeleting,name='DoneDeleting'),
    path('Sysdownloadpdf',views.Downloadpdfsys,name='Downloadpdfsys'),
    path('Hodownloadpdf',views.Hodownloadpdf,name='Hodownloadpdf'),
    path('download_pdf_fromname',views.DownloadingFromNet,name='DownloadingFromNet'),
    path('Done_download',views.DonePDF,name='DonePDF'),
    path('Delete_Co',views.DeleteCO,name='DeleteCO'),
    path('Delete_unitD',views.DeleteUD,name='DeleteUD'),
    path('Done_Deleting_co',views.DoneDeletingCO,name='DoneDeletingCO'),
    path('Done_Deleting_ud',views.DoneDeletingUD,name='DoneDeletingUD'),
    path('del_unit_det',views.DeleteNowUD,name='DeleteNowUD'),
    path('del_co_det',views.DeleteNowCO,name='DeleteNowCO'),
    path('del_staff_det',views.DeleteStaffD,name='DeleteStaffD'),
    path('del_course_map',views.DeleteCourseMap,name='DeleteCourseMap'),
    path('Done_Deleting_courseMP',views.DoneDelCMP,name='DoneDelCMP'),
    path('Done_Deleting_staff',views.DoneDelStaff,name='DoneDelStaff'),
    path('Instance_det',views.DisplayInstance,name='DisplayInstance'),
    path('display_instance_id',views.displayinstanceid,name='displayinstanceid'),
    path('displaybyid2',views.displaybyid2,name='displaybyid2'),
    path('display_instance_idm',views.displayinstanceid,name='displayinstanceidm'),
    path('displaybyid2m',views.displaybyid2,name='displaybyid2m'),
    path('Done_Latex_sys',views.Download_paper_sys,name='Download_paper_sys'),
    path('ViewDepDetails',views.ViewDeptDetails,name='ViewDepDetails'),
    path('changePW',views.changePW,name='changePW'),
    path('ChangePWUP',views.changePWUP,name='changePWUP'),
  
    path('CreateCourseAdmin',views.CreateCourseAdmin,name='CreateCourseAdmin'),
    path('InsertCourseSysad',views.InsertCourseSysad,name='InsertCourseSysad'),
    path('Verify_pdf',views.Verify_pdf,name='Verify_pdf'),
    path('Done_verify',views.Done_verify,name='Done_verify'),
    path('Deletepdf1',views.Deletepdf1,name='Deletepdf1'),
    path('Deletepdf2',views.Deletepdf2,name='Deletepdf2'),
    path('Done_Deleting_pdf',views.DoneDeleting,name='DoneDeleting'),
    path('del_courses',views.DelCourses,name='DelCourses'),
    path('Done_del_courses',views.Done_del_courses,name='Done_del_courses'),
    path("Delete_Courses",views.DeleteCourses,name='DeleteCourses'),
    

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)