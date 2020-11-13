from django.shortcuts import render, redirect
from .models import Subscriber
import requests, json

# Create your views here.
def index (request):
    if request.method == 'GET': 
        return render(request, 'main/index.html')
    
    elif request.method == 'POST':
        
        name = request.POST['name']
        email = request.POST['email']
        
        URL =  "https://api.stibee.com/v1/lists/81111/subscribers"
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

        headers = {
            "AccessToken" : "ed00b5b09dc81a0ee29ae26577bed3c2d5f38e5caedd824fe905ff5c6d9cbd4d6c8a79f45cb4641f9d54f4de85e713c83d6e50524343bd1fd4049e91d064175d",
            "listID" : "81111",
            "Content-Type": "application/json"
        }
        

        response_get = requests.get(URL, verify=False, headers = headers)
        user_data = response_get.json()
        value = user_data['Value']
        emails = [email['email'] for email in value]

        if email in emails:
            print('already exists')
        else:
            response_post = requests.post(URL, verify=False, data=json.dumps(data), headers = headers)
            print(response_post.text)
            
        return redirect('index')
