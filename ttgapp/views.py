from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
# from rest_framework.parsers import JSONparser
from rest_framework.decorators import api_view

# Create your views here.
from .models import Admin,Department,Degreeprogram,Semester,Subject,Faculty,TimetableData
from .serializers import AdminSerializer,DeptSerializer,DegpgmSerializer,SemSerializer,SubSerializer,FacSerializer,TimetableDataSerializer

# admin--view
@api_view(['GET'])
def adminOverview(request):
    api_urls={
        'List':'/admin-list/',
        'Create':'/admin-create/',
        'Update':'/admin-Update/',
        'Delete':'/admin-delete/',
    }
    return Response(api_urls)
@api_view(['GET'])
def showall(request):
    admins=Admin.objects.all()
    serializer=AdminSerializer(admins,many=True)
    return Response(serializer.data)

# department--view
@api_view(['GET'])
def deptOverview(request):
    api_urls={
        'List':'/dept-list/',
        'Create':'/dept-create/',
        'Update':'/dept-Update/',
        'Delete':'/dept-delete/',
    }
    return Response(api_urls)
@api_view(['GET'])
def showalldep(request):
    admins=Department.objects.all()
    serializer=DeptSerializer(admins,many=True)
    return Response(serializer.data)

# degree-progamme -- view
@api_view(['GET'])
def degpgmOverview(request):
    api_urls={
        'List':'/degpgm-list/',
        'Create':'/degpgm-create/',
        'Update':'/degpgm-Update/',
        'Delete':'/degpgm-delete/',
    }
    return Response(api_urls)
@api_view(['GET'])
def showalldegpgm(request):
    admins=Degreeprogram.objects.all()
    serializer=DegpgmSerializer(admins,many=True)
    return Response(serializer.data)

#sem view
@api_view(['GET'])
def SemesterOverview(request):
    api_urls={
        'List':'Semester-list/',
        'Create':'/Semester-create/',
        'Update':'/Semester-Update/',
        'Delete':'/Semester-delete/',
    }
    return Response(api_urls)
@api_view(['GET'])
def showallsem(request):
    admins=Semester.objects.all()
    serializer=SemSerializer(admins,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def SubjectOverview(request):
    api_urls={
        'List':'Subject-list/',
        'Create':'/Subject-create/',
        'Update':'/Subject-Update/',
        'Delete':'/Subject-delete/',
    }
    return Response(api_urls)
@api_view(['GET'])
def showallsub(request):
    admins=Subject.objects.all()
    serializer=SubSerializer(admins,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def FacultyOverview(request):
    api_urls={
        'List':'Faculty-list/',
        'Create':'/Faculty-create/',
        'Update':'/Faculty-Update/',
        'Delete':'/Faculty-delete/',
    }
    return Response(api_urls)

@api_view(['GET'])
def showallsub(request):
    admins=Faculty.objects.all()
    serializer=FacSerializer(admins,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Overllview(request):
    api_urls={
        'List':'overall-list/',
        'Create':'/overall-create/',
        'Update':'/overall-Update/',
        'Delete':'/overall-delete/',
    }
    return Response(api_urls)

@api_view(['GET'])
def overallshow(request):
    admins=TimetableData.objects.all()
    serializer=TimetableDataSerializer(admins,many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def overallcreate(request):
    serializer = TimetableDataSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return JsonResponse(serializer.data)


# def posttimedata(request):
#     s_no = request.POST['S no']
#     sub_code  = request.POST['Sub_code ']
#     sub_title = request.POST['Sub_title']
#     fac_name = request.POST['Fac_name']
#     data = TimetableData.objects.get(s_no=s_no,sub_code=sub_code,sub_title=sub_title,fac_name=fac_name)
#     if data:
#         return JsonResponse({'bool':True})
#     else:
#         return JsonResponse({'bool':False})