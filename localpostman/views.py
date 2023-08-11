from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# from localpostman.models import User
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
   