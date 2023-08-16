import json
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["POST"])
def emailView(request , *args , **kwargs):
    return_data = {
        "data" : None , 
        "errors" : None , 
        "success" : False , 
    }
    email = request.POST.get("email")
    name = request.POST.get("name")
    phone_number = request.POST.get("phone_number")
    data = json.dumps({"api_key" : "b8afcee3-9b74-40d9-bebd-5e2472fcee1c" , 
            "email_address" : f"{email}",
            "fields" :
                {
                    "FirstName" : f"{name}",
                    "LastName":"",
                    "Birthday": f"" ,
                    "PhoneNumber" : f"{phone_number}"
                },
            "tags":["vip"] ,
            "status" : "SUBSCRIBED" ,
            })
    url = "https://emailoctopus.com/api/1.6/lists/c6a2061c-3b7b-11ee-a331-db42d3227797/contacts"
    headers = {
        "Content-Type" : "application/json" ,   
    }
    response = requests.post(
        url = url , 
        headers = headers , 
        data = data ,
    )
    if response.status_code != 200 :
        return_data["success"] = True
    return Response(return_data)