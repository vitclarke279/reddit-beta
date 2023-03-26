start:
	docker-compose up --build

shell:
	docker-compose up -d
	docker-compose exec backend /bin/bash
