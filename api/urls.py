from django.urls import path

from . import views
urlpatterns = [
    #ignore this data below one
    path("",views.getRoutes),
    path("books/",views.books),
    path("notes/",views.getNotes),
    path("notes/create/",views.createNote),
    path("notes/<str:pk>",views.getNote),
    path("notes/<str:pk>/update",views.updateNote),
    path("notes/<str:pk>/delete",views.deleteNote),
     #ignore this data above one
    path('api/create_user_profile/', views.create_user_profile, name='create_user_profile'),
    #viewing all the users
    path('api/Users/', views.getUsers, name='get_users'),
      #viewing one user
    path('api/Users/<str:pk>', views.get_user_profile, name='get_each_users'),
    #updating the users
    path('api/create_user_profile/<str:pk>/update', views.updateUser, name='update_user_profile'),
    #for deleting the users profile
    path('api/create_user_profile/<str:pk>/delete', views.delete_user_profile, name='delete_user_profile'),
    

    #createing the profile after making user profile and get and delete is also done on it

    path('api/create_user_profile/<str:pk>/create_Proper_Profile', views.create_after_create_user_profile, name='after_creating_user_profile'),
    # path('api/create_user_profile/7/view_Proper_Profile/<str:pk>', views.deleteProfile, name='get_creating_user_profile'),
    path('api/create_user_profile/<str:pk>/create_Proper_Profile/entreprenuer', views.entrepreneur_profile_view, name='creating_entreprenuer_profile'),

    path('api/entrepreneur_profiles/<int:user_id>/<int:profile_id>',views.get_entrepreneur_profile, name='get_entrepreneur_profile'),
    

     # URL pattern for creating or retrieving ProperProfileCreation
    # path('api/create_user_profile/<int:pk>/create_Proper_Profile/entreprenuer/', create_after_create_user_profile, name='create_after_create_user_profile'),

    # URL pattern for creating or retrieving Project
    path('api/create_user_profile/<int:pk>/create_project', views.project_view, name='project_view'),
    path('api/project_proposal/<int:user_id>/<int:profile_id>',views.get_project_proposal, name='get_project_proposal'),
#for getting all the projects
    path('api/Projects/', views.getProjects, name='get_projects'),

#write the get code of the project here to get all projects with respect to user
      path('api/Projects/<int:pk>', views.get_all_project_view_of_each_user, name='get_all_project_view_of_each_user'),    

#for updating the projects of entrepreneur
    path('api/Projects/<int:pk>/update/<int:project_id>', views.update_project_view, name='update_projects'),
#for deleting the projects of entrepreneur
    path('api/Projects/<int:pk>/delete/<int:project_id>', views.delete_project_view, name='delete_projects'),    


    #for investor uploading the project of him
    path('api/create_user_profile/<int:pk>/create_investor_project', views.Investor_project_view, name='Investor_project_view'),
    #getting all investor projects
    path('api/InvestorProjects/', views.getInvestorProjects, name='get_Investor_projects'),
    #for updating the projects of investor


    path('api/InvestorProjects/<int:pk>/update/<int:investment_id>', views.update_investor_project_view, name='update_Investor_projects'),

    #for deleting the projects of investor


    path('api/InvestorProjects/<int:pk>/delete/<int:investment_id>', views.delete_investor_project_view, name='delete_Investor_projects'),
    #to get investor project of each user
    #write the get code of the project here to get all projects with respect to user
      path('api/InvestorProjects/<int:pk>', views.get_all_project_view_of_each_Investor_user, name='get_all_project_view_of_each_Investor_user'), 
#for sending notifications

path('send-push-notification/', views.send_push_notification, name='send_push_notification'),
]
