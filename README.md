# Тестовое задание на должность Python developer в ООО КОМТЕК

Разработать сервис терминологии и REST API к нему.



## Описание

Сервис терминологии оперирует ниже перечисленными сущностями.



Сущность "Справочник" содержит следующие атрибуты:

- идентификатор справочника (глобальный и не зависит от версии)
- наименование
- короткое наименование
- описание
- версия (тип: строка,  не может быть пустойуникальная в пределах одного справочника)
- дата начала действия справочника этой версии



Сущность "Элемент справочника"

- идентификатор
- родительский идентификатор
- код элемента (тип: строка, не может быть пустой)
- значение элемента (тип: строка, не может быть пустой)



API должно предоставлять следующие методы:

- получение списка справочников.
- получение списка справочников, актуальных на указанную дату.
- получение элементов заданного справочника текущей версии
- валидация элементов заданного справочника текущей версии
- получение элементов заданного справочника указанной версии
- валидация элемента заданного справочника по указанной версии

В API должен быть предусмотрен постраничный вывод результата (данные должны возвращаться частями по 10 элементов).

К сервису должна иметься GUI административной части, с помощью которой можно добавлять новые справочники, новые версии справочников, указывать дату начала действия и наполнять справочники элементами.

Некоторые подробности намеренно не указаны. Оставляем их на ваше усмотрение.


## Реализация
* REST API
* Административный интерфейс


## Использованные технологии
* Python >=3.8
* Django >=3.2,<4
* DRF
* PostgreSQL
* Docker


## Диаграмма связей таблиц базы данных
TODO: добавить изображение диаграммы


## Установка

1. Клонировать репозиторий
    ```
    git clone https://github.com/vowatchka/komtek_test_task
    cd komtek_test_task
    ```
2. Запустить контейнеры docker
    ```
    docker-compose up --build -d
    ```
3. Выполнить миграции и создать суперпользователя
    ```
    docker-compose run terms_srv python manage.py migrate
    docker-compose run terms_srv python manage.py createsuperuser
    ```
4. Импортировать заранее сгенерированные тестовые фикстуры
    ```
    docker-compose run terms_srv python manage.py loaddata --format yaml -i --app app_terms Directory.yaml DirectoryVersion.yaml DirectoryItem.yaml
    ```
5. Перейти по адресу http://localhost:8000. Должен отобразиться Swagger UI, где можно попробовать предлагаемый API.
6. Также можно воспользоваться административным интерфейсом для управления справочниками, их версиями и элементами, перейдя по адресу http://localhost:8000/admin/ и войдя под созданным ранее суперпользователем.


## Примеры работы API
* Получение списка справочников
    ```
    GET http://localhost:8000/api/directories/
    ```

    Вывод не полностью отформатирован для краткости:
    ```json
    {
      "count": 20,
      "next": "http://127.0.0.1:8000/api/directories/?page=2",
      "previous": null,
      "results": [
        {"id":4,"title":"Справочник 1","alias":"directory1","description":"Сгенерированный справочник 1","versions":[{"version":"3","actual_from_dt":"2022-03-10"},{"version":"2","actual_from_dt":"2022-03-05"},{"version":"1","actual_from_dt":"2022-02-28"}],"items":"http://127.0.0.1:8000/api/directories/4/items/"},
        {"id":13,"title":"Справочник 10","alias":"directory10","description":"Сгенерированный справочник 10","versions":[{"version":"3","actual_from_dt":"2022-03-08"},{"version":"2","actual_from_dt":"2022-03-05"},{"version":"1","actual_from_dt":"2022-03-02"}],"items":"http://127.0.0.1:8000/api/directories/13/items/"},
        {"id":14,"title":"Справочник 11","alias":"directory11","description":"Сгенерированный справочник 11","versions":[{"version":"3","actual_from_dt":"2022-03-08"},{"version":"2","actual_from_dt":"2022-03-05"},{"version":"1","actual_from_dt":"2022-03-02"}],"items":"http://127.0.0.1:8000/api/directories/14/items/"},
        {"id":15,"title":"Справочник 12","alias":"directory12","description":"Сгенерированный справочник 12","versions":[{"version":"3","actual_from_dt":"2022-03-08"},{"version":"2","actual_from_dt":"2022-03-05"},{"version":"1","actual_from_dt":"2022-03-02"}],"items":"http://127.0.0.1:8000/api/directories/15/items/"},
        {"id":16,"title":"Справочник 13","alias":"directory13","description":"Сгенерированный справочник 13","versions":[{"version":"3","actual_from_dt":"2022-03-08"},{"version":"2","actual_from_dt":"2022-03-05"},{"version":"1","actual_from_dt":"2022-03-02"}],"items":"http://127.0.0.1:8000/api/directories/16/items/"},
        {"id":17,"title":"Справочник 14","alias":"directory14","description":"Сгенерированный справочник 14","versions":[{"version":"3","actual_from_dt":"2022-03-08"},{"version":"2","actual_from_dt":"2022-03-05"},{"version":"1","actual_from_dt":"2022-03-02"}],"items":"http://127.0.0.1:8000/api/directories/17/items/"},
        {"id":18,"title":"Справочник 15","alias":"directory15","description":"Сгенерированный справочник 15","versions":[{"version":"3","actual_from_dt":"2022-03-14"},{"version":"2","actual_from_dt":"2022-03-09"},{"version":"1","actual_from_dt":"2022-03-04"}],"items":"http://127.0.0.1:8000/api/directories/18/items/"},
        {"id":19,"title":"Справочник 16","alias":"directory16","description":"Сгенерированный справочник 16","versions":[{"version":"3","actual_from_dt":"2022-03-14"},{"version":"2","actual_from_dt":"2022-03-09"},{"version":"1","actual_from_dt":"2022-03-04"}],"items":"http://127.0.0.1:8000/api/directories/19/items/"},
        {"id":20,"title":"Справочник 17","alias":"directory17","description":"Сгенерированный справочник 17","versions":[{"version":"3","actual_from_dt":"2022-03-14"},{"version":"2","actual_from_dt":"2022-03-09"},{"version":"1","actual_from_dt":"2022-03-04"}],"items":"http://127.0.0.1:8000/api/directories/20/items/"},
        {"id":21,"title":"Справочник 18","alias":"directory18","description":"Сгенерированный справочник 18","versions":[{"version":"3","actual_from_dt":"2022-03-14"},{"version":"2","actual_from_dt":"2022-03-09"},{"version":"1","actual_from_dt":"2022-03-04"}],"items":"http://127.0.0.1:8000/api/directories/21/items/"}
      ]
    }
    ```
