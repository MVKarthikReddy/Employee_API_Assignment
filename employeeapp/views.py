from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from employeeapp.serializers import UserRegistrationSerializer,UserLoginSerializer,UserProfileSerializer
from django.contrib.auth import authenticate
from employeeapp.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated




def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return{
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    }

# @desc Register the user
# @route POST /api/users/register/
# @access public

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            # token = get_tokens_for_user(user)
            return Response({ 'msg' : 'Registration Successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @desc Login the user
# @route POST /api/users/login/
# @access public

class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token, 'msg' : 'Login Success'},status=status.HTTP_200_OK)
            else:
                return Response({'errors' : {"non_field_errors":["Email or Password is not valid"]} },status=status.HTTP_404_NOT_FOUND)

# @desc Profile of the user
# @route GET /api/users/profile/
# @access private

class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        serializer = UserProfileSerializer(request.user)
        print(serializer.data['id'])
        return Response(serializer.data, status=status.HTTP_200_OK)

