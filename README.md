# 🚀 Docker Hands-on Workshop
## DevOps Food Ordering Application

This project demonstrates **Docker fundamentals using a simple microservices application**.

You will learn:

- Docker installation
- Docker images
- Docker containers
- Dockerfile
- Docker Compose
- Running multi-container applications

---

# 🏗️ Application Architecture


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


---

# 📁 Project Structure


docker-food-app
│
├── api
│ ├── app.py
│
├── frontend
│ ├── index.html
│ └── Dockerfile
│
├── Dockerfile
├── requirements.txt
└── docker-compose.yml


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
Mac

Install using Docker Desktop:

https://www.docker.com/products/docker-desktop

Verify installation:

docker --version
Linux (Ubuntu)

Run:

sudo apt update
sudo apt install docker.io -y

Start Docker:

sudo systemctl start docker

Enable Docker at startup:

sudo systemctl enable docker

Verify installation:

docker --version
2️⃣ Install Docker Compose

Check if Docker Compose is installed:

docker compose version

If not installed, run:

sudo apt install docker-compose -y
3️⃣ Clone the Project

Run:

git clone https://github.com/vaishnavisolanki07/devops-handson-workshops.git

Go to the project folder:

cd devops-handson-workshops/docker-food-app
4️⃣ Build the Application

Run:

docker compose build

This will:

build the frontend image

build the API image

5️⃣ Start the Application

Run:

docker compose up

Docker will start:

frontend container

api container

mysql container

6️⃣ Check Running Containers

Run:

docker ps

You should see containers like:

frontend
api
mysql
7️⃣ Access the Application

Open browser:

Frontend:

http://localhost:3000

API:

http://localhost:5000
8️⃣ Stop the Application

Press:

CTRL + C

Or run:

docker compose down
9️⃣ Useful Docker Commands
List Containers
docker ps
List Images
docker images
View Logs
docker logs <container_id>

Example:

docker logs api
Enter a Container
docker exec -it api bash
🔧 Troubleshooting
Docker not running

Start Docker Desktop or run:

sudo systemctl start docker
Port already in use

Check process using port:

lsof -i :3000

Kill process or change port in:

docker-compose.yml
Containers not starting

Check logs:

docker compose logs
Database connection error

Restart containers:

docker compose down
docker compose up

🎯 Learning Outcomes

After this workshop, you will understand:

How Docker works
How to build Docker images
How to run containers
How to connect multiple services using Docker Compose
How microservices run inside containers
