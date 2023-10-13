create_env:
	touch .env
	echo "POSTGRES_USER=postgres\nPOSTGRES_PASSWORD=postgres\nPOSTGRES_DB=postgres\nPOSTGRES_PORT=5432\nPOSTGRES_HOST=db\nAPP_PORT=8000"
up:
	docker compose -f docker-compose-dev.yaml up -d
down:
	docker compose -f docker-compose-dev.yaml down