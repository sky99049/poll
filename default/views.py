from django.shortcuts import render , render_to_response
from django.views.generic import ListView, DetailView, RedirectView
from .models import *
# Create your views here.


def poll_list(req):
    polls = Poll.objects.all()
    return render_to_response('poll_list.html', {'polls': polls})

class PollList(ListView):
    model = Poll

class PollDetail(DetailView):
    model = Poll
    # 取得額外資料供頁面範本顯示
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        options = Option.objects.filter(poll_id=self.kwargs['pk'])
        context['options'] = options
        return context
## 投票
class PollVote(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        option = Option.objects.get(id=self.kwargs['pk'])
        option.count += 1   # 將選項的票數+1
        option.save()       # 儲存至資料庫
        return "/poll/"+str(option.poll_id)+"/"
