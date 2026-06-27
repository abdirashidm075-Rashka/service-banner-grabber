# Penetration Testing: Network Service Banner Grabber

## 📝 Description
This intelligence-gathering utility is designed for network reconnaissance and vulnerability management. By creating direct TCP socket handshakes with an asset's active infrastructure ports, the tool collects raw text responses ("banners") emitted by running services. This allows security engineers to perform manual service enumeration and identify outdated software versions.

## 🛠️ Features
* **Low-Level Socket Probing:** Utilizes Python's native network socket engine to manipulate raw TCP connection attempts.
* **Service Enumeration Mapping:** Isolates specific version footprints (e.g., specific OpenSSH or Apache versions).
* **Fault-Tolerant Scanning:** Embedded timeout configurations to prevent script stalls across unresponsive network targets.

## 🚀 How to Run It

### Prerequisites
* Python 3.x installed.

### Execution
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/service-banner-grabber.git](https://github.com/YOUR-USERNAME/service-banner-grabber.git)
