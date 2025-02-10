from rest_framework import serializers

from socialapp.models import Profile, User,Post,Comment


class UserSerializer(serializers.ModelSerializer):

    password1=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)
    
    class Meta:
        
        model=User
        
        fields=["id","username","phone","email","password","password1","password2"]
        
        read_only_fields=["id","password"]

    def create(self, validated_data):
       
        password1=validated_data.pop('password1')
        
        password2=validated_data.pop('password2')
        
        if password1!=password2:
            
            raise serializers.ValidationError("password mismatch")
        
        
        return User.objects.create_user(**validated_data,password=password1)
    
    
class PostSerializer(serializers.ModelSerializer):

    owner=serializers.StringRelatedField(read_only=True)

    liked_by=serializers.StringRelatedField(read_only=True,many=True)
    
    class Meta:

        model=Post

        fields="__all__"

        read_only_fields=["id","owner","created_at","updated_at","liked_by"]
        
        
    def get_like_count(self,obj):
        
        return obj.liked_by.all().count()
    
    
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model=Comment
        
        fields="__all__"
        
        read_only_fields=["id","post","owner","created_at"]
        
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model=Profile

        fields="__all__"

        read_only_fields=["id","owner"]
