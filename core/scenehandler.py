import importlib
import re
from scenes.scene import Scene

class SceneHandler:
    """
    Загрузчик сцен
    """

    # Директория, где хранятся сцены
    DIR_SCENES = 'scenes'

    def load_scene(self, name: str):
        """
        Загрузка сцены по имени
        :param name: имя класса сцены
        :return: класс загруженной сцены
        """

        # Преобразование имени в snake_case для загрузки из файла
        filename = self.DIR_SCENES + '\\' + re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

        module = importlib.import_module(name=filename.replace('\\', '.').removesuffix('.py'), package=None)
        loaded_class = getattr(module, name)

        if self.validate_scene(loaded_class):
            return loaded_class
    # load_scene

    def validate_scene(self, scene) -> bool:
        # TODO Выбросить исключение, если валидация не пройдена
        return issubclass(scene, Scene)
    # validate_scene
