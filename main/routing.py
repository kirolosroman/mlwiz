from django.urls import re_path
from .consumers import PlotUpdateConsumer,PlotResultConsumerHD

websocket_urlpatterns = [
    re_path(r'ws/plot_update/$', PlotUpdateConsumer.as_asgi()),
    re_path(r'ws/plot_resulthd/$', PlotResultConsumerHD.as_asgi()),
]