* Получение списка справочников, актуальных на указанную дату
    ```
    GET http://localhost:8000/api/directories/?actual_before_dt=28.02.2022
    ```

    Получим все справочники, для которых дата начала действия одной из версий меньше либо равна указанной дате. Справочники, которые еще не начали действовать на момент указанной даты, не попадут в список.
    Вывод не полностью отформатирован для краткости:
    ```json
    {
      "count": 7,
      "next": null,
      "previous": null,
      "results": [
        {"id":4,"title":"Справочник 1","alias":"directory1","description":"Сгенерированный справочник 1","versions":[{"version":"3","actual_from_dt":"2022-03-10"},{"version":"2","actual_from_dt":"2022-03-05"},{"version":"1","actual_from_dt":"2022-02-28"}],"items":"http://127.0.0.1:8000/api/directories/4/items/"},
        {"id":5,"title":"Справочник 2","alias":"directory2","description":"Сгенерированный справочник 2","versions":[{"version":"3","actual_from_dt":"2022-03-10"},{"version":"2","actual_from_dt":"2022-03-05"},{"version":"1","actual_from_dt":"2022-02-28"}],"items":"http://127.0.0.1:8000/api/directories/5/items/"},
        {"id":6,"title":"Справочник 3","alias":"directory3","description":"Сгенерированный справочник 3","versions":[{"version":"3","actual_from_dt":"2022-03-10"},{"version":"2","actual_from_dt":"2022-03-05"},{"version":"1","actual_from_dt":"2022-02-28"}],"items":"http://127.0.0.1:8000/api/directories/6/items/"},
        {"id":7,"title":"Справочник 4","alias":"directory4","description":"Сгенерированный справочник 4","versions":[{"version":"3","actual_from_dt":"2022-03-10"},{"version":"2","actual_from_dt":"2022-03-05"},{"version":"1","actual_from_dt":"2022-02-28"}],"items":"http://127.0.0.1:8000/api/directories/7/items/"},
        {"id":8,"title":"Справочник 5","alias":"directory5","description":"Сгенерированный справочник 5","versions":[{"version":"3","actual_from_dt":"2022-03-10"},{"version":"2","actual_from_dt":"2022-03-05"},{"version":"1","actual_from_dt":"2022-02-28"}],"items":"http://127.0.0.1:8000/api/directories/8/items/"},
        {"id":9,"title":"Справочник 6","alias":"directory6","description":"Сгенерированный справочник 6","versions":[{"version":"3","actual_from_dt":"2022-03-10"},{"version":"2","actual_from_dt":"2022-03-05"},{"version":"1","actual_from_dt":"2022-02-28"}],"items":"http://127.0.0.1:8000/api/directories/9/items/"},
        {"id":10,"title":"Справочник 7","alias":"directory7","description":"Сгенерированный справочник 7","versions":[{"version":"3","actual_from_dt":"2022-03-10"},{"version":"2","actual_from_dt":"2022-03-05"},{"version":"1","actual_from_dt":"2022-02-28"}],"items":"http://127.0.0.1:8000/api/directories/10/items/"}
      ]
    }
    ```
