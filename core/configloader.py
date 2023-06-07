import glob
import configparser

class ConfigLoader:
    """
    Загрузчик файлов конфигурации
    """

    def parse_ini(self, file: str) -> dict:
        """
        Парсит указанный файл .ini и возвращает данные из него в виде словаря
        :param file: название файла .ini, который нужно распарсить
        :param parser: парсер для файла. Если None, создаётся автоматически
        :return: dict
        """
        parser = configparser.ConfigParser()
        parser.read(filenames=file, encoding='UTF-8')

        config = dict()

        for section in parser.sections():
            for key, value in parser.items(section=section):
                config[key] = value

        return config
    # parse_ini

    def parse_dir(self, directory: str) -> dict:
        """
        Парсит все файлы .ini в указанной директории
        :param directory: название директории (начиная от корневой)
        :return: dict
        """

        #   Загрузка списка файлов в директории с расширением .ini
        ini_files = glob.glob(pathname=directory + '/*.ini');

        #   Если файлов конфигурации не найдено, вернуть пустой массив
        total_files = len(ini_files)
        if total_files < 1:
            return dict()

        print(f"\t\tНайдено {total_files} файлов: {','.join(ini_files)}")

        configs = dict()

        #   Парсинг каждого файла
        for file in ini_files:
            config_name = file.removeprefix(f"{directory}\\")
            config_name = config_name.removesuffix('.ini')

            configs[config_name] = self.parse_ini(file)

        return configs
    #parse_dir