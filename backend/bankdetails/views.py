from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from bankdetails.models import Bankdetails, Updaterequests, UsersList
 
from bankdetails.serializers import BankdetailsSerializer, UpdaterequestsSerializer, UserSerializer

from rest_framework.decorators import api_view


@api_view(['POST'])
def users_login(request):
    users_data = JSONParser().parse(request)
    username = users_data.get("email")
    password = users_data.get("password")
    try: 
        user = UsersList.objects.get(email=username) 
    except UsersList.DoesNotExist: 
        return JsonResponse({'message': 'Email does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    users_serializer = UserSerializer(user) 

    # print(password)
    
    # print(users_serializer.data.get("password"))
    if password == users_serializer.data.get("password"):
        # true0 - no entry in bankdetails
        # true1 - update allowed
        # true2 - no update allowed
        try: 
            bankdetails = Bankdetails.objects.get(email=username) 
        except Bankdetails.DoesNotExist: 
            return JsonResponse({'password': 'true0'})
        
        if bankdetails.update_allowed == True:
            return JsonResponse({'password': 'true1','id':bankdetails.pk})
        bankdetails_serializer = BankdetailsSerializer(bankdetails)
        return JsonResponse({'password': 'true2', 'bankdetails': bankdetails_serializer.data})
    
        # return JsonResponse({'password': 'true2'})
    
    return JsonResponse({'password': 'false'}, status=status.HTTP_409_CONFLICT)

@api_view(['GET','POST'])
def users_list(request):
    if request.method == 'GET':
        Users = UsersList.objects.all()     
        users_serializer = UserSerializer(Users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    
    elif request.method == 'POST':
        users_data = JSONParser().parse(request)
        email = users_data.get("email")
        
        try: 
            old_data = UsersList.objects.get(email=email)
            return JsonResponse({'message': 'Email already exists'}, status=status.HTTP_409_CONFLICT)
        except UsersList.DoesNotExist: 
            users_serializer = UserSerializer(data=users_data)
            if users_serializer.is_valid():
                users_serializer.save()
                return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED)
        # if UsersList.objects.get(email=email):
        #     print("1")
        #     return JsonResponse({'message': 'Email already exists'}, status=status.HTTP_409_CONFLICT)
        # else:
        #     print("11")
        #     users_serializer = UserSerializer(data=users_data)
        #     if users_serializer.is_valid():
        #         users_serializer.save()
        #         return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def bankdetails_list(request):
    if request.method == 'GET':
        bankdetails = Bankdetails.objects.all()
        bankdetails_serializer = BankdetailsSerializer(bankdetails, many=True)
        return JsonResponse(bankdetails_serializer.data, safe=False)
    
    elif request.method == 'POST':
        bankdetails_data = JSONParser().parse(request)
        username = bankdetails_data.get("email")
        try: 
            user = Bankdetails.objects.get(email=username) 
            return JsonResponse({'message': 'Bank details already exists'}, status=status.HTTP_409_CONFLICT)
        except Bankdetails.DoesNotExist: 
            bankdetails_serializer = BankdetailsSerializer(data=bankdetails_data)
            if bankdetails_serializer.is_valid():
                bankdetails_serializer.save()
                return JsonResponse(bankdetails_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(bankdetails_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def bankdetails_detail(request, pk):
    try: 
        bankdetails = Bankdetails.objects.get(pk=pk) 
    except Bankdetails.DoesNotExist: 
        return JsonResponse({'message': 'Bank details does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        bankdetails_serializer = BankdetailsSerializer(bankdetails) 
        return JsonResponse(bankdetails_serializer.data) 
        
    elif request.method == 'DELETE': 
        bankdetails.delete() 
        return JsonResponse({'message': 'Bank details was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        
        new_data = JSONParser().parse(request)
        if bankdetails.update_allowed == False:
            return JsonResponse({'message': 'Maximum attempts reached!'}, status=status.HTTP_400_BAD_REQUEST)
        bankdetails.update_allowed = False
        bankdetails_serializer = BankdetailsSerializer(data=bankdetails)
        if bankdetails_serializer.is_valid():
            bankdetails_serializer.save()
        
        username = new_data.get("email")
        try: 
            user = Updaterequests.objects.get(email=username) 
            return JsonResponse({'message': 'Update Pending'}, status=status.HTTP_400_BAD_REQUEST) 

        except Updaterequests.DoesNotExist: 
            Updaterequests_serializer = UpdaterequestsSerializer(data=new_data)
            if Updaterequests_serializer.is_valid():
                Updaterequests_serializer.save()
                return JsonResponse(Updaterequests_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(Updaterequests_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        return JsonResponse({'message': 'Bank details !'})
        # if Updaterequests_serializer.is_valid():
        #     Updaterequests_serializer.save()
        #     return JsonResponse(Updaterequests_serializer.data, status=status.HTTP_201_CREATED) 
        # return JsonResponse(Updaterequests_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # return JsonResponse({'message': 'Bank details !'})
        # try: 
        #     details = Bankdetails.objects.get(email=email) 
        # except Bankdetails.DoesNotExist: 
        #     return JsonResponse({'message': 'Email does not exist'}, status=status.HTTP_404_NOT_FOUND) 

        # bankdetails_serializer = BankdetailsSerializer(details) 
        # print(bankdetails_serializer.data)
        # if bankdetails_serializer.data.get("update_allowed")=='false':
        #     return JsonResponse({'CanUpdate': 'false'})
        # Updaterequests_serializer = UpdaterequestsSerializer(data=bankdetails_data)
        # if Updaterequests_serializer.is_valid():
        #     Updaterequests_serializer.save()
        #     bankdetails_serializer.data["update_allowed"] = "false"
        #     return JsonResponse(Updaterequests_serializer.data, status=status.HTTP_201_CREATED) 
        # return JsonResponse(Updaterequests_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # bankdetails_data = JSONParser().parse(request) 
        # bankdetails_serializer = BankdetailsSerializer(bankdetails, data=bankdetails_data) 
        # if bankdetails_serializer.is_valid(): 
        #     bankdetails_serializer.save() 
        #     return JsonResponse(bankdetails_serializer.data) 
        # return JsonResponse(bankdetails_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','POST'])
def updates_list(request):
    if request.method == 'GET': 
        updates = Updaterequests.objects.all()    
        updates_serializer = UpdaterequestsSerializer(updates, many=True)
        return JsonResponse(updates_serializer.data, safe=False)
    
    if request.method == 'POST': 
        new_data = JSONParser().parse(request)
        new_data.pop('id', None)
        email = new_data.get("email")
        try: 
            old_data = Bankdetails.objects.get(email=email) 
        except Bankdetails.DoesNotExist: 
            return JsonResponse({'message': 'Email does not exist'}, status=status.HTTP_404_NOT_FOUND) 

        bankdetails_serializer = BankdetailsSerializer(old_data, data=new_data) 
        if bankdetails_serializer.is_valid(): 
            bankdetails_serializer.save() 
            Updaterequests.objects.filter(email=email).delete()
            return JsonResponse(bankdetails_serializer.data) 
        return JsonResponse(bankdetails_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

