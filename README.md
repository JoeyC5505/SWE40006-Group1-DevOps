
# SWE40006 Group 1 — DevOps Deployment Pipeline

## Project Overview

This project was developed by Group 1 for SWE40006 Software Deployment and Evolution at Swinburne University of Technology.

Our team designed and implemented a Level 4 DevOps pipeline for a Student Task Management System. The pipeline automates the software build, testing and deployment process using GitHub, Jenkins, Docker and Ubuntu Server virtual machines.

The project also incorporates production performance monitoring using Prometheus, Grafana and Node Exporter to monitor the health and performance of the production server.

**Target Level:** Level 4  
**Application:** Student Task Management System  
**Project Status:** Implementation and Testing Completed

---

## Student Task Management System

The application is developed using Python Flask and SQLite.

The main features include:

- Create new tasks with a title and description.
- View existing tasks.
- Edit task information.
- Mark tasks as completed or pending.
- Delete tasks.
- Assign task priorities (High, Medium and Low).
- Verify application availability through the `/health` endpoint.

The application has been successfully developed and tested. All nine automated pytest tests passed locally and through the Jenkins CI/CD pipeline on VM2. The application was successfully deployed to VM3 using Docker Compose.

---

## Technologies Used

| Tool | Purpose |
|---|---|
| Git and GitHub | Source code management and team collaboration |
| VMware / VirtualBox | Virtual machine environments |
| Ubuntu Server | Server operating system |
| Jenkins | CI/CD pipeline automation |
| Docker | Application containerisation and deployment |
| Docker Compose | Container configuration and management |
| Python Flask | Web application development |
| SQLite | Application data storage |
| pytest | Automated testing |
| Prometheus | Production server performance monitoring |
| Grafana | Monitoring dashboard and data visualisation |
| Node Exporter | Collection of Linux server metrics |

---

## DevOps Architecture

The project uses three virtual machines, each assigned a specific responsibility.

| Server | Responsibility |
|---|---|
| VM1 — Jenkins Server | CI/CD orchestration and deployment coordination |
| VM2 — Test Server | Jenkins agent, Docker image build and automated pytest execution |
| VM3 — Production Server | Hosting the deployed Flask application |

### Deployment Workflow

```text
Developer
    |
    v
GitHub Repository
    |
    v
Jenkins Controller (VM1)
    |
    v
Test Server (VM2)
Docker Build + 9 Automated pytest Tests
    |
    v
Tests Passed
    |
    v
Production Server (VM3)
SSH + Docker Compose Deployment
    |
    v
Running Flask Application
    |
    v
Production Monitoring
Node Exporter + Prometheus + Grafana
```

The Jenkins controller on VM1 coordinates the pipeline. VM2 acts as the build and testing agent, while VM3 hosts the production application.

The production deployment stage is executed after the automated tests pass. Production performance is monitored using Node Exporter, Prometheus and Grafana.

---

## Project Levels

### Level 1 — DevOps Infrastructure

The team established a complete DevOps environment consisting of:

- GitHub source code repository.
- VM1 Jenkins controller.
- VM2 build and test server.
- VM3 production server.
- SSH connectivity between the relevant environments.

The separate virtual machines provide isolated environments for building, testing and deploying the application.

### Level 2 — Production Monitoring

The production server is monitored using Node Exporter, Prometheus and Grafana.

- Node Exporter collects Linux server metrics from VM3.
- Prometheus collects and stores production performance data.
- Grafana displays CPU usage, memory usage, disk usage and server availability.

### Level 3 — Application Deployment

The Flask Student Task Management System was successfully deployed through the Jenkins pipeline.

- The application was packaged using Docker.
- All nine automated pytest tests passed on VM2.
- The application was deployed to VM3 using Docker Compose.
- The production application was accessible through a web browser.
- The `/health` endpoint returned a successful HTTP 200 response.

### Level 4 — Automated Deployment

The team implemented a CI/CD workflow that supports deployment following source-code changes.

The workflow includes:

1. Updating the application source code in GitHub.
2. Triggering the Jenkins pipeline.
3. Building the application Docker image on VM2.
4. Running automated pytest tests.
5. Deploying the application to VM3 after successful testing.
6. Verifying the updated production application and monitoring results.

The team has completed the integration and deployment testing for the Level 4 workflow.

