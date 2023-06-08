from rest_framework import serializers 
from bankdetails.models import Bankdetails, Updaterequests, UsersList
 
 
class BankdetailsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Bankdetails
        fields = ('id',
                  'email',
                  'account_holder_name',
                  'account_number',
                  'ifsc_code',
                  'bank_name',
                  'branch_name')
        
 
class UpdaterequestsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Updaterequests
        fields = ('id',
                  'email',
                  'account_holder_name',
                  'account_number',
                  'ifsc_code',
                  'bank_name',
                  'branch_name')
        
 
class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = UsersList
        fields = ('id',
                  'email',
                  'password')