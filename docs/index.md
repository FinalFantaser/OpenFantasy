# Структура приложения
- Ядро:
    - Файлы конфигурации
    - Модули
    - Сцены

Ядро загружает и хранит в памяти данные конфигурации и модули.

Логика взаимодействия модулей указывается в сцене. За запуск и смену сцен отвечает ядро.

# Логика выполнения приложения
- Ядро загружает все файлы конфигурации
- Ядро загружает и инициализирует все модули
- Ядро запускает первую сцену

# Ядро
Ядро отвечает за управление ресурсами: файлами конфигурации, модулями и сценами. Напрямую ядро не влияет на логику конечного приложения. В задачи ядра входит только загрузка конфигурации и модулей с последующим запуском сцены. Вся логика приложения выполняется в сценах

# Ресурсы
Ресурсы - это данные, составляющие основу приложения. Ресурсы подразделяются на три типа:
- Файлы конфигурации
- Модули
- Сцены

## Файлы конфигурации
Файлы конфигурации содержат в себе данные, на основе которых действуют модули и сцены.

Файлы конфигурации должны храниться в папке **config** и иметь расширение *.ini*

### Создание файла конфигурации
Создайте текстовый файл с названием на латинице и расширением *.ini* (например, *test_config.ini*) и поместите его в папку **config**.

**Содержимое файла обязательно должно начинаться с заголовка, иначе приложение не распознает его!** Содержимое заголовка может быть произвольным.

```ini
[HEADER]
option_1=true
option_2=option_2
option_3=123
```

**Заголовки и параметры указывать на латинице**

### Доступ к данным конфигурации из приложения
Загруженные данные хранятся в ядре в свойстве config. Данные хранятся в виде словаря:

```python
core.config['имя файла']['название настройки']
```

После загрузки данные файла сохраняются в core.config под именем файла конфигурации (без пути и без расширения *.ini*). Например, если в папке **config** находится файл *test_config.ini*, то он будет сохранён в словаре под именем test_config:

```python
core.config['test_config']
```

Опции, указанные в файле, сохраняются под своим именем:

```ini
; Содержимое test_config.ini
[HEADER]
example=example_text
```

```python
# Получение опции example в приложении
value = core.config['test_config']['example']

print(value)  # example_text
```

## Модули
В модулях содержатся структуры данных и методы, которые пользователь сочтёт нужным для работы приложения.

Каждый модуль представляет собой отдельный класс, хранящийся в отдельном файле. Все модули должны храниться в папке **modules**

Модули наследуют от класса Module и имеют обязательный метод init, который необходимо прописать. Родительский класс также предоставляет модулям методы для удобства работы

### Создание модуля
Чтобы приложение без ошибок распознало файлы модулей, необходимо соблюсти следующие условия:
- Все модули должны быть файлами исходного кода Python (расширение *.py*)
- Каждый модуль должен быть отдельным классом в отдельном файле
- Имя класса должно указываться в формате UpperCamelCase
- Имя файла должно повторять имя класса, но в формате snake_case. При загрузке оно преобразуется ядром в имя класса (в формат UpperCamelCase).
- В классе обязательно должен быть переназначен метод init, в котором будет указана логика инициализации модуля
- Класс не может называться Module, а файл не может называться module.py
- Файл модуля должен быть сохранён в папке **modules**

Нельзя удалять или изменять файл *module.py* с классом *Module*, который также находится в папке **modules**.

У метода init есть параметр config, куда ядро при загрузке модулей передаёт данные, загруженные из файлов конфигурации. Их можно использовать для инициализации модуля