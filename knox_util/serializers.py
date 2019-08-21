from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

username_field = User.USERNAME_FIELD if hasattr(User, 'USERNAME_FIELD') else 'username'

email_field = User.IS_STAFF if hasattr(User, 'IS_STAFF') else 'is_staff'

# customize .... with email stuff ....  and image jpg ... 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (username_field, email_field)