# 🔐 Cybersecurity Internship - Task 1: Vulnerability Assessment using OWASP Juice Shop

## 📌 Overview

As part of the Future Interns Cybersecurity Internship, Task 1 involved performing a hands-on vulnerability assessment of the **OWASP Juice Shop** — a deliberately insecure web application. This exercise focused on identifying common web vulnerabilities using tools like **Burp Suite**, and applying foundational OWASP Top 10 security concepts.

---

## 🧰 Tools & Technologies Used

- 🔍 **Burp Suite Community Edition**
- 🌐 **OWASP Juice Shop (Localhost)**
- 📖 OWASP Top 10
- 📸 Screenshots of discovered vulnerabilities

---

## 🎯 Objectives

- Set up a proxy and intercept HTTP traffic using Burp Suite.
- Explore the OWASP Juice Shop app and identify at least **3–5 common vulnerabilities**.
- Document findings with screenshots and explain how each vulnerability maps to the **OWASP Top 10**.
- Suggest mitigation strategies for each vulnerability.

---

## ✅ Vulnerabilities Identified

| Vulnerability             | OWASP Mapping       | Screenshot Ref | Suggested Mitigation                         |
|--------------------------|----------------------|----------------|----------------------------------------------|
| Insecure Login           | A07: Identification & Authentication Failures | Screenshot-1 | Enforce strong password policy, use 2FA     |
| SQL Injection            | A01: Broken Access Control | Screenshot-2 | Use parameterized queries                    |
| Cross-Site Scripting (XSS) | A03: Injection         | Screenshot-3 | Encode outputs, validate input               |
| Security Misconfiguration| A05: Security Misconfiguration | Screenshot-4 | Remove default debug info, configure headers |

---

## 🖼️ Screenshots

All screenshots have been added to the `/screenshots` directory and are referenced in the report.

---

## 📄 Report

See the `Task1_Report.pdf` or `Report.md` file for a full breakdown of vulnerabilities with explanations, evidence, OWASP mapping, and recommendations.

---

## 💡 Learnings

- Gained hands-on exposure to Burp Suite and how HTTP requests can be intercepted/manipulated.
- Understood how to identify and document real-world vulnerabilities.
- Applied OWASP Top 10 knowledge practically.
- Built foundational skills for offensive and defensive web security.




