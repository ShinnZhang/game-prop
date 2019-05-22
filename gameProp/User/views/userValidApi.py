from django.http import JsonResponse
from django.views import View
from ..models.userValid import UserValid

class UserValidApi(View):

    def post(self, request):

        user_input = request.POST.get('user_input')
        result = {}
        try:
            if UserValid.objects.filter(v_value=user_input):
                result["code"] = 0
            else:
                result["code"] = 1
        except Exception as e:
            result["code"] = 500
            result["msg"] = str(e)

        return JsonResponse(data=result)
