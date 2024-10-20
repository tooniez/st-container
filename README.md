<h1 align="center">Streamlit Container App 🐳📊</h1>

<h2 align="center">Containerized Streamlit app with Docker and Docker Compose</h2>

<!-- Badges -->
<p align="center">
<img src="https://img.shields.io/badge/Docker-blue" alt="Docker" />
<img src="https://img.shields.io/badge/Docker%20Compose-blue" alt="Docker Compose" />
<img src="https://img.shields.io/badge/Streamlit-red" alt="Streamlit" />
<img src="https://img.shields.io/badge/Make-yellow" alt="Make" />
</p>

## Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Available Commands](#available-commands)
4. [Usage](#usage)
5. [Docker Compose Configuration](#docker-compose-configuration)
6. [Customization](#customization)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

This project uses Docker and Docker Compose to manage the development and deployment process of a containerized Streamlit app. The Makefile provides convenient commands to manage the Docker container.

## Prerequisites

- Docker
- Docker Compose
- Make

## Available Commands

The following commands are available through the Makefile:

### `make all`

This is the default command that runs the following sequence:
1. Stops the existing container
2. Rebuilds the Docker image
3. Runs the rebuilt container

### `make stop`

Stops and removes the Docker container.

### `make build`

Rebuilds the Docker image without using cache.

### `make run`

Runs the rebuilt Docker container in detached mode.

### `make remove`

Removes the Docker image.

## Usage

To use these commands, simply run `make all` followed by the command name. For example:


This will execute the default sequence of stopping the container, rebuilding the image, and running the rebuilt container.

## Docker Compose Configuration

The project uses a Docker Compose configuration file (`docker-compose.yml`) to define the service. The main service is named `st-container`.

## Customization

You can modify the Makefile to add more commands or adjust the existing ones according to your project needs.

## Contributing

If you want to contribute to this project, please make sure to follow the existing code style and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
