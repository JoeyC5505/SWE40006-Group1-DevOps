# Monitoring Setup (Prometheus & Grafana)

## Ports Used
- Node Exporter (VM 3): 9100
- Prometheus (VM 1): 9090
- Grafana (VM 1): 3000

## Setup Steps
*(Detailed installation steps will go here once VMs are ready)*

## Verification
- [ ] `curl http://<VM3_IP>:9100/metrics` returns metrics
- [ ] Prometheus `/targets` shows production-server UP
- [ ] Grafana shows CPU/Memory panels
