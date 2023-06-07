class Module:
    """
    Базовый класс для модулей. Содержит обязательный метод init и методы для логирования ошибок
    """

    def __init__(self, name: str, config: dict = (), params: dict = ()):
        """
        Конструктор
        :param name: название модуля, под которым будут выводиться сообщения
        :param config: конфигурация для модуля
        :param params: любые дополнительные параметры
        """
        self.name = name
        self.init(config=config, params=params)
    #   __init__

    def init(self, config: dict = (), params: dict = ()) -> None:
        """
        Обязательная функция для инициализации модуля
        :param config: конфигурация для модуля
        :param params: любые дополнительные параметры
        :return: None
        """
        pass

    def shutdown(self, params: dict = ()) -> None:
        """
        Обязательная функция для отключения модуля
        :param params: любые дополнительные параметры, которые могут понадобиться для отключения
        :return: None
        """
        pass

    def info(self, message: str) -> None:
        """
        Вывести информационное сообщение
        :param message: текст сообщения
        :return: None
        """
        print(f"\u001b[1;37;40m{self.name}:\u001b[0;32m {message}\u001b[0;0m")

    def warning(self, message: str) -> None:
        """
        Вывести предупреждение
        :param message: текст предупреждения
        :return: None
        """
        print(f"\u001b[1;37;40m{self.name}:\u001b[0;0m \u001b[0;33;40m{message}\u001b[0;0m")

    def error(self, message: str) -> None:
        """
        Вывести ошибку
        :param message: текст ошибки
        :return: None
        """
        print(f"\u001b[1;37;40m{self.name}:\u001b[0;0m \u001b[0;31;40m{message}\u001b[0;0m")