from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Student
from .serializers import *


@api_view(['GET', "POST"])
def students_list(req):
	if req.method == "GET":
		data = []
		nextPage = 1
		prevPage = 1
		students = Student.objects.all()
		page = req.GET.get('page', 1)
		paginator = Paginator(students, 10)
		try:
			data = paginator.page(page)
		except PageNotAnInteger:
			data = paginator.page(1)
		except EmptyPage:
			data = paginator.page(paginator.num_pages)

		serializer = StudentSerializer(data, context={'req': req}, many=True)
		if data.has_next():
			nextPage = data.next_page_number()
		if data.has_previous():
			prevPage = data.previous_page_number()

		return Response({
			'data': serializer.data,
			'count': paginator.count,
			'numpages': paginator.num_pages,
			'nextlink': '/api/students/?page='+str(nextPage),
			'prevlink': '/api/students/?page='+str(prevPage)
			})
	elif req.method == 'POST':
		serializer = StudentSerializer(data=req.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def students_detail(request, pk):
	try:
		student = Student.objects.get(pk=pk)
	except student.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = StudentSerializer(student,context={'request': request})
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = StudentSerializer(student, data=request.data,context={'request': request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		student.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)