# Project Keswick Tech Showcase

Demonstrates edge computing on ESXi with Kubernetes, running containerised workloads (computer vision, LLMs, monitoring) on Intel NUC hardware with GitOps-style promotion across multiple physical sites.

## Components

| Directory | Description |
|-----------|-------------|
| `edge-llm/` | Self-contained Ollama + Llama 3.1 8B Docker image for offline edge LLM inference with Open WebUI |
| `face-detector/` | Real-time face/eye detection from RTSP camera streams using OpenCV Haar Cascades and Flask |
| `opencv/` | Base Docker image with Python, OpenCV, and Flask — foundation for `face-detector` |
| `log-ship/` | Lightweight log shipper container forwarding logs from edge nodes via NFS |
| `three-tier/` | Classic three-tier microservices demo (PostgreSQL, API, UI) for application lifecycle demos |
| `rtos/` | Kubernetes VM Operator manifest for latency-sensitive real-time OS workloads on ESXi |
| `sec.yaml` | Declarative ESXi host security and configuration profile (NTP, syslog, lockout, vSwitch hardening) |
| `sites/` | Per-site Kubernetes manifests for GitOps deployment across three edge locations |

## Site Topology

| Site | Role | Workloads |
|------|------|-----------|
| Bakewell | Production | Face detector, monitoring, log shipping, host config, VMs |
| Sheffield | UAT | Face detector |
| Manchester | QA | Face detector |

## CI/CD Pipeline

Azure DevOps pipeline (`azure-pipelines.yml`) triggered by changes to `face-detector/`:

1. Build multi-arch Docker image (amd64/arm64) and push to GHCR
2. Update QA manifest (Manchester) with new image tag
3. Manual approval gate
4. Update UAT manifest (Sheffield)
5. Manual approval gate
6. Update Production manifest (Bakewell)

Each stage commits the updated manifest back to the repo, promoting builds through environments via GitOps.

## Useful Commands

Access Kubernetes from ESXi SSH:

```bash
alias kubectl="inf-cli exec -i $(inf-cli get pods -a | awk '/ec-system/{print $2}') kube-apiserver -n kube-system -- kubectl --kubeconfig /etc/kubernetes/admin.conf"
```

When running on a device with multiple NICs, specify the management NIC:

```bash
network --bootproto=dhcp --device=vmnic5
```

## Network

```url
https://veco929-kiad1.velocloud.net
```

## RTSP Authentication

```bash
rtsp://camera:password@192.168.1.127/stream1
rtsp://camera:password@192.168.1.127/stream2
```

## Presentations

- `jan24-manc-devops-meetup/` — Live demo cheat sheet from the January 2024 Manchester DevOps Meetup
