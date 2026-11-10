# SWE40006 Group 1 — DevOps Deployment Pipeline

## Project Overview

This project is developed by Group 1 for SWE40006 Software Deployment and Evolution at Swinburne University of Technology.

Our objective is to design and implement a Level 4 DevOps pipeline for a Student Task Management System. The pipeline aims to automate the software build, testing and deployment process using GitHub, Jenkins, Docker and Ubuntu Server virtual machines.

The project also includes production performance monitoring using Prometheus and Grafana.

**Target Level:** Level 4  
**Application:** Student Task Management System  
**Project Status:** Development and Integration in Progress

## Student Task Management System

The application is developed using Python Flask and SQLite.

Main features include:

- Create new tasks with a title and description.
- View existing tasks.
- Edit task information.
- Mark tasks as completed or pending.
- Delete tasks.
- Assign task priorities (High, Medium and Low).
- Verify application availability through the `/health` endpoint.

The application has been developed and all 9 automated pytest tests have passed in the developer's local environment. Testing through the complete Jenkins pipeline is still pending.

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
| Grafana | Monitoring dashboard |
| Node Exporter | Collection of Linux server metrics |

## Proposed DevOps Architecture

The project uses three virtual machines:

| Server | Responsibility |
|---|---|
| VM1 — Jenkins Server | CI/CD orchestration, building and deployment automation |
| VM2 — Test Server | Application testing and verification |
| VM3 — Production Server | Hosting the deployed Flask application |

The planned deployment workflow is:

Developer → GitHub → Jenkins (VM1) → Test Server (VM2) → Production Server (VM3)

Production server performance will be monitored using Node Exporter, Prometheus and Grafana.

## Project Levels

**Level 1 — DevOps Infrastructure**

Establish a GitHub repository, CI/build server, test server and production server.

**Level 2 — Production Monitoring**

Configure monitoring to collect server performance metrics and display them using Grafana.

**Level 3 — Application Deployment**

Deploy the Flask application through the pipeline and verify that it is accessible and functioning correctly.

**Level 4 — Automated Deployment**

Demonstrate that a source-code change triggers an automatic or deferred pipeline execution, including build, testing and production deployment.

## Team Members and Responsibilities

| Member | Name | Responsibility |
|---|---|---|
| 1 | Chan Kar Yan | GitHub repository management, Pull Request review, team coordination and evidence collection |
| 2 | Yong Khai Cheik | VM1 and VM2 setup, Ubuntu, Jenkins installation, Docker, Docker Compose and SSH |
| 3 | Charya Kavingi Mayadunna Dissawage | Flask application development, SQLite integration and pytest |
| 4 | Raqibul Hasan | VM3, Jenkins Pipeline configuration, automated Build/Test and Production Deployment |
| 5 | Lee Ren Qi | Prometheus, Grafana, Node Exporter and production monitoring |

All team members will support integration testing, troubleshooting, documentation and final presentation preparation.

## Current Development Progress

| Component | Current Status |
|---|---|
| GitHub repository and collaboration | Completed |
| Flask application development | Completed |
| Local automated testing | 9 tests passed |
| VM1 — Jenkins Server | Basic setup completed |
| VM2 — Test Server | Basic setup completed |
| VM1 to VM2 manual SSH connection | Verified |
| VM3 — Production Server | Initial Docker deployment demonstrated |
| Jenkins automated Build/Test/Deploy | In progress |
| Node Exporter on VM3 | Running; metrics reachable on port 9100 |
| Prometheus and Grafana configuration files | Uploaded (`monitoring/` folder on `feature/monitoring`) |
| Production monitoring integration | Verified: Prometheus collects VM3 metrics and Grafana displays them. Post-deployment verification pending |
| Level 4 automatic deployment | Not yet verified |

*This progress summary reflects the team's reported work. Successful installation does not necessarily mean end-to-end pipeline integration has been completed.*

## Monitoring

Monitoring components:

- Node Exporter on VM3 — Port 9100
- Prometheus — Port 9090
- Grafana — Port 3000

**Current status**

- Node Exporter is running on VM3, and its metrics were verified from the monitoring machine.
- Prometheus is configured with a `production-server` job targeting VM3 (`172.20.10.3:9100`). The Prometheus Target health page shows the target as **UP**.
- Grafana is connected to Prometheus. The "Production Server Monitoring" dashboard displays CPU usage, memory usage, disk usage and node availability from live data.
- The configuration files, dashboard export and setup guide are in the `monitoring/` folder (see `monitoring/README.md`).

**Current limitations**

- Prometheus and Grafana currently run on the owner's laptop, on the same hotspot as VM3. The team still needs to decide whether to move them to VM1 for the final demonstration.
- VM3's address is assigned by the hotspot, so it may change. If it does, the target in `monitoring/prometheus.yml` must be updated.
- Monitoring has not yet been verified during a Jenkins-triggered deployment. This will be shown in the Level 4 demonstration.

Monitoring will be considered complete when the dashboard keeps displaying the production server's metrics after the automated Level 4 deployment.

## Development Workflow

Each team member should work on a separate feature branch.

- `main` — Integrated project code
- `feature/jenkins` — Jenkins CI/CD
- `feature/flask-app` — Flask application and tests
- `feature/docker` — Docker and deployment
- `feature/monitoring` — Monitoring configuration

Changes should be submitted through Pull Requests for review before merging into `main`.

Passwords, SSH private keys and other sensitive credentials must not be committed to the repository.

## Next Steps

1. Complete Jenkins Pipeline configuration.
2. Configure the required SSH connections among the servers.
3. Build the application and perform automated testing through Jenkins.
4. Deploy the approved application to VM3.
5. Decide where monitoring runs for the final demonstration (VM1 or the owner's laptop) and verify the dashboard after the Level 4 deployment.
6. Demonstrate automatic deployment after a source-code change.
7. Collect screenshots and testing results for the final project report.

## Project Deliverables

- Project Brief
- GitHub source code repository
- Flask Student Task Management System
- Automated pytest tests
- Docker configuration
- Jenkins CI/CD Pipeline
- Test and Production server environments
- Prometheus and Grafana monitoring dashboard
- Level 4 deployment demonstration
- Project presentation and final report

## Project Status

**In Progress — Full Integration and Level 4 Verification Pending**
