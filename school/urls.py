from django.urls import path
from . import views

urlpatterns = [


    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),



    path('', views.home, name="home"),
    path('user_home/', views.user_home, name="user_home"),
    path('staff/', views.staff, name="staff"),
    
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('maths/', views.maths, name="maths"),
    path('sciences/', views.sciences, name="sciences"),
    path('arts/', views.arts, name="arts"),
    path('geography/', views.geography, name="geography"),
    path('religious_studies/', views.religious_studies, name="religious_studies"),

    path('user_staff/', views.user_staff, name="user_staff"),
    path('user_about/', views.user_about, name="user_about"),
    path('user_contact/', views.user_contact, name="user_contact"),

    path('student_profile/', views.student_profiles, name="student_profile"),



    path('class_section/', views.class_section, name="class_section"),
    path('profile/<str:pk>/', views.profile, name="profile"),
    path('student/', views.student, name="student"),
    path('attendence/<str:pk>/', views.attendence, name="attendence"),
    path('student_grades/<str:pk>/', views.student_grades, name="student_grades"),

    path('student_page/', views.student, name="student_page"),
    path('student_attendence/', views.student_attendence, name="student_attendence"),
    path('student_marks/', views.student_marks, name="student_marks"),


    # path('report/', views.report, name="home"),

    path('teacher_panel/', views.teacher_panel, name="teacher_panel"),



    path('createGeography/', views.createGeography, name="create_geography"),
    path('createArts/', views.createArts, name="create_arts"),
    path('createMaths/', views.createMaths, name="create_maths"),
    path('createReligious_studies/', views.createReligious_studies, name="create_religious_studies"),
    path('createSciences/', views.createSciences, name="create_sciences"),
    path('createstudent_profile/', views.createStudentProfile, name="create_student_profile"),

    path('updateGeography/<str:pk>/', views.updateGeography, name="update_geography"),
    path('deleteGeography/<str:pk>/', views.deleteGeography, name="delete_geography"),
    path('updateeArts/<str:pk>/', views.updateArts, name="update_arts"),
    path('deleteArts/<str:pk>/', views.deleteArts, name="delete_arts"),
    path('updateMaths/<str:pk>/', views.updateMaths, name="update_maths"),
    path('deleteMaths/<str:pk>/', views.deleteMaths, name="delete_maths"),
    path('updateReligious_studies/<str:pk>/', views.updateReligious_studies, name="update_religious_studies"),
    path('deleteReligious_studies/<str:pk>/', views.deleteReligious_studies, name="delete_religious_studies"),
    path('updateSciences/<str:pk>/', views.updateSciences, name="update_sciences"),
    path('deleteSciences/<str:pk>/', views.deleteSciences, name="delete_sciences"),
    path('updatestudent_profile_form/<str:pk>/', views.updateStudentProfile, name="update_student_profile_form"),
    path('deletestudent_profile_form/<str:pk>/', views.deleteStudentProfile, name="delete_student_profile_form"),


    path('account/', views.accountSettings, name="account"),

















    # path('physics/', views.physics, name=""),
    # path('english/', views.english, name="home"),
    # path('chemistry/', views.chemistry, name="home"),
    # path('biology/', views.biology, name="home"),
    # path('economics/', views.economics, name="home"),
    # path('business_studies/', views.business_studies, name="home"),
    # path('accounts/', views.accounts, name="home"),

    # path('s_math/<str:pk>/', views.s_math),
    # path('s_re/<str:pk>/', views.s_re),
    # path('s_art/<str:pk>/', views.s_art),
    # path('s_science/<str:pk>/', views.s_science),





]
