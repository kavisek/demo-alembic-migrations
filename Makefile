# DOCKER COMPOSE COMMANDS

.PHONY: stop
stop:
	docker-compose down

.PHONY: start
start: stop
	docker-compose --profile app up

