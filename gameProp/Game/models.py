from django.db import models

# Create your models here.
class GameBase(models.Model):

    class Meta:
        db_table = 'game_info_table'

    game_id = models.CharField(max_length=16,unique=True, primary_key=True, verbose_name='游戏ID')
    game_label = models.CharField(max_length=32,unique=True, verbose_name='游戏名')
    game_neckname = models.CharField(max_length=32, verbose_name='游戏别名')
    # 使用CDN的情况下数据库保存连接
    # game_logo = models.CharField(max_length='512', verbose_name='游戏logo')
    # 现阶段使用本地静态文件
    game_logo = models.ImageField(upload_to='gameLogos', verbose_name='游戏logo')
    game_op = models.CharField(max_length=128, verbose_name='游戏运行商')