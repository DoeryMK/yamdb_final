# yamdb_final

## CI и CD проекта api_yamdb

## **Статус workflow**
![push to master](https://github.com/DoeryMK/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?event=push)

## **Краткое описание**
### _Цель проекта_
Для проекта API сервера обсуждения популярных произведений выполнена автоматизация процессов тестирования и деплоя на боевой сервер после выполнения PUSH в ветку master репозитория. 

### _Основные файлы_  
- yamdb_workflow.yaml - команды, выполняемые автоматически, для тестирования и деплоя проекта  
- Dockerfile - инструкции, которые используются для создания образа  
- Docker-compose.yaml - инструкции, которые используются для развертывания проекта в нескольких контейнерах: db, web, nginx  


### _Выполняемые инструкции workflow_
- Проверка кода на соответствие PEP8  
- Запуск pytest  
- Создание образа и загрузка на Docker Hub  
- Деплой проекта на боевой сервер  
- Отправка отчета об успешном выполнении workflow в чат telegram

## **Запуск проекта**
После выполнения push в репозиторий подключитесь к серверу и выполните слудующие команды в терминале:

1. Внутри контейнера web выполнить миграции
```
docker-compose exec web python manage.py migrate
```
2. Внутри контейнера web создать суперпользователя
```
docker-compose exec web python manage.py createsuperuser
```
3. Внутри контейнера web выполнить команду сбора статики
```
docker-compose exec web python manage.py collectstatic --no-input 
```
4. Внутри контейнера web выполнить команду для заполнения БД тестовыми данными
```
docker-compose exec web python manage.py import_data
```
Проект доступен по [адресу](https://ypyield.ddns.net/)

### _Документация_
(https://ypyield.ddns.net/redoc) 

## **Тестирование через HHTP-клиент**
Для тестирования работы API проекта можно воспользоваться HHTP-клиентом [Postman](https://www.postman.com) или [httpie](https://httpie.io). 

### Авторы: [DoeryMK](https://github.com/DoeryMK) 