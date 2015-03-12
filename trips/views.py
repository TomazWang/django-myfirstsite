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