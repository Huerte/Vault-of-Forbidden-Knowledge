[← Back to README](../README.md) | [Contributing Guide](../CONTRIBUTING.md)

---

# Docker Basics Cheatsheet (Quick Reference)

A quick reference guide for essential Docker commands used daily.

---

## 1. Container Management
```bash
docker run -d -p 8080:80 --name my-app nginx    # Start a container in detached mode with port mapping
docker ps                                      # List running containers
docker ps -a                                   # List all containers (running and stopped)
docker stop my-app                             # Stop a running container
docker start my-app                            # Start a stopped container
docker rm my-app                               # Remove a container
```

---

## 2. Logs and Debugging
```bash
docker logs -f my-app                          # Stream logs for a container
docker exec -it my-app bash                    # Execute interactive bash shell inside container
docker inspect my-app                          # View detailed container metadata
```

---

## 3. Image Operations
```bash
docker build -t my-app:v1 .                    # Build image from Dockerfile in current directory
docker images                                  # List local Docker images
docker rmi my-app:v1                           # Delete local image
docker pull nginx                              # Pull image from Docker Hub registry
```

---

## 4. Docker Compose
```bash
docker compose up -d                           # Build and start multi-container services in background
docker compose down                            # Stop and remove containers and networks
docker compose logs -f                         # Stream logs from all compose services
```
