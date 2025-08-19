from django.shortcuts import render
from django.http import JsonResponse
 

# Create your views herd

def dataview(request):
  data = {
       'user' : 'Ayush Yadav',
       'age' : 25,
       'password' : 'your_password_here'
  }

  return JsonResponse(data)
