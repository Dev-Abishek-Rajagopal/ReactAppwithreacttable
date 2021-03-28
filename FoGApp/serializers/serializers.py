'''
Created on 27-MAR-2021

@author: Abishek Rajagopal
'''


from rest_framework import serializers

from FoGApp.models import (Green_Business,Green_Owner)
from django.contrib.auth.models import User
import logging

logger = logging.getLogger("fog.request")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User;
        fields = ("id", 'username', 'first_name', 'last_name', 'email', "password")

    def create(self, validated_data):
        try:
            validated_data['username'] = validated_data['username'].lower()
            validated_data['email'] = validated_data['email'].lower()

            user = User.objects.create(**validated_data);
            logger.info(user)
            return user

        except Exception as e:
            logger.info("Error")
            logger.info('jiji')
            logger.info(str(e))

    def update(self, instance, validated_data):
        try:
            validated_data['username'] = validated_data['username'].lower()
            validated_data['email'] = validated_data['email'].lower()

            instance.id = validated_data.get('id', instance.id);
            instance.first_name = validated_data.get('first_name', instance.first_name);
            instance.last_name = validated_data.get('last_name', instance.last_name);
            instance.password = validated_data.get('password', instance.password);
            instance.email = validated_data.get('email', instance.email);

            instance.save();
            return instance;

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


class Green_OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Green_Owner;
        fields = (
        'id', 'user', 'first_name', 'active', 'last_name', 'username', 'password', 'country' , 'city', 'email',"contact",
        'FB_link', 'Twitter_link', 'Insta_link', 'Twitter_link', 'Linkedin_link', 'social_media', 'social_media_link', 'privacy_info', 'dp');

    def create(self, validated_data):
        try:
            validated_data['username'] = validated_data['username'].lower()
            validated_data['country'] = validated_data['country'].lower()
            validated_data['country'] = validated_data['country'].lower()
            validated_data['city'] = validated_data['city'].lower()
            user = Green_Owner.objects.create(**validated_data);
            return user

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))



class Green_OwnerSerializerI(serializers.ModelSerializer):
    class Meta:
        model = Green_Owner;
        fields = (
        'id', 'first_name', 'last_name', 'username', 'country' , 'city', 'email',"contact",
        'FB_link', 'Twitter_link', 'Insta_link', 'Twitter_link', 'Linkedin_link', 'social_media', 'social_media_link', 'dp','publist');

    def create(self, validated_data):
        try:
            validated_data['username'] = validated_data['username'].lower()
            validated_data['country'] = validated_data['country'].lower()
            validated_data['country'] = validated_data['country'].lower()
            validated_data['city'] = validated_data['city'].lower()
            user = Green_Owner.objects.create(**validated_data);
            return user

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


class Green_OwnerSerializerII(serializers.ModelSerializer):
    class Meta:
        model = Green_Owner;
        fields = (
        'id', 'first_name', 'last_name', 'username', 'country' , 'city',
        'FB_link', 'Twitter_link', 'Insta_link', 'Twitter_link', 'Linkedin_link', 'social_media', 'social_media_link', 'dp','publist');

    def create(self, validated_data):
        try:
            validated_data['username'] = validated_data['username'].lower()
            validated_data['country'] = validated_data['country'].lower()
            validated_data['country'] = validated_data['country'].lower()
            validated_data['city'] = validated_data['city'].lower()
            user = Green_Owner.objects.create(**validated_data);
            return user

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


class Green_OwnerSerializerIII(serializers.ModelSerializer):
    class Meta:
        model = Green_Owner;
        fields = (
        'id', 'first_name', 'last_name', 'username', 'country' , 'city', 'dp','publist');

    def create(self, validated_data):
        try:
            validated_data['username'] = validated_data['username'].lower()
            validated_data['country'] = validated_data['country'].lower()
            validated_data['country'] = validated_data['country'].lower()
            validated_data['city'] = validated_data['city'].lower()
            user = Green_Owner.objects.create(**validated_data);
            return user

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))



