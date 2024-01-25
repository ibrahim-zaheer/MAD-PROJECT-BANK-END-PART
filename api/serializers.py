from rest_framework import serializers

from .models import Notes,UserProfileAfterLogin,UserProfileBeforeLogin,ProperProfileCreation,EntrepreneurProfile,Project,InvestorProject

class NotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'

class BeforeLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfileBeforeLogin
        fields = '__all__'        

class AfterLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfileAfterLogin
        fields = '__all__'



class ProperProfileCreationSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProperProfileCreation
        fields = '__all__'


class EntrepreneurProfileCreationSerializers(serializers.ModelSerializer):
    class Meta:
        model = EntrepreneurProfile
        fields = '__all__'  

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__' 



class InvestorProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = InvestorProject
        fields = '__all__'                        
