from django.apps import AppConfig


class GoodiesConfig(AppConfig):
    name = 'goodies'

    def ready(self):
    	import goodies.signals
