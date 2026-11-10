# SWE40006 Group 1 — DevOps Deployment Pipeline

## Project Overview

This project is developed by Group 1 for SWE40006 Software Deployment and Evolution at Swinburne University of Technology.

Our objective is to design and implement a Level 4 DevOps pipeline for a Student Task Management System. The pipeline aims to automate the software build, testing and deployment process using GitHub, Jenkins, Docker and Ubuntu Server virtual machines.

The project also incorporates production performance monitoring using Prometheus, Grafana and Node Exporter to monitor the health and performance of the production server.

**Target Level:** Level 4  
**Application:** Student Task Management System  
**Project Status:** CI/CD Pipeline Successfully Tested — Final Level 4 Verification Pending


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

The application has been developed, and all 9 automated pytest tests have passed in the developer's local environment. Testing through the complete Jenkins pipeline is still pending.

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

## Proposed DevOps Architecture

The project uses three virtual machines, each assigned a specific responsibility.

| Server | Responsibility |
|---|---|
| VM1 — Jenkins Server | CI/CD orchestration, build automation and deployment coordination |
| VM2 — Test Server | Application testing and verification |
| VM3 — Production Server | Hosting the deployed Flask application |

The planned deployment workflow is:

```text
Developer
    |
    v
GitHub Repository
    |
    v
Jenkins (VM1)
    |
    v
Test Server (VM2)
    |
    v
Production Server (VM3)
    |
    v
Running Flask Application
```

Production server performance is monitored using Node Exporter, Prometheus and Grafana.

## Project Levels

### Level 1 — DevOps Infrastructure

Establish the GitHub repository, CI/build server, test server and production server. Configure the required virtual machines and communication between the servers.

### Level 2 — Production Monitoring

Configure monitoring to collect production server performance metrics using Node Exporter and Prometheus. Visualise the collected metrics through Grafana dashboards.

### Level 3 — Application Deployment

Deploy the Flask application through the pipeline and verify that it is accessible and functioning correctly on the production server.

### Level 4 — Automated Deployment

Demonstrate that a source-code change triggers an automatic or deferred pipeline execution, including application building, automated testing and production deployment.

The deployment process should also include verification that the application is running successfully after deployment.

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
| VM1 — Jenkins Server | Completed — Ubuntu Server, Jenkins, Docker and required plugins installed and configured |
| VM2 — Test Server | Completed — Docker, Docker Compose, Java 21 and Jenkins agent `vm2-docker` configured and tested successfully |
| VM1 to VM2 manual SSH connection | Completed — passwordless SSH connection verified and `vm2-ssh` credential configured in Jenkins |
| VM3 — Production Server | Initial Docker deployment demonstrated |
| Jenkins automated Build/Test/Deploy | In progress |
| Node Exporter on VM3 | Running; metrics reachable on port 9100 |
| Prometheus and Grafana configuration files | Uploaded in the `monitoring/` folder on `feature/monitoring` |
| Production monitoring integration | Verified: Prometheus collects VM3 metrics and Grafana displays CPU usage, memory usage, disk usage and node availability |
| Updated Grafana dashboard export | Updated JSON export maintained in the `monitoring/` folder |
| Post-deployment monitoring verification | Pending |
| Level 4 automatic deployment | Not yet verified |

*This progress summary reflects the team's reported work. Successful installation does not necessarily mean end-to-end pipeline integration has been completed.*

## Production Server Monitoring

### Monitoring Architecture

The project uses three main monitoring components:

| Component | Port | Responsibility |
|---|---:|---|
| Node Exporter (VM3) | 9100 | Collects Linux server performance metrics |
| Prometheus | 9090 | Scrapes and stores monitoring metrics |
| Grafana | 3000 | Displays monitoring data through dashboards |

The monitoring architecture follows this workflow:

```text
VM3 — Production Server
        |
        v
   Node Exporter
      Port 9100
        |
        v
    Prometheus
      Port 9090
        |
        v
      Grafana
      Port 3000
        |
        v
Production Server Monitoring Dashboard
```

### Current Monitoring Configuration

Node Exporter is running on VM3 and exposes Linux system metrics through port 9100.

Prometheus is configured with a `production-server` scrape job targeting VM3.

Example configuration:

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'production-server'
    static_configs:
      - targets:
          - '172.20.10.3:9100'

  - job_name: 'prometheus'
    static_configs:
      - targets:
          - 'localhost:9090'
