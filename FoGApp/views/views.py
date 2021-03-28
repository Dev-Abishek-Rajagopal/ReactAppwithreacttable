'''
Created on 27-MAR-2021

@author: Abishek Rajagopal
'''

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import api_view
from FoGApp.models import (Green_Business,Green_Owner)
from FoGApp.serializers.serializers import (UserSerializer,Green_OwnerSerializer,Green_OwnerSerializerI,
Green_OwnerSerializerII, Green_OwnerSerializerIII, Green_OwnerSerializerforPUT, Green_BusinessSerializer,
Green_BusinessSerializerI, Green_BusinessSerializerforPut)
from django.contrib.auth.models import User
from rest_framework.response import Response
import logging
from FoGApp.views.process import (smtpsender,smtpsenderBiz)
import json
import requests 
import requests

logger = logging.getLogger("fog.request")

@api_view(['POST'])
def create_Owner(request):
    try:
        validated_data = {}
        validated_data = request.data.copy()
        validated_data['username'] = request.data['username'].lower()
        validated_data['email'] = request.data['email'].lower()
        validated_data['country'] = request.data['country'].lower()
        validated_data['city'] = request.data['city'].lower()

        User_list = User.objects.all()
        for i in User_list:
            if i.username == validated_data['username']:
                return Response("Username already exist", status=404)
            if i.email == validated_data['email']:
                return Response("Email already exit", status=404)

        serializer = UserSerializer(data=validated_data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=200)

        logger.info(serializer.data["username"])

        list = User.objects.get(username=serializer.data["username"])
        datas = request.data.copy()
        datas["user"] = list.id

        serializer = Green_OwnerSerializer(data=datas)
        # logger.info("jay")
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data.copy()
            datas["message"] = "A verification mail will be sent to mail id to activate your account."
            smtpsenderBiz(datas, list.id)
            return Response(datas, status=200)
        else:
            return Response(serializer.errors, status=200)
        return Response(serializer.errors, status=200)

        # return Response(serializer.errors, status=200)
    except Exception as e:
        logger.info("Error")
        logger.info(str(e))
        return Response(str(e), status=200)


@api_view(['POST'])
def create_Business(request):
    try:
        validated_data = {}
        validated_data = request.data.copy()
        validated_data['landmark'] = request.data['landmark'].lower()
        validated_data['email'] = request.data['email'].lower()
        validated_data['country'] = request.data['country'].lower()
        validated_data['city'] = request.data['city'].lower()



        serializer = Green_BusinessSerializer(data=validated_data)
        # logger.info("jay")
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data.copy()
            datas["message"] = "A verification mail will be sent to mail id to activate your account."
            smtpsenderBiz(datas, serializer.data['id'])
            return Response(datas, status=200)
        else:
            return Response(serializer.errors, status=200)
        return Response(serializer.errors, status=200)

        # return Response(serializer.errors, status=200)
    except Exception as e:
        logger.info("Error")
        logger.info(str(e))
        return Response(str(e), status=200)


class Green_OwnerVeiwSet(ModelViewSet):

    queryset = Green_Owner.objects.all()
    serializer_class = Green_OwnerSerializer


    def list_User(self, request):
        try:
            App_User_list = Green_Owner.objects.all()
            serializer = Green_OwnerSerializer(App_User_list, many=True)
            # logger.info("hi")
            # for i in serializer.data:
            #     image_data =""
            #     with open(i['dp'], "rb") as image_file:
            #         image_data = base64.b64encode(image_file.read()).decode('utf-8')
            #     i['dp']= image_data
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)



    def get_User(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = Green_Owner.objects.get(id=pk)
            serializer = Green_OwnerSerializer(list)

            datas = serializer.data.copy()

            return Response(datas, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


    def delete_User(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = Green_Owner.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Owner deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_User(self, request, *args, **kwargs):
        try:
            serializer = Green_OwnerSerializerforPUT(data=request.data)
            pk = self.kwargs['pk']
            item = Green_Owner.objects.get(id=pk)
            logger.info("in views")
            if serializer.is_valid():
                logger.info("valid")
                serializer.update(item, serializer.data)
            else:
                return Response(serializer.errors, status=200)
            pk = self.kwargs['pk']
            list = Green_Owner.objects.get(id=pk)
            serializer = Green_OwnerSerializer(list)
            return Response(serializer.data, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


class Green_BusinessVeiwSet(ModelViewSet):

    queryset = Green_Business.objects.all()
    serializer_class = Green_BusinessSerializer


    def list_business(self, request):
        try:
            App_User_list = Green_Business.objects.all()
            serializer = Green_BusinessSerializer(App_User_list, many=True)
            # logger.info("hi")
            # for i in serializer.data:
            #     image_data =""
            #     with open(i['dp'], "rb") as image_file:
            #         image_data = base64.b64encode(image_file.read()).decode('utf-8')
            #     i['dp']= image_data
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)



    def get_business(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = Green_Business.objects.get(id=pk)
            serializer = Green_BusinessSerializer(list)

            datas = serializer.data.copy()

            return Response(datas, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


    def delete_business(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = Green_Business.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Owner deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_business(self, request, *args, **kwargs):
        try:
            serializer = Green_BusinessSerializerforPut(data=request.data)
            pk = self.kwargs['pk']
            item = Green_Business.objects.get(id=pk)
            logger.info("in views")
            if serializer.is_valid():
                logger.info("valid")
                serializer.update(item, serializer.data)
            else:
                return Response(serializer.errors, status=200)
            pk = self.kwargs['pk']
            list = Green_Owner.objects.get(id=pk)
            serializer = Green_OwnerSerializer(list)
            return Response(serializer.data, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


@api_view(['GET'])
def Get_Business(request):
    try:
        query = ["agriculture+in+chatham+kent","greenhouse+in+chatham+kent","greenhouse+in+Tilbury","agriculture+in+Tilbury","agriculture+in+windsor+Essex"]
        API = "AIzaSyDRk_82nVafWTtDXyQuhAzc6ROWPBC9LlY"
        responsearr =[]
        for i in range(0,len(query)):
            url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + query[i] + "&key=" + API
            response = requests.get(url).json()
            arr = response["results"]
            for j in arr:
                url1 = "https://maps.googleapis.com/maps/api/place/details/json?place_id="+ j["place_id"] + "&fields=name,rating,formatted_phone_number,type,website,opening_hours,international_phone_number,photo,price_level,review,url,utc_offset,vicinity&key=" + API
                response1 = requests.get(url1).json()
                j["placeJson"] = response1
                j["iframe"] = "https://www.google.com/maps/embed/v1/place?key=" + API + "&q=" + j["name"]
                responsearr.append(j)
        return Response(responsearr, status=200)
    except Exception as e:
        logger.info("Error")
        logger.info(str(e))
        return Response(str(e), status=200)
