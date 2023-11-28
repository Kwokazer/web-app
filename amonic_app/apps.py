from django.apps import AppConfig



class AmonicAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'amonic_app'

    def ready(self):
        from .utils import import_data_from_csv
        # Вызываем функцию импорта данных из CSV при запуске приложения
        import_data_from_csv('./UserData.csv')
