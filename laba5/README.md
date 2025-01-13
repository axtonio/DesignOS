# Laba5

## About

Телеграм бот с бд `Postgres`. Бот общается с `tg` и кладет инфу в `postgre`

## Build and Setup

### Docker

```sh
docker-compose up -d
```

### Kubernetes

Используем `minikube` для работы с `kuber`:

```sh
minikube start --mount --mount-string="<path_to_tracker_demo>:/minikubeContainer/tg_backend/"
# example: minikube start --mount --mount-string="/Users/antonio/Projects/Education/SberTech/DesignOS/laba5/tracker_bot_demo:/minikubeContainer/tg_backend/"
```

Отдельно по подам:

```sh
kubectl apply -f ./kubernetes/postgres-pod.yaml && kubectl apply -f ./kubernetes/bot-pod.yaml
```

Deployment:

```sh
kubectl apply -f ./kubernetes/deployment.yaml
```

## Media

Видео с работой: [media](./media/)