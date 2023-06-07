from core.configloader import ConfigLoader
from core.moduleloader import ModuleLoader
from core.scenehandler import SceneHandler

class Core:
    """
    Ядро движка, которое отвечает за загрузку конфигурации и модулей, за запуск первой сцены

    Attributes
    ----------
    start_scene : str
        Название начальной сцены, которую запустит ядро

    """
    def __init__(self, start_scene: str):
        """
        Конструктор
        Parameters
        ----------
        start_scene : str
            Название начальной сцены, которую запустит ядро
        """
        print('Загрузка ядра...')

        # Загрузка файлов конфигурации
        print('\tЗагрузка файлов конфигурации...')
        config_loader = ConfigLoader()
        self.config = config_loader.parse_dir('config')

        # Загрузка модулей
        print('\tЗагрузка модулей...')
        module_loader = ModuleLoader()
        self.modules = module_loader.load_modules_from_dir(directory='modules', configs=self.config)

        # Загрузка остальных свойств
        self.start_scene = start_scene

        print('Ядро загружено\n')
    # __init__

    def run(self) -> None:
        """
        Запуск начальной сцены, указанной в свойстве start_scene
        """

        scene_handler = SceneHandler()
        scene_name = self.start_scene

        while scene_name != None:
            print(f"Загрузка сцены {scene_name}...")
            scene_class = scene_handler.load_scene(scene_name)
            scene = scene_class(config=self.config, modules=self.modules)
            scene_name = scene.handle()

        print('Завершение программы')
    # run
