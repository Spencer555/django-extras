from django.shortcuts import render
from search.models import Info 
from django.views.generic import ListView
import json
# Create your views here.



class InfoListView(ListView):
    model = Info 
    template_name = "infos/main.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Info.objects.values()))
        return context
     