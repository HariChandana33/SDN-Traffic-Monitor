import time
import requests
from prometheus_client import start_http_server, Gauge

# Define the metric
PACKETS_TX = Gauge('sdn_port_packets_transmitted', 'Packets sent per port', ['switch_id', 'port_id'])

def fetch_metrics():
    # Trying the most common URL for your version
    url = "http://localhost:8181/rests/data/opendaylight-inventory:nodes?content=nonconfig"
    auth = ('admin', 'admin')
    try:
        r = requests.get(url, auth=auth, headers={'Accept': 'application/json'})
        if r.status_code == 200:
            data = r.json()
            # This logic searches for any 'node' entry in the data
            nodes = data.get('opendaylight-inventory:nodes', {}).get('node', []) or data.get('nodes', {}).get('node', [])
            
            for node in nodes:
                s_id = node.get('id', 'unknown')
                connectors = node.get('node-connector', [])
                for conn in connectors:
                    p_id = conn.get('id', 'unknown')
                    
                    # Search for the statistics block specifically
                    # Some versions use different prefixes; this covers the most common ones
                    stats = conn.get('opendaylight-port-statistics:flow-capable-node-connector-statistics', {})
                    if not stats:
                        stats = conn.get('flow-capable-node-connector-statistics', {})
                    
                    packets = stats.get('packets', {}).get('transmitted', 0)
                    
                    # Update Prometheus
                    PACKETS_TX.labels(switch_id=s_id, port_id=p_id).set(packets)
                    print(f"Updated: {s_id} Port {p_id} -> {packets} packets")
        else:
            print(f"ODL Error: {r.status_code}")
    except Exception as e:
        print(f"Script Error: {e}")

if __name__ == '__main__':
    start_http_server(8000)
    print("Exporter is live on http://localhost:8000")
    while True:
        fetch_metrics()
        time.sleep(2)
