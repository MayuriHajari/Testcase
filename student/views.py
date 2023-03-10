import re
from django.http import JsonResponse
from rest_framework.views import APIView
from student.models.student_model import Student
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
class StudentView(APIView):
    
    def get(self, request):
        try:
          queryset = Student.objects.all()
          return JsonResponse(list(queryset.values()), safe=False)
      
        except ValidationError as e:
            data = {'status':'error','error_code': 103, 'message': "error: {0} ".format(e)}
            return JsonResponse(data)
        
        except Exception as e:
            data = {'status':'error','error_code': 101, 'message': "error: {0}".format(e)}      
            return JsonResponse(data)
       
    def post(self, request): 
        def validate_name(name):
           if not all(char.isalpha() or char.isspace() for char in name):
               return False
           return True  
        
        try:       
            data = {}
            data['student_name'] =request.POST.get('name')
            data['mail_id'] =request.POST.get('mail_id')
            if not validate_name(data['student_name']):
                 raise ValidationError('Name is not valid')
            else: 
              validate_email( data['mail_id'])
            student = Student.objects.create(**data)
            
            return JsonResponse({'data':data},status=status.HTTP_201_CREATED) 
        except ValidationError as e:
            data = {'status':'error','error_code': 103, 'message': "error: {0} ".format(e)}
            return JsonResponse(data)        
        except NameError as e:
            data = {'status':'error','error_code': 103, 'message': "error: {0} ".format(e)}
            return JsonResponse(data)
        except Exception as e:
            data = {'status':'error','error_code': 101, 'message': "error: {0}".format(e)}      
            return JsonResponse(data)
       
    def put(self, request, format=None):
      try:   
           data={}
           data['pk'] =request.POST.get('pk')
           data['student_name'] =request.POST.get('name')
           data['mail_id'] =request.POST.get('mail_id')
           stud= Student.objects.get(id=data['pk'])
           for key, value in data.items():
               setattr(stud, key, value)
           stud.save()
           print(data['pk'])
           return JsonResponse({'data':data}, status=status.HTTP_200_OK)
      except ValidationError as e:
            data = {'status':'error','error_code': 103, 'message': "error: {0} ".format(e)}
            return JsonResponse(data)        
      except NameError as e:
            data = {'status':'error','error_code': 103, 'message': "error: {0} ".format(e)}
            return JsonResponse(data)
      except Exception as e:
            data = {'status':'error','error_code': 101, 'message': "error: {0}".format(e)}      
            return JsonResponse(data)
    
    def delete(self,request,format=None):
        try:
            data={}
            data['pk'] =request.POST.get('pk')
            stud= Student.objects.get(id=data['pk'])
            stud.delete()
            return JsonResponse({'data':'Deleted Successsfully!!'}, status=status.HTTP_204_NO_CONTENT) 
        except ValidationError as e:
            data = {'status':'error','error_code': 103, 'message': "error: {0} ".format(e)}
            return JsonResponse(data)        
        except NameError as e:
            data = {'status':'error','error_code': 103, 'message': "error: {0} ".format(e)}
            return JsonResponse(data)
        except Exception as e:
            data = {'status':'error','error_code': 101, 'message': "error: {0}".format(e)}      
            return JsonResponse(data)
    
      

    
    