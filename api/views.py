from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notes,UserProfileAfterLogin,UserProfileBeforeLogin,ProperProfileCreation,EntrepreneurProfile,Project,InvestorProject
from .serializers import NotesSerializers,BeforeLoginSerializers,AfterLoginSerializers,ProperProfileCreationSerializers,EntrepreneurProfileCreationSerializers,ProjectSerializers,InvestorProjectSerializers
from rest_framework import status,generics
# from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
# Create your views here.
@api_view(['POST'])
def books(request):
    return Response('these are my books',status=status.HTTP_200_OK)



@api_view(['POST','GET','DELETE'])
def getRoutes(request):
    routes = [
        {
            'Endpoint':' /notes/',
            'method':'GET',
            'body': None,
            'description':'an array of notes'

        },
        {
            'Endpoint':' /notes/id',
            'method':'GET',
            'body': None,
            'description':'get single notes'

        },
        {
            'Endpoint':' /notes/create/',
            'method':'POST',
            'body': {'body':""},
            'description':'Creates new notes with data send in post request'

        },
        {
             'Endpoint':' /notes/id/updates/',
            'method':'POST',
            'body': {'body':""},
            'description':'Creates existing notes with data send in post request'

        },
         {
             'Endpoint':' /notes/id/delete/',
            'method':'DELETE',
            'body': None,
            'description':'Delete the existing notes'

        },

    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Notes.objects.all()
    serializer = NotesSerializers(notes,many = True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request,pk):
    note = Notes.objects.get(id= pk)

    serializer = NotesSerializers(note,many = False)
    return Response(serializer.data)
@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Notes.objects.create(
        body=  data['body']
    )
    serializer  =NotesSerializers(note,many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data
    note = Notes.objects.get(id = pk)
    serializer  =NotesSerializers(note,data = data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request,pk):
    note = Notes.objects.get(id = pk)
    note.delete()

    return Response("Note was deleted")


#user login part
#creating a user
@api_view(['POST'])
def create_user_profile(request):
    data = request.data
    user_profile = UserProfileBeforeLogin.objects.create(
        username=data['username'],
        password=data['password'],
        email=data['email'],
        phoneNumber=data['phoneNumber']
    )
    serializer = BeforeLoginSerializers(user_profile, many=False)
    return Response(serializer.data)
#for deleting the user
@api_view(['DELETE'])
def delete_user_profile(request, pk):
    try:
        user_profile = UserProfileBeforeLogin.objects.get(id=pk)
    except UserProfileBeforeLogin.DoesNotExist:
        return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)

    user_profile.delete()
    return Response({"message": "User profile deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

#Viewing all users
@api_view(['GET'])
def getUsers(request):
    notes = UserProfileBeforeLogin.objects.all()
    serializer = BeforeLoginSerializers(notes,many = True)
    return Response(serializer.data)
#get each user
@api_view(['GET'])
def get_user_profile(request, pk):
    try:
        user_profile = UserProfileBeforeLogin.objects.get(id=pk)
    except UserProfileBeforeLogin.DoesNotExist:
        return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)

    # You can customize the response data based on your model structure
    response_data = {
        "id": user_profile.id,
        "username": user_profile.username,
        "email": user_profile.email,
        "phoneNumber":user_profile.phoneNumber,
        "role":user_profile.role
        # Add other fields as needed
    }

    return Response(response_data, status=status.HTTP_200_OK)

#Updating the User
@api_view(['PUT'])
def updateUser(request,pk):
    data = request.data
    note = UserProfileBeforeLogin.objects.get(id = pk)
    serializer  =BeforeLoginSerializers(note,data = data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def deleteUser(request,pk):
    data = request.data
    note = UserProfileBeforeLogin.objects.get(id = pk)
    serializer  =BeforeLoginSerializers(note,data = data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#after user profile is successfully created we will now add more information here for ProperProfileCreation

# @api_view(['POST'])
# def create_after_create_user_profile(request,pk):
#     data = request.data
#     user_profile = ProperProfileCreation.objects.create(
#     userID=data['UserId'],
#     username=data['username'],
#     password=data['password'],
#     email=data['email'],
#     phoneNumber=data['phoneNumber'],
#     role=data['role'],
#     date_of_birth=data['date_of_birth'],
#     city=data['date_of_birth'],
#     country=data['date_of_birth'],
#     postalCode=data['date_of_birth'],
#     latest_job=data['date_of_birth'],
#     salary_Income_allowance=data['date_of_birth'],
#     is_married=data['date_of_birth'],
#     cnic_number=data['date_of_birth']
# )

#     serializer = ProperProfileCreationSerializers(user_profile, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_after_create_user_profile(request, pk):
#     data = request.data
#     user_profile = ProperProfileCreation.objects.create(
#         UserId=pk,  # Assuming 'UserId' is part of the URL path
#         username=data.get('username', ''),
#         password=data.get('password', ''),
#         email=data.get('email', ''),
#         phoneNumber=data.get('phoneNumber', ''),
#         role=data.get('role', ''),
#         date_of_birth=data.get('date_of_birth', ''),
#         city=data.get('city', ''),
#         country=data.get('country', ''),
#         postalCode=data.get('postalCode', ''),
#         latest_job=data.get('latest_job', ''),
#         salary_Income_allowance=data.get('salary_Income_allowance', 0.00),
#         is_married=data.get('is_married', ''),
#         cnic_number=data.get('cnic_number', '')
#     )

#     serializer = ProperProfileCreationSerializers(user_profile, many=False)
#     return Response(serializer.data)

# for viewing the profile
# @api_view(['GET'])
# def get_after_create_user_profile(request,pk):
#     notes = ProperProfileCreation.objects.get(id = pk)
#     serializer = ProperProfileCreationSerializers(notes,many = True)
#     return Response(serializer.data)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])  # Allow both GET and POST requests
def create_after_create_user_profile(request, pk):
    if request.method == 'GET':
        # Retrieve the created profile based on the provided user ID (pk)
        user_profile = get_object_or_404(ProperProfileCreation, UserId=pk)
        serializer = ProperProfileCreationSerializers(user_profile, many=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create the profile as you've done in your original function
        data = request.data
        user_profile = ProperProfileCreation.objects.create(
            UserId=pk,
            username=data.get('username', ''),
            password=data.get('password', ''),
            email=data.get('email', ''),
            phoneNumber=data.get('phoneNumber', ''),
            role=data.get('role', ''),
            date_of_birth=data.get('date_of_birth', ''),
            city=data.get('city', ''),
            country=data.get('country', ''),
            postalCode=data.get('postalCode', ''),
            latest_job=data.get('latest_job', ''),
            salary_Income_allowance=data.get('salary_Income_allowance', 0.00),
            is_married=data.get('is_married', ''),
            cnic_number=data.get('cnic_number', '')
        )

        serializer = ProperProfileCreationSerializers(user_profile, many=False)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        # Retrieve the user_profile for deletion
        user_profile = get_object_or_404(ProperProfileCreation, UserId=pk)
        # Delete the profile
        user_profile.delete()
        return Response({'message': 'Profile deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        # Update the profile based on the provided user ID (pk)
        user_profile = get_object_or_404(ProperProfileCreation, UserId=pk)
        data = request.data

        user_profile.username = data.get('username', user_profile.username)
        user_profile.password = data.get('password', user_profile.password)
        user_profile.email = data.get('email', user_profile.email)
        user_profile.phoneNumber = data.get('phoneNumber', user_profile.phoneNumber)
        user_profile.role = data.get('role', user_profile.role)
        user_profile.date_of_birth = data.get('date_of_birth', user_profile.date_of_birth)
        user_profile.city = data.get('city', user_profile.city)
        user_profile.country = data.get('country', user_profile.country)
        user_profile.postalCode = data.get('postalCode', user_profile.postalCode)
        user_profile.latest_job = data.get('latest_job', user_profile.latest_job)
        user_profile.salary_Income_allowance = data.get('salary_Income_allowance', user_profile.salary_Income_allowance)
        user_profile.is_married = data.get('is_married', user_profile.is_married)
        user_profile.cnic_number = data.get('cnic_number', user_profile.cnic_number)
        user_profile.save()

        serializer = ProperProfileCreationSerializers(user_profile, many=False)
        return Response(serializer.data)



@api_view(['DELETE'])
def deleteProfile(request,pk):
    note = ProperProfileCreation.objects.get(id = pk)
    note.delete()

    return Response("Note was deleted")

#making an entrepreneur profile

@api_view(['GET', 'POST'])
def entrepreneur_profile_view(request, pk):
    if request.method == 'GET':
        # Retrieve the entrepreneur profile based on the provided user ID (pk)
        entrepreneur_profile = get_object_or_404(EntrepreneurProfile, UserId=pk)
        serializer = EntrepreneurProfileCreationSerializers(entrepreneur_profile, many=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create the entrepreneur profile
        data = request.data
        entrepreneur_profile = EntrepreneurProfile.objects.create(
            UserId=pk,
            company_name=data.get('company_name', ''),
            industry_expertise=data.get('industry_expertise', ''),
            job_title=data.get('job_title', ''),
            previous_venture=data.get('previous_venture', ''),
            years_of_experience=data.get('years_of_experience', 0),
            achievements=data.get('achievements', ''),
            key_skills=data.get('key_skills', ''),
            highest_education_attained=data.get('highest_education_attained', ''),
            profile_image=data.get('profile_image'),
            linkedin_profile=data.get('linkedin_profile', ''),
            twitter_profile=data.get('twitter_profile', ''),
            bio=data.get('bio', ''),
        )

        serializer = EntrepreneurProfileCreationSerializers(entrepreneur_profile, many=False)
        return Response(serializer.data)
    

@api_view(['GET'])
def get_entrepreneur_profile(request, user_id, profile_id):
    # Use get_object_or_404 to retrieve the entrepreneur profile based on both user ID and profile ID
    entrepreneur_profile = get_object_or_404(EntrepreneurProfile, UserId=user_id, id=profile_id)

    # Serialize the data
    serializer = EntrepreneurProfileCreationSerializers(entrepreneur_profile)

    # Return the serialized data in the response
    return Response(serializer.data)    




#makimg proposal of the project

@api_view(['POST'])
def project_view(request, pk):
    # if request.method == 'GET':
    #     # Retrieve the project based on the provided user ID (pk)
    #     project = get_object_or_404(Project, UserId=pk)
    #     serializer = ProjectSerializers(project, many=False)
    #     return Response(serializer.data)

    if request.method == 'POST':
        # Create the project
        data = request.data
        project = Project.objects.create(
            UserId=pk,
            name=data.get('name', ''),
            field=data.get('field', ''),
            minimum_investment=data.get('minimum_investment', 0.00),
            guaranteed_profit=data.get('guaranteed_profit', 0.00),
            chance_of_risk=data.get('chance_of_risk', 0.0),
            description=data.get('description', ''),
            time_scale=data.get('time_scale', '')
        )

        serializer = ProjectSerializers(project, many=False)
        return Response(serializer.data)
    

#for getting the proposal of the project    
@api_view(['GET'])
def get_project_proposal(request, user_id, profile_id):
    # Use get_object_or_404 to retrieve the entrepreneur profile based on both user ID and profile ID
    entrepreneur_profile = get_object_or_404(Project, UserId=user_id, project_id=profile_id)

    # Serialize the data
    serializer = ProjectSerializers(entrepreneur_profile)

    # Return the serialized data in the response
    return Response(serializer.data)  


@api_view(['GET'])
def getProjects(request):
    if request.method == 'GET':
        # Get all projects
        projects = Project.objects.all()

        # Filter by minimum_investment and maximum_investment if provided in query parameters
        min_investment = request.query_params.get('min_investment')
        max_investment = request.query_params.get('max_investment')
        min_guaranteed_profit = request.query_params.get('min_guaranteed_profit')
        max_guaranteed_profit = request.query_params.get('max_guaranteed_profit')

        # Convert string values to Decimal if they exist
        if min_investment is not None:
            min_investment = Decimal(min_investment)
            projects = projects.filter(minimum_investment__gte=min_investment)
        if max_investment is not None:
            max_investment = Decimal(max_investment)
            projects = projects.filter(minimum_investment__lte=max_investment)
        if min_guaranteed_profit is not None:
            min_guaranteed_profit = Decimal(min_guaranteed_profit)
            projects = projects.filter(guaranteed_profit__gte=min_guaranteed_profit)
        if max_guaranteed_profit is not None:
            max_guaranteed_profit = Decimal(max_guaranteed_profit)
            projects = projects.filter(guaranteed_profit__lte=max_guaranteed_profit)

        serializer = ProjectSerializers(projects, many=True)
        return Response(serializer.data)

#for updating the project proposal of entreprenuer
def update_project(project, data):
    project.name = data.get('name', project.name)
    project.field = data.get('field', project.field)
    project.minimum_investment = data.get('minimum_investment', project.minimum_investment)
    project.guaranteed_profit = data.get('guaranteed_profit', project.guaranteed_profit)
    project.chance_of_risk = data.get('chance_of_risk', project.chance_of_risk)
    project.description = data.get('description', project.description)
    project.time_scale = data.get('time_scale', project.time_scale)
    project.save()

@api_view(['PUT'])
def update_project_view(request, pk,project_id):
    project = get_object_or_404(Project, UserId=pk,project_id = project_id)

    if request.method == 'PUT':
      data = request.data
      update_project(project, data)

    serializer = ProjectSerializers(project, many=False)
    return Response(serializer.data)  
# for getting all the projects with respect to UserID
@api_view(['GET'])
def get_all_project_view_of_each_user(request, pk, project_id=None):
    if request.method == 'GET':
        projects = Project.objects.filter(UserId=pk)
        serializer = ProjectSerializers(projects, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_all_project_view_of_each_Investor_user(request, pk, project_id=None):
    if request.method == 'GET':
        projects = InvestorProject.objects.filter(UserId=pk)
        serializer = InvestorProjectSerializers(projects, many=True)
        return Response(serializer.data)
@api_view(['DELETE'])
def delete_project_view(request, pk,project_id):
    project = get_object_or_404(Project, UserId=pk,project_id = project_id)

    if request.method == 'DELETE':
      project.delete()
      return Response({'message': 'Investor project deleted successfully'}, status=204)  



#get the investor project
@api_view(['POST'])
def Investor_project_view(request, pk):
    # if request.method == 'GET':
    #     # Retrieve the project based on the provided user ID (pk)
    #     project = get_object_or_404(Project, UserId=pk)
    #     serializer = ProjectSerializers(project, many=False)
    #     return Response(serializer.data)

    if request.method == 'POST':
        # Create the project
        data = request.data
        project = InvestorProject.objects.create(
            UserId=pk,
             field_of_investment=data.get('field_of_investment', ''),
             years_of_investment=data.get('years_of_investment', ''),
            minimum_investment=data.get('minimum_investment', 0.00),
            minimum_profit=data.get('minimum_profit', 0.00),
            allowed_risk=data.get('allowed_risk', 0.0),
            description=data.get('description', ''),
            time_scale_allowed=data.get('time_scale_allowed', '')
        )

        serializer = InvestorProjectSerializers(project, many=False)
        return Response(serializer.data)
#updating the investor project 
#Fix this poart of code 

def update_investor_project(project, data):
    project.field_of_investment = data.get('field_of_investment', project.field_of_investment)
    project.years_of_investment = data.get('years_of_investment',project.years_of_investment )
    project.minimum_investment = data.get('minimum_investment', project.minimum_investment)
    project.minimum_profit = data.get('minimum_profit', project.minimum_profit)
    project.allowed_risk = data.get('allowed_risk', project.allowed_risk)
    project.description = data.get('description', project.description)
    project.time_scale_allowed = data.get('time_scale_allowed', project.time_scale_allowed)
    project.save()

@api_view(['PUT'])
def update_investor_project_view(request, pk,investment_id):
    project = get_object_or_404(InvestorProject, UserId=pk,investment_id = investment_id)

    if request.method == 'PUT':
      data = request.data
      update_investor_project(project, data)

    serializer = InvestorProjectSerializers(project, many=False)
    return Response(serializer.data)

#deleting the investor project
@api_view(['DELETE'])
def delete_investor_project_view(request, pk, investment_id):
    project = get_object_or_404(InvestorProject, UserId=pk, investment_id=investment_id)

    # if request.method == 'PUT':
    #     data = request.data
    #     update_investor_project(project, data)
    #     serializer = InvestorProjectSerializers(project, many=False)
    #     return Response(serializer.data)

    if request.method == 'DELETE':
        project.delete()
        return Response({'message': 'Investor project deleted successfully'}, status=204)
#get all the investor projects
@api_view(['GET'])
def getInvestorProjects(request):
    notes = InvestorProject.objects.all()
    serializer = InvestorProjectSerializers(notes,many = True)
    return Response(serializer.data) 



#for sending notifications

# views.py
from push_notifications.models import GCMDevice
@api_view(['POST'])
def send_push_notification(request):
    # Get all registered devices
    devices = GCMDevice.objects.all()

    # Customize the congratulations message
    congratulations_title = "Congratulations!"
    congratulations_body = "Your account has been created successfully. Welcome aboard!"

    # Send push notification to all devices with the customized message
    for device in devices:
        device.send_message(congratulations_title, congratulations_body)

    return JsonResponse({"status": "success"})
