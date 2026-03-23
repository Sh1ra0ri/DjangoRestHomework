## Настройка CI/CD и деплоя на сервер

### Секреты GitHub Actions
Добавь в Settings → Secrets and variables → Actions:

| Секрет | Описание |
|---|---|
| `SERVER_HOST` | IP-адрес сервера |
| `SERVER_USER` | Пользователь SSH (например, `ubuntu`) |
| `SSH_PRIVATE_KEY` | Приватный SSH-ключ |

### Подготовка сервера
```bash
# Установить Docker
sudo apt update && sudo apt install -y docker.io docker-compose-plugin

# Клонировать репозиторий
git clone https://github.com/Sh1ra0ri/DjangoRestHomework ~/app
cd ~/app

# Создать .env файл
cp .env.example .env
nano .env

# Первый запуск
docker compose up -d --build
```

### Как работает CI/CD
После каждого `push` в ветку `develop` автоматически:
1. Запускаются тесты
2. Проверяется сборка Docker-образов
3. Проект деплоится на сервер
