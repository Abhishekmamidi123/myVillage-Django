from rest_framework import serializers

from server import models

class houseSerializer(serializers.ModelSerializer):
	class Meta:
        	model = models.house
        	# fields = ('ticker', 'volume')
        	fields = '__all__'
        	
class memberSerializer(serializers.ModelSerializer):
	class Meta:
        	model = models.member
        	fields = '__all__'

class housePhotoSerializer(serializers.ModelSerializer):
	class Meta:
        	model = models.housePhoto
        	fields = '__all__'

class houseAudioSerializer(serializers.ModelSerializer):
	class Meta:
        	model = models.houseAudio
        	fields = '__all__'

class farmSerializer(serializers.ModelSerializer):
	class Meta:
        	model = models.farm
        	fields = '__all__'

class pointSerializer(serializers.ModelSerializer):
	class Meta:
        	model = models.point
        	fields = '__all__'

class cropSerializer(serializers.ModelSerializer):
	class Meta:
        	model = models.crop
        	fields = '__all__'

class seasonSerializer(serializers.ModelSerializer):
	class Meta:
        	model = models.season
        	fields = '__all__'

class croppingSerializer(serializers.ModelSerializer):
	class Meta:
        	model = models.cropping
        	fields = '__all__'

class farmPhotoSerializer(serializers.ModelSerializer):
	class Meta:
        	model = models.farm
        	fields = '__all__'

class farmAudioSerializer(serializers.ModelSerializer):
	class Meta:
        	model = models.farmAudio
        	fields = '__all__'

class wellSerializer(serializers.ModelSerializer):
	class Meta:
        	model = models.well
        	fields = '__all__'
		
class dateTimeSerializer(serializers.ModelSerializer):
	class Meta:
        	model = models.dateTime
        	fields = '__all__'
        	
class wellPhotoSerializer(serializers.ModelSerializer):
	class Meta:
        	model = models.wellPhoto
        	fields = '__all__'

class wellAudioSerializer(serializers.ModelSerializer):
	class Meta:
        	model = models.wellAudio
        	fields = '__all__'
class graphColorsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.graphColors
		fields = '__all__'
class weatherSerializer(serializers.ModelSerializer):
        class Meta:
                model = models.weather
                fields = '__all__'

