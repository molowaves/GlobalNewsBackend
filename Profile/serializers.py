from rest_framework import serializers
from .models import User, Reader, Journalist

class UserSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(max_length=100, style={'input_type':'password'}, write_only=True)
	class Meta:
		model = User
		fields = ['username', 'email', 'user_type', 'password', 'password2']
		extra_kwargs = {
			'password':{'write_only': True}
		}

	def save(self, request):
		user = User(username=self.validated_data['username'], 
					email=self.validated_data['email'], 
					user_type=self.validated_data['user_type']
					)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']

		if password != password2:
			raise serializers.ValidationError({'non_field_errors': ['Passwords not matched!']})
		user.set_password(password)
		user.save()
		return user


class ReaderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reader
		fields = '__all__'


class JournalistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Journalist
		fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['email', 'user_type', 'pk']
		







