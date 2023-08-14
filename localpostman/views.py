from django.http import JsonResponse
import json
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from localpostman.models import jarvis_user
from localpostman.models import jarvis_requested_access
from localpostman.settings import OPENAIKEY
import openai

openai.api_key = OPENAIKEY

@csrf_exempt
def jarvis(request):
    try:
        data = json.loads(request.body)
        order = data.get('order', 'Hello Jarvis')
        response=''
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=order,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        ) 
        return JsonResponse({'result': response["choices"][0]["text"].replace("\n", "")})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
@csrf_exempt    
def checkjarvis_user(request):
    try:
        data = json.loads(request.body)
        v_user_name = data.get('UserName', 'N')
        v_pass_code = data.get('PassCode','N')
        Isexits = jarvis_user.objects.filter(username = v_user_name,passcode = v_pass_code).exists()
        return JsonResponse({'response': Isexits})
    except Exception as e:
        return JsonResponse({'response': str(e)}, status=400)
    
@csrf_exempt     
def create_user(request):
    try:
        data = json.loads(request.body)
        v_user_name = data.get('UserName', 'N')
        v_pass_code = data.get('PassCode','N')
        v_message = data.get('message','N')
        c_jarvis_requested_access = jarvis_requested_access(
            username = v_user_name,
            passcode = v_pass_code,
            message = v_message
        )
        c_jarvis_requested_access.save()
        return JsonResponse({'response': True})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
    
   