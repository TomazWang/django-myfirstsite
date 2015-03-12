# trips/views.py

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# simple hello world
def hello_world(request):
	return HttpResponse("Hello World")

# use html 
def hello_html(request):
	output = """
		<!DOCTYPE html>
			<html>
				<head>
					<title>Hello Html with Django</title> 
				</head>

				<body>
					Hello World!
					<p>What time is it?</p>
					<em style="">It's {current_time}</em>
				</body>
			</html>
			""".format(current_time=datetime.now())
	return HttpResponse(output)


# use a template
def hello_temp(request):
	return render(request,'hello_temp.html',{'current_time':datetime.now()})


'''
	start making my first site with not just hello world
'''
# import the Post obj from model
from trips.models import Post

# home page ,show all the posts
def home(request):
	post_list = Post.objects.all()
	return render(request,
		'home.html',
		{'post_list':post_list})



