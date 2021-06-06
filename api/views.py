from django.http.response import Http404, HttpResponse, HttpResponseNotFound
from .models import Game, Case, Cpu, Gpu, Motherboard, Psu, Ssd
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from api import serializers
from .serializers import *

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Games List': '/games',
        'Game Get with ID': '/game/<pk>',
        'Calculate FPS [POST]': '/calculate-fps',
    }
    return Response(api_urls)

@api_view(['GET'])
def GamesGet(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GameGet(request, pk):
    try:
        game = Game.objects.get(id = pk)
    except ObjectDoesNotExist:
        raise Http404("No such game in database.")
    serializer = GameSerializer(game, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def CasesGet(request):
    cases = Case.objects.all()
    serializer = CaseSerializer(cases, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def CasesGetLimit(request, limit):
    cases = Case.objects.all().order_by('id')[0:limit:1]
    serializer = CaseSerializer(cases, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def CalculateFps(request):
    fps_min = min([
        Case.objects.get(id = request.data["case"]["id"]).max_fps,
        Cpu.objects.get(id = request.data["cpu"]["id"]).max_fps,
        Gpu.objects.get(id = request.data["gpu"]["id"]).max_fps,
        Motherboard.objects.get(id = request.data["mobo"]["id"]).max_fps,
        Psu.objects.get(id = request.data["psu"]["id"]).max_fps,
        Ssd.objects.get(id = request.data["ssd"]["id"]).max_fps,
    ])
    res_multiplayer = {
        "1080p": 1,
        "1440p": 0.7,
        "4k": 0.4
    }
    return Response(fps_min / Game.objects.get(id = request.data["game"]["id"]).demand_value * res_multiplayer[request.data["resolution"]])