* Получение элементов заданного справочника текущей версии
    ```
    GET http://localhost:8000/api/directories/4/items/
    ```

    Получим все элементы указанного справочника, т.е. и те, которые входят в последнюю версию (текущую), и те, которые были добавлены в предыдущих версиях.
    Вывод не полностью отформатирован для краткости:
    ```json
    {
      "count": 60,
      "next": "http://127.0.0.1:8000/api/directories/4/items/?page=2",
      "previous": null,
      "results": [
        {"id":56,"code":"Элемент 1","value":"Значение элемента 1","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":65,"code":"Элемент 10","value":"Значение элемента 10","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":66,"code":"Элемент 11","value":"Значение элемента 11","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":67,"code":"Элемент 12","value":"Значение элемента 12","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":68,"code":"Элемент 13","value":"Значение элемента 13","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":69,"code":"Элемент 14","value":"Значение элемента 14","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":70,"code":"Элемент 15","value":"Значение элемента 15","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":71,"code":"Элемент 16","value":"Значение элемента 16","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":72,"code":"Элемент 17","value":"Значение элемента 17","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":73,"code":"Элемент 18","value":"Значение элемента 18","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"}
      ]
    }
    ```
* Валидация элементов заданного справочника текущей версии
    ```
    POST http://localhost:8000/api/directories/4/items/validate/ 
    ```

    Тело запроса:
    ```json
    {
      "codes": [
        "Элемент 1", "Элемент 2", "Элемент 100500", "Элемент 20", "Элемент 30", "Элемент 100"
      ]
    }
    ```

    Для каждого указанного элемента получим ``true``, если он есть в справочнике и ``false`` в противном случае:
    ```json
    {
      "Элемент 1": true,
      "Элемент 2": true,
      "Элемент 100500": false,
      "Элемент 20": true,
      "Элемент 30": true,
      "Элемент 100": false
    }
    ```
* Получение элементов заданного справочника указанной версии
    ```
    GET http://localhost:8000/api/directories/4/items/?version=1
    ```

    Получим все элементы указанного справочника, которые были добавлены первой (1) версии.
    Вывод не полностью отформатирован для краткости:
    ```json
    {
      "count": 20,
      "next": "http://127.0.0.1:8000/api/directories/4/items/?page=2&version=1",
      "previous": null,
      "results": [
        {"id":56,"code":"Элемент 1","value":"Значение элемента 1","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":65,"code":"Элемент 10","value":"Значение элемента 10","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":66,"code":"Элемент 11","value":"Значение элемента 11","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":67,"code":"Элемент 12","value":"Значение элемента 12","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":68,"code":"Элемент 13","value":"Значение элемента 13","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":69,"code":"Элемент 14","value":"Значение элемента 14","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":70,"code":"Элемент 15","value":"Значение элемента 15","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":71,"code":"Элемент 16","value":"Значение элемента 16","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":72,"code":"Элемент 17","value":"Значение элемента 17","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"},
        {"id":73,"code":"Элемент 18","value":"Значение элемента 18","added_in":{"version":"1","actual_from_dt":"2022-02-28"},"directory":"http://127.0.0.1:8000/api/directories/4/"}
      ]
    }
    ```
* Валидация элементов заданного справочника по указанной версии
    ```
    POST http://localhost:8000/api/directories/4/items/validate/?version=1
    ```

    Тело запроса:
    ```json
    {
      "codes": [
        "Элемент 1", "Элемент 2", "Элемент 100500", "Элемент 20", "Элемент 30", "Элемент 100"
      ]
    }
    ```

    Для каждого указанного элемента получим ``true``, если он есть в справочнике указанной версии и ``false`` в противном случае.
    Как видно, элемента с кодом ``Элемент 30`` нет в указанном справочнике в первой (1) версии. Этот элемент был добавлен во второй (2) версии.
    ```json
    {
      "Элемент 1": true,
      "Элемент 2": true,
      "Элемент 100500": false,
      "Элемент 20": true,
      "Элемент 30": false,
      "Элемент 100": false
    }
    ```
* Валидация элемента заданного справочника по указанной версии
    ```
    POST http://localhost:8000/api/directories/4/items/validate/?version=2
    ```

    Тело запроса:
    ```json
    {
      "codes": [
        "Элемент 1"
      ]
    }
    ```

    Для валидации одного элемента достаточно указать только его в списке ``codes``:
    ```json
    {
      "Элемент 1": true
    }
    ```