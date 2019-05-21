from django.db import models

# Create your models here.
class Game(models.Model):

    class Meta:
        db_table = 'game_info_table'

    game_id = models.CharField(max_length=16,unique=True, primary_key=True, verbose_name='游戏ID')
    game_label = models.CharField(max_length=32,unique=True, verbose_name='游戏名')
    game_neckname = models.CharField(max_length=32, verbose_name='游戏别名')
    game_logo = models.ImageField(upload_to='gameLogos', verbose_name='游戏logo')
    game_op = models.CharField(max_length=128, verbose_name='游戏运行商')
    game_props = models.IntegerField(default=0, verbose_name='游戏下道具数')
    game_concern = models.IntegerField(default=0, verbose_name='游戏关注度')