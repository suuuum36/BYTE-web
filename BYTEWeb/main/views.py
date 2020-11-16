from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .models import Subscriber
import requests, json, re

# Create your views here.
def index (request):
    if request.method == 'GET': 
        
        URL =  "https://api.stibee.com/v1/lists/81111/subscribers"
        
        headers = {
            "AccessToken" : "ed00b5b09dc81a0ee29ae26577bed3c2d5f38e5caedd824fe905ff5c6d9cbd4d6c8a79f45cb4641f9d54f4de85e713c83d6e50524343bd1fd4049e91d064175d",
            "listID" : "81111",
            "Content-Type": "application/json"
        }
        
        response_get = requests.get(URL, headers = headers)
        user_data = response_get.json()
        value = user_data['Value']
        emails = [email['email'] for email in value]
        user_num = len(emails)
        
        return render(request, 'main/index.html', {'user_num' : user_num})
    
    elif request.method == 'POST':
        
        URL =  "https://api.stibee.com/v1/lists/81111/subscribers"
        
        headers = {
            "AccessToken" : "ed00b5b09dc81a0ee29ae26577bed3c2d5f38e5caedd824fe905ff5c6d9cbd4d6c8a79f45cb4641f9d54f4de85e713c83d6e50524343bd1fd4049e91d064175d",
            "listID" : "81111",
            "Content-Type": "application/json"
        }
        
        name = request.POST['name']
        email = request.POST['email']
        
        
        data = {
        "eventOccuredBy": "MANUAL",
        "confirmEmailYN": "Y",
        "groupIds": [
        ],
        "subscribers": [
            {
            "email": email,
            "name": name
            }
        ]
        }
        
        response_get = requests.get(URL, headers = headers)
        user_data = response_get.json()
        value = user_data['Value']
        emails = [email['email'] for email in value]
        user_num = len(emails)
        
        if name != '' and email != '':
            
            email_match = re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)
            
            if email_match != None:
                
                if email in emails:
                    exist_alarm = "이미 존재하는 이메일입니다."
                    print('already exists')
                    
                else:
                    checked = request.POST.getlist('checkbox')
                    if checked != [] :
                        response_post = requests.post(URL, data=json.dumps(data), headers = headers)
                        exist_alarm = "메일함에서 인증을 완료해주세요!"
                        print(response_post.text)
                        print(checked)
                    else:
                        exist_alarm = "이용약관에 동의해주세요."
                        
            else:
                exist_alarm = "이메일 형식을 맞춰주세요."
                
        else:
            exist_alarm = "이름과 이메일을 모두 작성해주세요."
            
        return render(request, 'main/index.html', {'user_num' : user_num, 'exist_alarm' : exist_alarm , 'name':name, 'email':email})  