---

## Team Members and Responsibilities

| Member | Name | Responsibility |
|---|---|---|
| 1 | Chan Kar Yan | GitHub repository management, Pull Request reviews, team coordination, documentation and presentation preparation |
| 2 | Yong Khai Cheik | VM1 and VM2 setup, Ubuntu, Jenkins installation, Docker, SSH and networking |
| 3 | Charya Kavingi Mayadunna Dissawage | Flask application development, SQLite integration and automated pytest testing |
| 4 | Raqibul Hasan | Jenkins CI/CD pipeline, Docker configuration, VM3 production server and automated deployment |
| 5 | Lee Ren Qi | Prometheus, Grafana, Node Exporter and production performance monitoring |

---

## Implementation and Individual Contributions

### 1. GitHub Repository and Team Integration — Chan Kar Yan

The GitHub repository provides a central platform for source code management, collaboration and project integration.

Main contributions:

- Established and managed the shared GitHub repository.
- Invited team members and configured repository collaboration.
- Organised feature branches for application development, Jenkins, Docker and monitoring.
- Reviewed Pull Requests and coordinated the integration of individual contributions.
- Communicated with team members regarding task allocation, project progress and integration issues.
- Reviewed the project structure and identified differences between development and deployment configurations.
- Collected project evidence and prepared the presentation slides.
- Organised presentation responsibilities and the live demonstration workflow.

**Supporting evidence:** GitHub repository, collaborator list, feature branches, commits, merged Pull Requests, team discussions and presentation materials.

### 2. VM Infrastructure and Networking — Yong Khai Cheik

VM1 and VM2 provide the infrastructure required for CI/CD orchestration, Docker builds and automated testing.

| Environment | Configuration |
|---|---|
| VM1 | Ubuntu Server, Jenkins controller and required plugins |
| VM2 | Ubuntu Server, Docker, Docker Compose, Java 21 and Jenkins build/test agent |

Main contributions:

- Installed and configured Ubuntu Server on VM1 and VM2.
- Installed Jenkins and configured the CI/CD infrastructure.
- Installed Docker and Docker Compose on VM2.
- Configured the Jenkins agent using the label `vm2-docker`.
- Established SSH connectivity between the virtual machines.
- Configured passwordless SSH authentication and supported Jenkins credentials setup.
- Worked with Raqibul to resolve networking and connectivity issues between the servers.
- Supported Docker builds, automated testing and end-to-end pipeline verification.

**Supporting evidence:** VM installation screenshots, Jenkins dashboard, agent configuration, SSH connectivity, Docker service status and pipeline testing results.

### 3. Flask Application and Automated Testing — Charya Kavingi Mayadunna Dissawage

The Student Task Management System was developed using Python Flask and SQLite to provide a functional application for the DevOps deployment pipeline.

Main contributions:

- Developed the Flask web application and user interface.
- Implemented SQLite database integration.
- Developed task creation, viewing, editing and deletion functionality.
- Implemented task completion status and priority management.
- Developed the `/health` endpoint to verify application availability.
- Created nine automated pytest tests to verify application functionality.
- Verified the application and automated tests in the local development environment.
- Supported Docker packaging and application integration with the Jenkins pipeline.

**Testing results:** All nine automated tests passed locally and during the Jenkins pipeline testing on VM2.

**Relevant project files:**

- `app/`
- `run.py`
- `requirements.txt`
- `tests/`

**Supporting evidence:** Flask source code, application screenshots, automated pytest results and health endpoint verification.

### 4. Jenkins CI/CD and Production Deployment — Raqibul Hasan

The Jenkins pipeline automates application building, testing and production deployment. VM3 provides the production environment for the Flask application.

#### Jenkins Pipeline Stages

| Stage | Execution Environment | Description |
|---|---|---|
| Clone | VM2 | Retrieve the application source code from GitHub |
| Build | VM2 | Build the application Docker image |
| Test | VM2 | Execute automated pytest tests inside the Docker container |
| Deploy to Production | VM1 to VM3 | Connect through SSH and deploy the application using Docker Compose |

Main contributions:

