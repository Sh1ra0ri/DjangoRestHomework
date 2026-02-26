## Запуск проекта

### 1. Клонировать репозиторий
```bash
git clone <ссылка на репозиторий>
cd <папка проекта>
```

### 2. Создать .env файл
```bash
cp .env.example .env
```

### 3. Запустить
```bash
docker-compose up --build
```

### 4. Проверка сервисов
- **web** — http://localhost:8000
- **db** — docker-compose logs db
- **redis** — docker-compose logs redis
- **celery** — docker-compose logs celery
- **celery_beat** — docker-compose logs celery_beat

### 5. Остановить
```bash
docker-compose down
```