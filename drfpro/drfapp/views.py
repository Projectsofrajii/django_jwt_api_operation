from datetime import datetime
from django.http import Http404

from rest_framework import viewsets, status, views, exceptions, response
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import RsmRoleMaster,RsmUserMaster
from .serializers import RsmRoleMasterSeri,RsmUserMasterSeri,RsmUserUpdateSeri
from .import serializers as user_serializer
from .import services

class RsmRole(viewsets.ModelViewSet):
    queryset = RsmRoleMaster.objects.all()
    serializer_class = RsmRoleMasterSeri

class RsmUser(viewsets.ModelViewSet):
    queryset = RsmUserMaster.objects.all()
    serializer_class = RsmUserMasterSeri

class Rolegetall(views.APIView):

    def get(self, request, format=None):
        queryset = RsmRoleMaster.objects.all()
        serializer = RsmRoleMasterSeri(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_302_FOUND)

class Usergetall(views.APIView):

    def get(self, request, format=None):
        queryset = RsmUserMaster.objects.all()
        serializer = RsmUserMasterSeri(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_302_FOUND)

class RoleCreate(APIView):

    def post(self, request, format=None):
        serializer = RsmRoleMasterSeri(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Data': serializer.data, 'Message': 'Record Created Successfully'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCreate(views.APIView):
    def post(self, request, format=None):
        serializer = RsmUserMasterSeri(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Data': serializer.data, 'Message': 'Record Created Successfully'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoleGet(views.APIView):

    def get(self, request, pk, format=None):
        queryset = (RsmRoleMaster.objects.get(role_id=pk))
        serializer = RsmRoleMasterSeri(queryset, many=False)
        return Response(serializer.data,status=status.HTTP_302_FOUND)

class UserGet(views.APIView):

    def get(self, request, pk, format=None):
        queryset = RsmUserMaster.objects.get(user_id=pk)
        serializer = RsmUserMasterSeri(queryset, many=False)
        if not serializer :
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data,status=status.HTTP_302_FOUND)

class RoleUpdate(views.APIView):
    def get_object(self, pk):
        try:
            return RsmRoleMaster.objects.get(pk=pk)
        except RsmUserMaster.DoesNotExist:
            raise Http404

    def patch(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RsmRoleMasterSeri(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Data':serializer.data,'Message':'Updated Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdate(views.APIView):

    def get_object(self, pk):
        try:
            return RsmUserMaster.objects.get(pk=pk)
        except RsmUserMaster.DoesNotExist:
            raise Http404

    def patch(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RsmUserUpdateSeri(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Data':serializer.data,'Message':'Updated Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoleDelete(views.APIView):
    serializer = RsmRoleMasterSeri

    def get_object(self, pk):
        try:
            return RsmRoleMaster.objects.get(pk=pk)
        except RsmRoleMaster.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = (RsmRoleMaster.objects.get(role_id=pk))
        serializer = RsmRoleMasterSeri(queryset, many=False)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserDelete(views.APIView):
    serializer = RsmUserMasterSeri

    def get_object(self, pk):
        try:
            return RsmUserMaster.objects.get(pk=pk)
        except RsmUserMaster.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = RsmUserMaster.objects.get(user_id=pk)
        serializer = RsmUserMasterSeri(queryset, many=False)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
class RegisterUserApi(views.APIView):

    def post(self,request):
        try:
            serializer = user_serializer.RsmUserMasterSeri(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            # User.objects.update(is_admin="0")
            serializer.instance = serializer.create(data)
            return Response({'User': serializer.data, 'message': ' Registered Successfully'},
                            status=status.HTTP_201_CREATED)
            # return Response(data=,status=status.HTTP_201_CREATED)
        except Exception as e:
            raise e
class RoleCreate(APIView):

    def post(self, request, format=None):
        serializer = RsmRoleMasterSeri(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Data': serializer.data, 'Message': 'Record Created Successfully'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCreate(views.APIView):
    def post(self, request, format=None):
        serializer = RsmUserMasterSeri(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Data': serializer.data, 'Message': 'Record Created Successfully'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUserApi(views.APIView):
    serializer_classess = RsmUserMasterSeri
    def post(self,request):
        email = request.data["email_id"]
        password = request.data["password"]
        user = services.user_email_selector(email_id=email)
        users = RsmUserMaster.objects.get(email_id=email)

        if user is None:
            raise exceptions.AuthenticationFailed({"Message": "Invalid EmailID"})

        if not users.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Password not matched")

        RsmUserMaster.objects.filter(email_id=email).update(last_login=datetime.now())
        RsmUserMaster.objects.filter(email_id=email).update(status="1")

        token = services.create_token(email_id=user.email_id)
        resp = response.Response({'access_token': token, 'Message': 'Login Successfully'})
        resp.set_cookie(key="jwt", value=token, httponly=True)
        RsmUserMaster.objects.filter(email_id=email).update(access_token=token)
        return resp

class LogoutUserApi(views.APIView):
    def post(self,request):
        try:
            email = request.data["email_id"]
            resp = response.Response()
            resp.delete_cookie("jwt")
            RsmUserMaster.objects.filter(email_id=email).update(status="0")
            RsmUserMaster.objects.filter(email_id=email).update(last_loupdated_timestampgin=datetime.now())
            RsmUserMaster.objects.filter(email_id=email).update(access_token="Token Expired ")

            resp.data = {"message": "Logout Successfully.."}
            return resp

        except Exception as e:
            raise e
'''