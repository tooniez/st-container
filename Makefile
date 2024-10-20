# Default target to run all commands
all: stop build run remove


# Stop and remove the container
stop:
	docker-compose down

# Rebuild Docker image
build:
	docker build --no-cache -t st-container:latest .

# Run the rebuilt container
run:
	docker compose up -d --force-recreate st-container


remove:	
	docker rmi st-container:latest

.PHONY: all stop run remove
