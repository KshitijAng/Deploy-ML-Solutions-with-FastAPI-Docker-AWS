# 🔍 YouTube Search API - ML Model Deployment on AWS (FastAPI + Docker + ECS)

This project demonstrates how to **deploy a Machine Learning (ML) solution on AWS** using FastAPI, Docker, and Amazon ECS (Elastic Container Service). The deployed API performs semantic search using `all-MiniLM-L6-v2` from [SentenceTransformers](https://www.sbert.net/), allowing for fast and accurate text-based querying.

---

# 🚀 Project Highlights

- ✅ ML model wrapped in a FastAPI-based RESTful API
- ✅ Dockerized for portability and ease of deployment
- ✅ Hosted on **AWS ECS with Fargate**, a serverless compute engine
- ✅ Docker image pushed to DockerHub for seamless cloud integration

---

# 📦 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) — for building the API
- [SentenceTransformers](https://www.sbert.net/) — for semantic search embeddings
- [Docker](https://www.docker.com/) — for containerization
- [AWS ECS](https://aws.amazon.com/ecs/) — for cloud deployment
- [DockerHub](https://hub.docker.com/) — for hosting Docker images

---

# ![image](https://github.com/user-attachments/assets/95f8c559-b719-4172-8753-771f979f7874) Docker Commands
The following commands were run to create, test and push the image to the [DockerHub](https://hub.docker.com/explore)
1. Create Docker Image
```
docker build -t yt-search .
```
2. Run the container from the image
```
docker run -d --name test -p 8000:80 yt-search
```

## 📤 Push to DockerHub
3. Tag the Docker Image
```
docker tag yt-search <your-dockerhub-username>/yt-search-deployment
```

4. Push to DockerHub
```
docker push <your-dockerhub-username>/yt-search-deployment
```

---

# ☁️ Deploy on AWS ECS with Fargate
## 1. Create a Task Definition
- Go to the AWS ECS dashboard

- Click Create new Task Definition

- Select Fargate as the launch type

- Define the container using your DockerHub image (keep rest as default)

## 2. Create a Cluster
- Go to Clusters and click Create Cluster

- Name it (e.g., yt-search-cluster)

- Choose Networking only (Fargate) as the template

## 3. Create a Service
- Under the newly created cluster, click Create Service

- Attach it to your Task Definition

- Choose the desired number of tasks and subnets (keep rest as default)

## 4. Update Security Group
- Under Services, go to Configuration & Networking > Security Groups

- Edit Inbound Rules to allow traffic on port 80 or 8000

---

# 🙌 Acknowledgements

This project is a result of my exploration into productionizing ML solutions and cloud deployment practices. Big thanks to [Shaw Talebi](https://www.youtube.com/watch?v=pJ_nCklQ65w) for the tutorial and open-source tools like FastAPI, Docker, and AWS ECS.


