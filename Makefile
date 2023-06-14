.PHONE: start stop format lint

start:
	@docker-compose up -d
	flask run --debug

stop:
	@docker-compose down

format:
	./bin/format.sh

lint:
	./bin/lint.sh
