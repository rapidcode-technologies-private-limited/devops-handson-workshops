# 🚀 Docker Hands-on Workshop
## DevOps Food Ordering Application

This project demonstrates Docker fundamentals using a simple microservices application.

Participants will learn:

- Docker installation
- Docker images
- Docker containers
- Dockerfile
- Docker Compose
- Running multi-container applications

---

# 🏗 Application Architecture

```
Browser
   │
   ▼
Frontend (Nginx)
   │
   ▼
API Service (Python Flask)
   │
   ▼
MySQL Database
```

---

# 📁 Project Structure

```
docker-food-app
│
├── api
│   └── app.py
│
├── frontend
│   ├── index.html
│   └── Dockerfile
│
├── Dockerfile
├── requirements.txt
└── docker-compose.yml
```

---

# 1️⃣ Install Docker

## Windows

Download Docker Desktop:

https://www.docker.com/products/docker-desktop

Steps:

1. Install Docker Desktop
2. Restart your system
3. Start Docker Desktop

Verify installation:

```bash
docker --version
```

---

## Mac

Download Docker Desktop:

https://www.docker.com/products/docker-desktop

Verify installation:

```bash
docker --version
```

---

## Linux (Ubuntu)

Run:

```bash
sudo apt update
sudo apt install docker.io -y
```

Start Docker:

```bash
sudo systemctl start docker
```

Enable Docker at startup:

```bash
sudo systemctl enable docker
```

Verify installation:

```bash
docker --version
```

---

# 2️⃣ Install Docker Compose

Check if Docker Compose is installed:

```bash
docker compose version
```

If not installed:

```bash
sudo apt install docker-compose -y
```

---

# 3️⃣ Clone the Project

```bash
git clone https://github.com/rapidcode-technologies-private-limited/devops-handson-workshops.git
```

Go to the project folder:

```bash
cd devops-handson-workshops/docker-food-app
```

---

# 4️⃣ Build the Application

```bash
docker compose build
```

This will build the frontend and API images.

---

# 5️⃣ Start the Application

```bash
docker compose up
```

Docker will start:

- frontend container
- api container
- mysql container

---

# 6️⃣ Check Running Containers

```bash
docker ps
```

You should see containers similar to:

```
frontend
api
mysql
```

---

# 7️⃣ Access the Application

Open in your browser:

Frontend:

```
http://localhost:3000
```

API:

```
http://localhost:5000
```

---

# 8️⃣ Stop the Application

Press:

```
CTRL + C
```

Or run:

```bash
docker compose down
```

---

# 9️⃣ Useful Docker Commands

### List containers

```bash
docker ps
```

### List images

```bash
docker images
```

### View container logs

```bash
docker logs <container_id>
```

Example:

```bash
docker logs api
```

### Enter a container

```bash
docker exec -it api bash
```

---

# 🔧 Troubleshooting

## Docker not running

Start Docker Desktop or run:

```bash
sudo systemctl start docker
```

---

## Port already in use

Check which process is using the port:

```bash
lsof -i :3000
```

Kill the process or change the port in:

```
docker-compose.yml
```

---

## Containers not starting

Check logs:

```bash
docker compose logs
```

---

## Database connection error

Restart containers:

```bash
docker compose down
docker compose up
```

---

# 🎯 Learning Outcomes

After this workshop, you will understand:

- How Docker works
- How to build Docker images
- How to run containers
- How to connect multiple services using Docker Compose
- How microservices run inside containers

---

# 👩‍💻 Author
QT
DevOps Hands-on Workshop
