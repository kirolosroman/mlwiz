from django.urls import re_path
from .consumers import PlotUpdateConsumer

websocket_urlpatterns = [
    re_path(r'ws/plot_update/$', PlotUpdateConsumer.as_asgi()),
]