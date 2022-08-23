from . models import Product
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields ='__all__'
        
    # def to_representation(self, instance):
    #     rep = super(JobSkillSerializer, self).to_representation(instance)
    #     rep['job'] = f'{instance.job.company.company_name} - {instance.job.title}' 
    #     rep['skill'] = instance.skill.name
    #     return rep

   