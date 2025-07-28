# 🔒 Incident Response Report: Task 2 - Security Alert Monitoring

### 🔍 Summary

This report outlines the findings from analyzing simulated security logs using **Splunk**, a SIEM (Security Information and Event Management) platform. The objective was to identify, classify, and respond to suspicious security events such as failed login attempts, malware alerts, and potential threat indicators.

---

### 🚀 Tools Used

* **Splunk Free Trial** (Splunk Enterprise 9.4.3)
* Sample log file: `SOC_Task2_Sample_Logs.txt`
* Splunk Dashboard Studio
* Screenshots from Splunk

---

### 🔢 Alerts Identified

| Alert Type             | Detected In      | Severity | Description                                                   | Suggested Action                                          |
| ---------------------- | ---------------- | -------- | ------------------------------------------------------------- | --------------------------------------------------------- |
| Failed Login           | Splunk Logs      | Medium   | Multiple failed login attempts by user 'root' from unknown IP | Block IP temporarily, review access logs                  |
| Malware Alert          | Splunk Logs      | High     | setup.zip malware detected on FINANCE-PC                      | Isolate host, scan with antivirus                         |
| Suspicious IP          | Splunk Logs      | High     | High number of login attempts from 203.0.113.77               | Blacklist the IP and monitor user behavior                |
| Multiple Failed Logins | Splunk Dashboard | High     | Repeated failed login attempts from user 'admin'              | Enforce 2FA and notify SOC team                           |
| Ransomware Detected    | Splunk Logs      | Critical | Ransomware signature detected in malware logs                 | Isolate infected system, start incident response protocol |

---

### 📊 Dashboard Overview

A summary dashboard was created using Splunk Dashboard Studio, containing:

* **Bar Chart**: User login attempts overview
* **Column Chart**: Malware alerts by host
* **Pie Chart**: Distribution of threat types (Trojan, Ransomware, etc.)
* **Single Value**: Total incidents detected (160)
* **Table**: Top 5 suspicious IP addresses with highest login attempts

![Dashboard Screenshot](dashboard.png)

---

### 🔒 Incident Summary & Recommendations

* Implement IP throttling and alerting on repeated failed login attempts.
* Enable 2FA for all administrative accounts.
* Update antivirus definitions and scan all hosts.
* Monitor high-frequency IPs and blacklist those flagged for brute-force behavior.
* Establish a response playbook for malware and ransomware detection.

---

### 📄 Files Attached

* `Alert_Classification_Task2.xlsx` – Alert log and classifications
* Screenshots – For malware, failed logins, Splunk dashboard