- Configured the Jenkins Build, Test and Deploy pipeline.
- Created and maintained Docker deployment configurations.
- Installed Ubuntu Server and Docker on VM3.
- Configured SSH access for Jenkins production deployment.
- Resolved Docker container startup and application configuration issues.
- Configured the production deployment process using Docker Compose.
- Verified that the application was accessible on the production server.
- Verified the `/health` endpoint returned HTTP 200 with a healthy status.
- Installed Node Exporter on VM3 and supported monitoring integration with Ren Qi.
- Completed pipeline integration and deployment testing with Yong.

**Relevant project files:**

- `Jenkinsfile`
- `Dockerfile`
- Docker Compose configuration
- Deployment scripts

**Supporting evidence:** Jenkins pipeline stages, console output, Docker container status, production application screenshots and health check results.

### 5. Production Monitoring — Lee Ren Qi

The production monitoring system provides visibility into the health and performance of VM3.

#### Monitoring Architecture

```text
VM3 Production Server
        |
        v
Node Exporter (Port 9100)
        |
        v
Prometheus (Port 9090)
        |
        v
Grafana (Port 3000)
        |
        v
Production Monitoring Dashboard
```

Main contributions:

- Configured Prometheus to collect production server metrics.
- Configured the Grafana data source and monitoring dashboard.
- Created the Production Server Monitoring dashboard.
- Configured production server monitoring for CPU usage, memory usage, disk usage and node availability.
- Coordinated Node Exporter connectivity with Raqibul.
- Verified that the Prometheus production server target was UP.
- Maintained the monitoring configuration, dashboard JSON export and installation instructions.
- Supported monitoring integration during project testing.

#### Monitoring Components

| Component | Port | Responsibility |
|---|---|---|
| Node Exporter | 9100 | Collects Linux server performance metrics |
| Prometheus | 9090 | Collects and stores monitoring metrics |
| Grafana | 3000 | Displays production monitoring dashboards |

**Relevant project files:**

- `monitoring/prometheus.yml`
- `monitoring/production-server-monitoring.json`
- `monitoring/README.md`

**Supporting evidence:** Prometheus Targets page, Grafana dashboard screenshots, Node Exporter metrics and monitoring configuration files.

---

## Final Implementation and Testing Results

| Component | Final Status |
|---|---|
| GitHub repository and collaboration | Completed |
| Flask application development | Completed |
| Local automated testing | All 9 tests passed |
| VM1 — Jenkins Server | Configured and operational |
| VM2 — Build and Test Server | Configured and operational |
| VM3 — Production Server | Configured and operational |
| SSH connectivity | Configured and tested |
| Docker image build | Successfully completed |
| Jenkins automated testing | All 9 tests passed |
| Jenkins production deployment | Successfully tested |
| Production application access | Verified |
| Production health check | HTTP 200 — Healthy |
| Node Exporter | Running |
| Prometheus | Production target UP |
| Grafana dashboard | Operational |
| Level 4 integration and deployment testing | Completed |

The team completed the integration testing of the CI/CD pipeline and verified the operation of the production application.

The testing results demonstrate that the application can be built, tested and deployed through the implemented DevOps infrastructure.

---

## Production Deployment Verification

The Flask application is hosted on VM3 using Docker.

The production environment was verified through:

- Successful Docker Compose deployment.
- Running application container.
- Browser access to the Student Task Management System.
- Successful application health endpoint response.
- Production server performance monitoring.

### Application Health Check

```json
{
  "status": "healthy"
}
```

HTTP Status: `200 OK`

### Network Configuration

The most recently documented VM3 IP address is:

```text
172.20.10.3
```

Production application:

```text
http://172.20.10.3:5000
```

Node Exporter:

```text
http://172.20.10.3:9100/metrics
```

The virtual machines use a shared network for communication. If the production server IP address changes, the Jenkins production host configuration and Prometheus monitoring target must be updated accordingly.

---

## Development Workflow

Each team member worked on a separate feature branch to support parallel development and reduce integration conflicts.

| Branch | Purpose |
|---|---|
| `main` | Integrated project source code |
| `feature/jenkins` | Jenkins CI/CD configuration |
| `feature/flask-app` | Flask application and automated tests |
| `feature/docker` | Docker and production deployment configuration |
| `feature/monitoring` | Prometheus, Grafana and Node Exporter monitoring configuration |

The development workflow includes:

