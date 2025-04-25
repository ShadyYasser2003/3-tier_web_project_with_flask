## Documentation: Pet Voting Application (Cat vs. Dog)

### Project Overview

A 3-tier web application enabling users to vote for cats or dogs. Leverages Docker, Kubernetes, ArgoCD, and GitHub for containerization, orchestration, continuous deployment, and version control, respectively.

### Architecture and Technologies

**1. 3-Tier Architecture**

* **1.1 Frontend (Presentation Layer)**
    * **Role:** User interface for voting and displaying results.
    * **Technology:** HTML, CSS, JavaScript.
    * **Responsibility:** UI rendering, vote submission (API calls), result display.
* **1.2 Backend (Business Logic Layer)**
    * **Role:** Vote processing and data retrieval.
    * **Technology:** Flask (Python).
    * **Key Functions:** RESTful API endpoints for voting (POST) and results (GET), vote validation, Redis interaction.
* **1.3 Database (Data Layer)**
    * **Role:** Vote count persistence.
    * **Technology:** Redis (in-memory key-value store).
    * **Key Operations:** Atomic increment/retrieval of vote counts per pet.

### Deployment and DevOps

* **2.1 Docker**
    * Containerization of frontend, backend, and Redis services for environment consistency and isolated execution.
* **2.2 Kubernetes**
    * Container orchestration platform for deployment, scaling, and high availability of application services.
* **2.3 ArgoCD (Continuous Deployment)**
    * GitOps-based CD tool for automated application deployment and synchronization with the GitHub repository within the Kubernetes cluster.
* **2.4 GitHub**
    * Distributed version control system for collaborative code management and change tracking.

### How It Works

1.  **Frontend:** User interaction triggers API calls to the backend for voting.
2.  **Backend:** Flask API receives votes, updates Redis counters, and serves real-time vote counts.
3.  **Database:** Redis persists and provides fast access to vote data.

### Conclusion

The Pet Voting Application exemplifies a modular 3-tier architecture deployed with modern DevOps practices, emphasizing scalability, maintainability, and continuous delivery.
