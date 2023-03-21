Для запуска проекта в докер контейнере необходимо выполнить следующие шаги:

1. скачать проект и перейти в директорию "hw-drf"
2. прописать в консоли команду: docker run --name python --network host -v ${PWD}:/hw -it python:3.10.10 bash
3. после запуска контейнера перейти в директорию "hw"
4. установить зависимости проекта: pip install -r requirements.txt
5. выполнить миграции: python3 manage.py migrate
6. запустить сервер: python3 manage.py runserver


При необходимости запуска постгрес через докер, остановите контейнер python (docker stop python) и выполните следующие шаги:

1. прописать в консоли команду: 
docker run --name db_django -e POSTGRES_PASSWORD=postgres -d -p 5433:5432 -v /home/<username>/db_proj:/var/lib/postgresql/data postgres
(команда скачает образ последней верии postgres, запустит контейнер и сохранит данные в директории /home/<username>/db_proj)
2. подключиться к БД контейнера postgres: docker exec -it <id контейнера> psql -U postgres
3. создать базу данных: create database drf_base;
4. запустить контейнер с проектом: docker start python