1. Create or update the relevant feature branch.
2. Implement and test the assigned component.
3. Commit and push changes to GitHub.
4. Create a Pull Request for review.
5. Integrate approved changes into the project.
6. Perform integration testing and deployment verification.

Passwords, SSH private keys, personal access tokens and other sensitive credentials must not be committed to the repository.

---

## Team Collaboration and Integration

All five team members collaborated throughout the development and testing process.

Chan Kar Yan managed the GitHub repository, coordinated task allocation, reviewed Pull Requests and organised the presentation.

Yong Khai Cheik and Raqibul Hasan worked together to configure the virtual machine environments, Jenkins connectivity, Docker builds, automated testing and production deployment.

Charya Kavingi Mayadunna Dissawage supplied the Flask application and automated pytest tests required for application integration.

Lee Ren Qi collaborated with Raqibul Hasan to configure production monitoring, verify Node Exporter connectivity and display production server metrics using Prometheus and Grafana.

The team communicated regularly, reviewed individual progress, resolved integration issues and prepared the final project demonstration.

---

## Challenges and Solutions

| Challenge | Solution |
|---|---|
| High memory usage when running multiple virtual machines | Reduced unnecessary background processes and coordinated VM resource usage |
| Network connectivity between different virtual machines and laptops | Configured shared network connectivity and verified SSH communication |
| Docker container startup issues | Corrected application startup configuration and rebuilt the container |
| Differences between development and deployment configurations | Coordinated GitHub integration and reviewed application compatibility |
| Changing production server IP address | Updated Jenkins deployment settings and Prometheus monitoring targets |
| Integrating individual project components | Used GitHub feature branches, Pull Requests and team integration testing |

These challenges provided practical experience in troubleshooting software deployment, infrastructure configuration and collaborative DevOps development.

---

## Final Presentation and Demonstration

The final presentation demonstrates the completed DevOps implementation.

1. Introduce the project background, objectives and team responsibilities.
2. Show the GitHub repository, source code and development workflow.
3. Explain the Flask application and automated pytest tests.
4. Demonstrate the Jenkins pipeline and Docker build on VM2.
5. Show all nine automated tests passing.
6. Demonstrate production deployment to VM3.
7. Demonstrate the source-code change and automated or deferred deployment workflow.
8. Verify the updated production application and health endpoint.
9. Show Prometheus and Grafana production monitoring.
10. Discuss implementation challenges, solutions and lessons learned.

### Presentation Responsibilities

| Member | Presentation Responsibility |
|---|---|
| Chan Kar Yan | Project introduction, background, scope, GitHub and team coordination |
| Yong Khai Cheik | VM infrastructure, networking and build/test environment |
| Charya Kavingi Mayadunna Dissawage | Flask application and automated testing |
| Raqibul Hasan | Jenkins pipeline, Docker and production deployment |
| Lee Ren Qi | Design compatibility and production monitoring |

---

## Project Deliverables

- Project Brief
- GitHub source code repository
- Flask Student Task Management System
- SQLite database integration
- Automated pytest test suite
- Docker configuration
- Docker Compose configuration
- Jenkins CI/CD pipeline
- Three virtual machine environments
- Production deployment configuration
- Prometheus monitoring configuration
- Node Exporter configuration
- Grafana monitoring dashboard and JSON export
- Monitoring setup documentation
- Level 4 deployment demonstration
- Project presentation
- Contribution document and supporting evidence

---

## Conclusion

This project demonstrates the implementation of a complete DevOps deployment pipeline for a Student Task Management System.

The team successfully integrated GitHub, Jenkins, Docker, Ubuntu Server, Flask, SQLite, pytest, Prometheus, Grafana and Node Exporter into a working deployment and monitoring environment.

The Jenkins pipeline uses VM1 for orchestration, VM2 for application building and automated testing, and VM3 for production deployment. All nine automated tests passed, and the application was successfully deployed to the production server.

The project provided practical experience in source code management, infrastructure configuration, automated testing, continuous integration, software deployment, production monitoring and team collaboration.

**Final Project Status: Level 4 Implementation and Testing Completed**

---

## Acknowledgement

This project was completed by Group 1 for SWE40006 Software Deployment and Evolution at Swinburne University of Technology.

We would like to thank our tutor, Dr Ruby Tinawin, for her guidance and support throughout the project.
