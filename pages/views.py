from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html" 

class AboutMeView(TemplateView):
    template_name = "about.html"