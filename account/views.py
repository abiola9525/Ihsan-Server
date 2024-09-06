from django.conf import settings
from django.shortcuts import render
from web3 import Web3
import os
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework import status, serializers
import random
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.template.loader import render_to_string
from django.core.mail import send_mail
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

from account.models import User
from . serializers import MyTokenObtainPairSerializer, UserSerializer, ResetPasswordSerializer, UpdateUserSerializer, ChangePasswordSerializer, ForgotPasswordSerializer
# ResetPasswordSerializer, UpdateUserSerializer, ChangePasswordSerializer, ForgotPasswordSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
import uuid


def email_veri(request):
    return render(request, 'confirmation_email.html') 



INFURA_PROJECT_ID =  os.environ['INFURA_PROJECT_ID']

w3 = Web3(Web3.HTTPProvider(f'https://arbitrum-sepolia.infura.io/v3/{INFURA_PROJECT_ID}'))

# w3 = Web3(Web3.HTTPProvider(f'https://arbitrum-mainnet.infura.io/v3/{INFURA_PROJECT_ID}'))

def create_blockchain_account():
    account = w3.eth.account.create()
    return account.address


@swagger_auto_schema(method='POST', request_body=UserSerializer)
@api_view(['POST'])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def register_user(request):
    data = request.data

    user_serializer = UserSerializer(data=data)
    if user_serializer.is_valid(raise_exception=True):
        # Generate a blockchain address for the user
        blockchain_address = create_blockchain_account()
        
        user = user_serializer.save(blockchain_address=blockchain_address)

        # Generate a random 4-digit confirmation code
        confirmation_code = ''.join([str(random.randint(0, 9)) for _ in range(4)])

        # Save the code in the user's profile
        user.confirmation_code = confirmation_code
        user.eval_test = False
        user.save()

        # Send confirmation code via email
        email_subject = 'Confirm Your Email'
        email_message = render_to_string('confirmation_email.html', {'confirmation_code': confirmation_code})
        
        send_mail(
            email_subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
            html_message=email_message,  
        )
    
        return Response({
                'message': 'Confirmation code sent successfully.',
                'user': user_serializer.data,
            }, status=status.HTTP_201_CREATED)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def confirm_email(request):
    confirmation_code = request.data.get('confirmation_code')

    if not confirmation_code:
        return JsonResponse({'message': 'Confirmation code is missing from the request.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(confirmation_code=confirmation_code, is_active=False)
        user.is_active = True
        user.confirmation_code = ""
        user.save()
        return JsonResponse({'message': 'Email confirmation successful.'})
    except User.DoesNotExist:
        return JsonResponse({'message': 'Invalid confirmation code.'}, status=status.HTTP_400_BAD_REQUEST)




class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    
@api_view(['PUT'])
def update_user_status(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    user.eval_test = True
    user.save()
    return Response({'message': 'User evaluation test status updated to "True"'})
