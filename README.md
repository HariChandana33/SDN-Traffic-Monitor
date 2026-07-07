# SDN-Based Network Traffic Monitoring & Visualization System

## 📌 Project Overview
This project implements a centralized network monitoring system using Software-Defined Networking (SDN) principles. By decoupling the control plane from the data plane, this system collects real-time traffic statistics and visualizes them to detect network anomalies, such as sudden bandwidth spikes or DDoS simulations.

## 🏗️ Architecture
* **Infrastructure Layer (Data Plane):** Mininet (Virtual Switches & Hosts)
* **Control Layer (Brain):** OpenDaylight Controller (Titanium Release)
* **Middleware (The Bridge):** Custom Python Exporter (REST API to Prometheus)
* **Storage & Visualization:** Prometheus (TSDB) & Grafana

![System Architecture](images/architecture.png) *(Add a diagram or photo of your handwritten architecture notes here)*

## 🚀 Technologies Used
* **Ubuntu Linux**
* **Mininet** (Network Emulator)
* **OpenDaylight (ODL)** (SDN Controller)
* **OpenFlow 1.3** (Southbound Protocol)
* **Python 3** (`requests`, `prometheus_client`)
* **Prometheus & Grafana**

---

## ⚙️ Installation & Setup

### 1. Network Simulation (Mininet)
Start the virtual network with 1 switch and 3 hosts, connecting remotely to the ODL controller via OpenFlow 1.3:
```bash
sudo mn --controller=remote,ip=127.0.0.1,port=6633 --topo=single,3 --switch=ovsk,protocols=OpenFlow13
