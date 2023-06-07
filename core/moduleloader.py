import glob
import importlib

class ModuleLoader:
    """
    Загрузчик модулей для ядра
    """

    # Имя класса базового модуля, который нельзя загружать
    BASE_MODULE_CLASS = 'Module'

    # Имя файла базового модуля, который нельзя загружать
    BASE_MODULE_FILE = 'module.py'

    def load_module(self, file: str, class_name: str):
        """
        Загружает указанный файл и извлекает из него определение класса
        :param file: загружаемый файл
        :param class_name: класс, который нужно извлечь
        :return: класс, указанный в class_name
        """

        # TODO Валидация модуля Проверка имени модуля. Если получается Module, то не загружать
        # ...

        module_file = importlib.import_module(file.replace('\\', '.').removesuffix('.py'))
        module = getattr(module_file, class_name)
        return module
    # load_module

    def load_modules_from_dir(self, directory: str, configs: dict):
        # Получение списка файлов в директории
        module_files = glob.glob(pathname=directory + "/*.py")

        # Удаление из списка module.py
        module_files.remove(f"{directory}\\{self.BASE_MODULE_FILE}")
        total_files = len(module_files)

        print(f"\t\tНайдено {total_files} модулей: {','.join(module_files)}")

        # Если модулей больше не найдено, прекратить выполнение
        if total_files < 1:
            return dict()

        # Загрузка и иницализация модулей из списка
        modules = dict()
        for file in module_files:
            filename = self.get_only_filename(full_filename=file, prefix=directory + '\\')
            class_name = self.get_class_name_from_file_name(filename)
            obtained_class = self.load_module(file=file, class_name=class_name)
            modules[class_name] = obtained_class(name=class_name, config=configs)

        return modules
    # load_modules_from_dir

    def get_class_name_from_file_name(self, file: str) -> str:
        """
        Переводит название файла в snake_case в UpperCamelCase
        :param file: название файла
        :return: str
        """

        init, *temp = file.split('_')
        camelcase = ''.join([init.title(), *map(str.title, temp)])

        return camelcase
    # get_class_name_from_file_name

    def get_only_filename(self, full_filename: str, prefix: str) -> str:
        """
        Вычленяет из полного пути только имя конечного файла без расширения
        :param full_filename: полный путь к файлу
        :param prefix: путь, который надо удалить
        :return: str
        """
        filename = full_filename.removeprefix(prefix)
        return filename.removesuffix('.py')
    # get_only_filename

