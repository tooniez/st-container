# Default target to run all commands
all: stop remove build

# Refresh the local container
refresh: stop remove build run

# Start streamlit app
dev:
	streamlit run streamlit_app.py

# Stop and remove the container
stop:
	docker-compose down

# Rebuild Docker image
build:
	docker build --no-cache -t st-container:latest .

# Run the rebuilt container
run:
	docker compose up -d --force-recreate


remove:	
	docker rmi st-container:latest --force

.PHONY: dev refresh stop build run remove
