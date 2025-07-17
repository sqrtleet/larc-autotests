COMPOSE=docker compose -f docker-compose.yml

up:
	$(COMPOSE) up --build -d

down:
	$(COMPOSE) down -v --remove-orphans

logs:
	$(COMPOSE) logs -f

logs-api:
	$(COMPOSE) logs backend

logs-db:
	$(COMPOSE) logs postgres

shell:
	$(COMPOSE) exec backend sh

ps:
	$(COMPOSE) ps

ping-db:
	$(COMPOSE) exec postgres pg_isready -U test

rebuild:
	$(COMPOSE) down -v --remove-orphans && $(COMPOSE) up --build -d