class Green_OwnerSerializerforPUT(serializers.ModelSerializer):

        class Meta:
            model = Green_Owner;
            fields = ('id', 'user', 'first_name', 'active', 'last_name', 'password', 'country', 'city',
                "contact",'FB_link', 'Twitter_link', 'Insta_link', 'Twitter_link', 'Linkedin_link', 'social_media',
                      'social_media_link', 'privacy_info', 'dp');

        def update(self, instance, validated_data):
            try:
                validated_data['username'] = validated_data['username'].lower()
                validated_data['country'] = validated_data['country'].lower()
                validated_data['country'] = validated_data['country'].lower()
                validated_data['city'] = validated_data['city'].lower()

                instance.id = validated_data.get('id', instance.id);
                instance.first_name = validated_data.get('first_name', instance.first_name);
                instance.last_name = validated_data.get('last_name', instance.last_name);

                instance.usertype = validated_data.get('usertype', instance.usertype);
                instance.password = validated_data.get('password', instance.password);
                instance.country = validated_data.get('country', instance.country);
                instance.city = validated_data.get('city', instance.city);

                instance.contact = validated_data.get('contact', instance.contact);

                instance.FB_link = validated_data.get('FB_link', instance.FB_link);
                instance.Twitter_link = validated_data.get('Twitter_link', instance.Twitter_link);
                instance.Insta_link = validated_data.get('Insta_link', instance.Insta_link);
                instance.Linkedin_link = validated_data.get('Linkedin_link', instance.Linkedin_link);
                instance.social_media = validated_data.get('social_media', instance.social_media);
                instance.social_media_link = validated_data.get('social_media_link', instance.social_media_link);

                instance.privacy_info = validated_data.get('privacy_info', instance.privacy_info);
                instance.dp = validated_data.get('dp', instance.dp);
                instance.save();

                return instance;
            except Exception as e:
                logger.info("Error")
                logger.info(str(e))


class Green_BusinessSerializer(serializers.ModelSerializer):


    class Meta:
        model = Green_Business;
        fields = ("id", 'name', 'Website', 'Address', 'city', 'country','landmark','pincode','maplocation','dp',
                  "owner", 'desc', 'email', 'contact', 'FB_link', 'Twitter_link', 'Insta_link', 'Twitter_link', 'Linkedin_link', 'social_media',
                      'social_media_link', 'active', 'BusinessFrom');

    def create(self, validated_data):
        try:
            return Green_Business.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))

class Green_BusinessSerializerI(serializers.ModelSerializer):


    class Meta:
        model = Green_Business;
        fields = ("id", 'name', 'Website', 'Address', 'city', 'country','landmark','pincode','maplocation','dp',
                  "owner", 'desc', 'email', 'contact', 'FB_link', 'Twitter_link', 'Insta_link', 'Twitter_link', 'Linkedin_link', 'social_media',
                      'social_media_link', 'active', 'BusinessFrom', "publist");

    def create(self, validated_data):
        try:
            return Green_Business.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))

class Green_BusinessSerializerforPut(serializers.ModelSerializer):


    class Meta:
        model = Green_Business;
        fields = ("id", 'name', 'Website', 'Address', 'city', 'country','landmark','pincode','maplocation','dp',
                 'desc', 'contact', 'FB_link', 'Twitter_link', 'Insta_link', 'Twitter_link', 'Linkedin_link', 'social_media',
                'social_media_link', 'active', 'BusinessFrom');

    def create(self, validated_data):
        try:
            return Green_Business.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))

    def update(self, instance, validated_data):
        try:
            validated_data['landmark'] = validated_data['landmark'].lower()
            validated_data['country'] = validated_data['country'].lower()
            validated_data['country'] = validated_data['country'].lower()
            validated_data['city'] = validated_data['city'].lower()

            instance.id = validated_data.get('id', instance.id);
            instance.name = validated_data.get('name', instance.name);
            instance.Website = validated_data.get('Website', instance.Website);

            instance.type = validated_data.get('type', instance.type);
            instance.Address = validated_data.get('Address', instance.Address);
            instance.country = validated_data.get('country', instance.country);
            instance.city = validated_data.get('country', instance.country);

            instance.dp = validated_data.get('dp', instance.dp);
            instance.desc = validated_data.get('desc', instance.desc);

            instance.contact = validated_data.get('contact', instance.contact);

            instance.FB_link = validated_data.get('FB_link', instance.FB_link);
            instance.Twitter_link = validated_data.get('Twitter_link', instance.Twitter_link);
            instance.Insta_link = validated_data.get('Insta_link', instance.Insta_link);
            instance.Linkedin_link = validated_data.get('Linkedin_link', instance.Linkedin_link);
            instance.social_media = validated_data.get('social_media', instance.social_media);
            instance.social_media_link = validated_data.get('social_media_link', instance.social_media_link);

            instance.BusinessFrom = validated_data.get('BusinessFrom', instance.BusinessFrom);

            instance.save();

            return instance;
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