```

The VM3 target address is currently `172.20.10.3:9100`. This address is assigned by the hotspot network and may change when the network connection changes.

If the address changes, the target in `monitoring/prometheus.yml` must be updated accordingly.

### Grafana Dashboard

The project uses a Grafana dashboard named **Production Server Monitoring**.

The current verified dashboard displays:

- CPU usage
- Memory usage
- Disk usage
- Node Exporter availability

Additional monitoring metrics planned for the dashboard include:

- Server uptime
- System load average (1-minute, 5-minute and 15-minute)
- Network download speed
- Network upload speed
- Network errors
- Network dropped packets
- Network interface status
- Filesystem inode usage
- System context switches
- System interrupts
- Operating system information

The updated Grafana dashboard is exported as a JSON file to allow the dashboard configuration to be stored, shared and imported when required.

### Monitoring Project Files

The monitoring-related files are maintained in the `monitoring/` directory.

```text
monitoring/
├── prometheus.yml
├── production-server-monitoring.json
└── README.md
```

The files serve the following purposes:

| File | Purpose |
|---|---|
| `prometheus.yml` | Prometheus scrape configuration |
| `production-server-monitoring.json` | Exported Grafana dashboard configuration |
| `README.md` | Monitoring installation, configuration and setup instructions |

### Current Monitoring Status

- Node Exporter is running on VM3, and its metrics have been verified from the monitoring machine.
- Prometheus is configured with a `production-server` job targeting VM3 (`172.20.10.3:9100`).
- The Prometheus Targets page shows the Node Exporter target as **UP**.
- Grafana is connected to Prometheus.
- The Production Server Monitoring dashboard displays CPU usage, memory usage, disk usage and node availability using live monitoring data.
- The monitoring configuration, updated dashboard JSON export and setup guide are maintained in the `monitoring/` folder on the `feature/monitoring` branch.

### Current Limitations

- Prometheus and Grafana currently run on the owner's laptop, which is connected to the same hotspot as VM3.
- The team still needs to decide whether Prometheus and Grafana should be moved to VM1 for the final demonstration.
- VM3's IP address is assigned by the hotspot network and may change. If it changes, the target address in `monitoring/prometheus.yml` must be updated.
- Monitoring has not yet been verified during a Jenkins-triggered deployment.
- The team must verify that monitoring continues to collect production server metrics after the automated Level 4 deployment.

Monitoring will be considered complete when the dashboard continues displaying the production server's metrics after the automated Level 4 deployment.

## Development Workflow

Each team member should work on a separate feature branch to support parallel development and reduce conflicts.

The current branch structure is:

| Branch | Purpose |
|---|---|
| `main` | Integrated project code |
| `feature/jenkins` | Jenkins CI/CD configuration |
| `feature/flask-app` | Flask application and automated tests |
| `feature/docker` | Docker and deployment configuration |
| `feature/monitoring` | Prometheus, Grafana and Node Exporter monitoring configuration |

Changes should be committed and pushed to the relevant feature branches.

Pull Requests should be submitted for review before changes are merged into `main`.

Passwords, SSH private keys, access tokens and other sensitive credentials must not be committed to the repository.

## Next Steps

1. Complete the Jenkins Pipeline configuration.
2. Configure the required SSH connections among the servers.
3. Build the application and perform automated testing through Jenkins.
4. Deploy the approved application to VM3.
5. Decide where Prometheus and Grafana will run for the final demonstration (VM1 or the owner's laptop).
6. Verify that the Grafana dashboard continues displaying production server metrics after the Jenkins-triggered deployment.
7. Demonstrate automatic or deferred deployment after a source-code change.
8. Collect screenshots, pipeline execution logs and testing results for the final project report.
9. Complete integration testing and prepare the final project presentation.

## Project Deliverables

- Project Brief
- GitHub source code repository
- Flask Student Task Management System
- SQLite database integration
- Automated pytest test suite
- Docker configuration
- Docker Compose configuration
- Jenkins CI/CD Pipeline
- Test and Production server environments
- Prometheus monitoring configuration
- Node Exporter installation and configuration
- Grafana monitoring dashboard and JSON export
- Monitoring installation and setup guide
- Level 4 deployment demonstration
- Project presentation and final report

## Project Status

**CI/CD Pipeline Successfully Tested — Final Level 4 Verification Pending**

The Jenkins CI/CD pipeline has been successfully tested. VM1 is working as the Jenkins controller, while VM2 is used as the Jenkins agent for Docker builds and automated testing. All 9 automated tests passed, and the pipeline successfully deployed the application to VM3.

The remaining work includes the final Level 4 automatic deployment demonstration and post-deployment monitoring verification.
