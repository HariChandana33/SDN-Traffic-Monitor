# SDN-Traffic-Monitor
A network monitoring dashboard that visualizes traffic flow and detects anomalies using OpenDaylight and Mininet.

# 🌐 SDN Network Traffic Visualizer

A Software Defined Networking (SDN) project designed to monitor, analyze, and visualize network traffic in real-time. This system leverages the **OpenDaylight (ODL)** controller to extract telemetry data from a simulated network topology.

## 🎯 Objectives
* **Real-Time Monitoring:** continuously track packet flows and bandwidth usage across network switches.
* **Anomaly Detection:** Identify sudden spikes or drops in traffic that may indicate network failures or attacks.
* **Visualization:** Convert raw network data into actionable graphs using Grafana.

## 🏗️ Architecture & Tools
* **Controller:** OpenDaylight (ODL) - Manages the flow rules and network state.
* **Simulation:** Mininet - Creates the virtual network topology (switches and hosts).
* **Data Collection:** Python scripts polling ODL Northbound APIs.
* **Visualization:** Grafana - Displays bandwidth, packet loss, and latency metrics.

## 📊 How It Works
1.  **Simulation:** Mininet generates a custom network topology.
2.  **Control:** OpenDaylight connects to the switches via OpenFlow.
3.  **Extraction:** A Python middleware script queries ODL for statistics (Flow stats, Port stats).
4.  **Display:** Data is pushed to a dashboard (Grafana) for live monitoring.

## 📝 Usage
* Start the ODL Karaf distribution.
* Run the Mininet topology script: `sudo mn --controller=remote...`
* Execute the Python monitoring script to begin fetching stats.
* Access the Grafana dashboard at `http://localhost:3000`.
