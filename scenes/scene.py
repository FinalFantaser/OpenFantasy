class Scene:
    """
    Выполняет основную логику приложения с использованием конфигурации и модулей
    """
    def __init__(self, config: dict, modules: dict):
        """
        Конструктор
        :param config: данные конфигурации
        :param modules: модули для использования в сцене
        """
        self.config = config
        self.modules = modules
    # Конструктор

    def handle(self) -> str | None:
        """
        Обязательная функция, в которой выполняется вся логика сцены
        :return: str | None - имя следующей сцены
        """
        return None
    # handle