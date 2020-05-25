from django.shortcuts import render
from django.contrib import messages
from . models import Usersdata
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
@csrf_exempt
def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']
		Usersdata(username=username,email=email,password=password1).save()
		
		print("Data Saved")
		if password1!=password2:
			return JsonResponse({"msg":"password are not same"}, safe=False)
		messages.success(request,f'Account created for{username}!')
		return JsonResponse({"username":username,"email":email,"password1":password1}, safe=False)
	return JsonResponse({"msg":"Use Post method"})
@csrf_exempt
def login(request):
	if request.method=="POST":
		username=request.POST['username']
		email = request.POST['email']
		password1=request.POST['password1']
		data=Usersdata.objects.get(email=email,username=username)
		if password1==data.password:
			return JsonResponse({"username":data.username,"email":data.email,"password":password1}, safe=False)

		return JsonResponse({"msg":"Wrong Username or password"},safe=False)
			






