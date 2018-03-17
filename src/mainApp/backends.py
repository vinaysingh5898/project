from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailBackend(object):
    def authenticate(self, username=None, password=None):
        UserModel = get_user_model()
        # print("usermodelnot")
        # if not UserModel:
        try:
            user = UserModel.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                # print(password)
                return None
        except UserModel.DoesNotExist:
            # print("usermodelnot")
            return None
        # else:
            # if user.check_password(password):
                # return user
        return None
    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

