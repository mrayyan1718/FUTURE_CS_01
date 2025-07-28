# 🧠 Task 2 – Security Alert Monitoring & Incident Response

This task involves using **Splunk**, a Security Information and Event Management (SIEM) tool, to analyze sample log data and monitor for potential security threats. We simulate a SOC (Security Operations Center) environment and respond to incidents based on log alerts.

---

## 📁 Files Included

| File                              | Description                                                   |
|-----------------------------------|---------------------------------------------------------------|
| `report.md`                       | Complete incident response report with screenshots and insights |
| `Alert_Classification_Task2.xlsx`| Excel sheet with alerts, severity, mapping, and remediation   |
| `screenshots/`                   | Folder containing PNGs of Splunk queries and dashboard         |
| `SOC_Task2_Sample_Logs.txt`      | Sample log file ingested into Splunk (if permitted to share)   |

---

## 📸 Screenshots Overview

| Screenshot Filename                   | Description                                                   |
|--------------------------------------|---------------------------------------------------------------|
| `01_index_main_search.png`           | Raw search with `index="main"` showing Splunk log ingestion   |
| `02_authentication_field_logs.png`   | Authentication-related log entries                            |
| `03_malware_virus_trojan_detected.png`| Malware, Trojan, and virus activity detected                   |
| `04_time_filter_24hrs_latest_now.png`| Search filtered for last 24 hours                             |
| `05_stats_count_by_user_gt_5.png`    | Failed login user stats where count > 5                       |
| `06_dashboard_view.png`              | Final SOC Dashboard built using Splunk Dashboard Studio       |

> All screenshots are located inside the `/screenshots` folder.

---

## ⚙️ Steps Performed

1. **Ingested** `SOC_Task2_Sample_Logs.txt` into Splunk
2. Performed log analysis to detect:
   - Failed login attempts
   - Malware/ransomware alerts
   - Suspicious IP activity and brute-force patterns
3. Took relevant **screenshots** of search results and dashboards
4. Created a **custom dashboard** with:
   - Login attempts chart
   - Malware alerts by host
   - Threat distribution (pie chart)
   - Total incident count (single value)
   - Top IPs by failed login (table view)
5. Compiled all findings into a professional **report.md**
6. Documented alert types and recommendations in an **Excel classification sheet**
7. Drafted a stakeholder email for incident escalation *(optional)*

---

## ✅ Deliverables

| Item                                     | Status |
|------------------------------------------|--------|
| 📝 `report.md` – Incident Response Report | ✅     |
| 📊 Security Dashboard (Splunk Studio)     | ✅     |
| 🖼️ Screenshots of searches and findings    | ✅     |
| 📑 `Alert_Classification_Task2.xlsx`      | ✅     |
| 📧 Stakeholder Email Draft *(Optional)*   | ✅     |

---

## 🧪 Skills Demonstrated

- Splunk Search Processing Language (SPL)
- Log correlation and event investigation
- Security event classification
- Creating visual dashboards with Splunk Studio
- Report writing and documentation best practices

---

## 📄 Report

👉 Refer to [`report.md`](./report.md) for detailed findings, dashboard views, and recommendations.

