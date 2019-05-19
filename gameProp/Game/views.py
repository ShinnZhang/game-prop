from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

# from ..gameProp.settings import MEDIA_ROOT
from .models import GameBase


class Game(View):

    def get(self, request):
        key_word = request.GET.get('game_label')
        result = {}
        # if key_word:
        try:
            game_ins = GameBase.objects.filter(game_label=key_word)[0]

            if game_ins:
                result['game_id'] = game_ins.game_id
                result['game_label'] = game_ins.game_label
                result['game_neckname'] = game_ins.game_neckname
                print('http://127.0.0.1:8000/static/Images/' + str(game_ins.game_logo))
                result['game_logo'] = 'http://127.0.0.1:8000/static/images/' + str(game_ins.game_logo)
                result['game_op'] = game_ins.game_op
            else:
                result['msg'] = 'ValueError: No game catched.'
        except Exception as e:
            print(e)

        return JsonResponse(data=result)

    def post(self, request):
        print(request)
        game_label = request.POST.get('game_label')
        game_neckname = request.POST.get('game_neckname')
        game_op = request.POST.get('game_op')
        game_logo = request.FILES.get('game_logo')

        print(game_label)
        print(game_neckname)
        print(game_op)
        print(game_logo)

        count = GameBase.objects.filter().count()
        game_id = hex(count)
        new_game = GameBase()
        new_game.game_id = game_id
        new_game.game_label = game_label
        new_game.game_neckname = game_neckname
        new_game.game_op = game_op
        new_game.game_logo = game_logo

        try:
            new_game.save()
        except Exception as e:
            print(e.__traceback__)

        return HttpResponse('111')