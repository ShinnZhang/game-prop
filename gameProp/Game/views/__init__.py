from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

# from ..gameProp.settings import MEDIA_ROOT
from .models import Game


class GameApi(View):

    def get(self, request):
        key_word = request.GET.get('game_label')
        result = {}
        # if key_word:
        try:
            game_ins = Game.objects.filter(game_label=key_word)[0]

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

        count = Game.objects.filter().count()
        game_id = hex(count)
        new_game = Game()
        new_game.game_id = game_id
        new_game.game_label = game_label
        new_game.game_neckname = game_neckname
        new_game.game_op = game_op
        new_game.game_logo = game_logo

        try:
            new_game.save()
        except Exception as e:
            print(e)

        return HttpResponse('111')

    def put(self, request):
        game_id = request.PUT.get('game_id')
        modis = {}
        modis['game_label'] = request.PUT.get('game_label')  or None
        modis['game_neckname'] = request.PUT.get('game_neckname')  or None
        modis['game_op'] = request.PUT.get('game_op') or None
        modis['game_logo'] = request.PUT.get('game_logo') or None
        result = {}
        if GameApi.is_all_empty(modis):
            try:
                game_ins = Game.objects.filter(game_id=game_id)[0]
                game_ins.game_label = modis['game_label'] or game_ins.game_label
                game_ins.game_neckname = modis['game_neckname'] or game_ins.game_neckname
                game_ins.game_op = modis['game_op'] or game_ins.game_op
                game_ins.game_logo = modis['game_logo'] or game_ins.game_logo
                game_ins.save()
                result['msg'] = '[200]Update successed.'
            except Exception as e:
                print(e)
        else:
            result['msg'] = 'RequestError: No change requested.'
        return JsonResponse(data=result)

    def delete(self, request):
        game_id  = request.DELETE.get('game_id')
        result = {}
        try:
            game_ins = Game.objects.filter(game_id=game_id)[0]
            if game_ins.exists():
                game_ins.delete()
                result['msg'] = '[200]Data delete successed.'
            else:
                result['msg'] = 'RequestError: No current game "' + game_id + '".'
        except Exception as e:
            print(e)

        return JsonResponse(data=result)



    @classmethod
    def is_all_empty(self, dic):
        for k in list(dic.keys()):
            if dic[k]:
                return True
        return False