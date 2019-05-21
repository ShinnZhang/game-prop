import time

from django.http import JsonResponse
from django.views import View

from ..models import Game

class GamesApi(View):
    #
    # 复数游戏信息操作的Api
    # GET
    #



    def get(self, request):
        result = {}
        key_word = request.GET.get('key_word') or None
        per_page = request.GET.get('per_page') or 20
        page = request.GET.get('page') or 1
        game_op = request.GET.get('game_op') or None
        concern = request.GET.get('concern') or 1
        start = (int(page) - 1) * int(per_page)
        end = int(page) * int(per_page)
        start_time = time.time()
        try:
            if key_word:
                if game_op:
                    if concern:
                        games = Game.objects.filter(game_op=game_op).filter(game_label_contains=key_word).order_by('game_concern')[start: end]
                    else:
                        games = Game.objects.filter(game_op=game_op).filter(game_label_contains=key_word).order_by('-game_concern')[start: end]
                else:
                    if concern==1:
                        games = Game.objects.filter(game_label_contains=key_word).order_by('game_concern')[start: end]
                    else:
                        games = Game.objects.filter(game_label_contains=key_word).order_by('-game_concern')[start: end]
            else:
                if game_op:
                    if concern==1:
                        games = Game.objects.filter(game_op=game_op).order_by('game_concern')[start: end]
                    else:
                        games = Game.objects.filter(game_op=game_op).order_by('-game_concern')[start: end]
                else:
                    if concern:
                        games = Game.objects.all().order_by('game_concern')[start: end]
                    else:
                        games = Game.objects.all().order_by('-game_concern')[start: end]
            print(time.time() - start_time)
            data = []
            for game in games:
                dic = {}
                dic['game_id'] = game.game_id
                dic['game_label'] = game.game_label
                dic['game_neckname'] = game.game_neckname
                dic['game_logo'] = 'http://127.0.0.1:8000/static/images/' + str(game.game_logo)
                dic['game_op'] = game.game_op
                dic['game_props'] = game.game_props
                dic['game_concern'] = game.game_concern
                data.append(dic)
        except Exception as e:
            print(e)
        result['data'] = data
        return JsonResponse(data=result, safe=False)

