# Task 1 - Web Application Security Testing Report

## 🎯 Objective

To perform security testing on a vulnerable web application (OWASP Juice Shop) and identify common web application vulnerabilities.  
This simulation reflects how real-world ethical hackers assess applications for exploitable issues like SQL injection, XSS, and authentication flaws.

---

## 🛠 Tools Used

- **Burp Suite Community Edition**
- **Chromium** (configured via Burp Proxy)
- **OWASP Juice Shop** – [https://demo.owasp-juice.shop](https://demo.owasp-juice.shop)

---

## 🚨 Vulnerabilities Discovered

### 1. Reflected XSS (Cross-Site Scripting)

- **Endpoint:** `/#/search?q=`
- **Payload Used:** `<script>alert(1)</script>`
- **Description:** The application reflects unsanitized input back to the user without encoding, leading to script execution in the browser.
- **Impact:** Attacker can steal session tokens or redirect users.
- **Severity:** 🟠 Medium  
- **Mitigation:** Implement input sanitization and output encoding.

---

### 2. SQL Injection (Login Bypass)

- **Endpoint:** `/rest/user/login`
- **Payload Used:** `' OR '1'='1`
- **Description:** Bypasses authentication logic by injecting always-true condition.
- **Impact:** Unauthorized access to user accounts or admin panel.
- **Severity:** 🔴 High  
- **Mitigation:** Use prepared statements and parameterized queries.

---

### 3. Insecure Authentication Tokens

- **Observation:** JWT token in login response is predictable and easily reusable.
- **Impact:** Session hijacking is possible if token is intercepted.
- **Severity:** 🟠 Medium  
- **Mitigation:** Secure token generation, HTTPS-only cookies, short token lifespan.

---

## 🖼️ Screenshots Included

All screenshots are available in the `/screenshots` directory.

- **Proxy Tab:** Captured login/search requests  
- **Repeater Tab:** Modified requests and responses  
- **Decoder Tab:** Base64 and URL payload decoding  
- **Comparer Tab:** Response diff between success and fail  
- **Target Tab:** Application structure analysis  

---

## 🧠 Skills Gained

- Web application penetration testing  
- Manual attack simulation using Burp Suite  
- HTTP request/response analysis  
- Identification of OWASP Top 10 vulnerabilities  
- Real-world vulnerability reporting techniques

---

## 🔐 OWASP Top 10 Mapping

| OWASP ID | Vulnerability Name                       | Status |
|----------|------------------------------------------|--------|
| A01      | Broken Access Control                    | ✅ Done |
| A02      | Cryptographic Failures                   | ✅ Done |
| A03      | Injection (SQLi)                         | ✅ Done |
| A04      | Insecure Design                          | ✅ Done |
| A05      | Security Misconfiguration                | ✅ Done |
| A06      | Vulnerable and Outdated Components       | ✅ Done |
| A07      | Identification & Authentication Failures | ✅ Done |
| A08      | Software and Data Integrity Failures     | ✅ Done |
| A09      | Logging and Monitoring Failures          | ✅ Done |
| A10      | Server-Side Request Forgery (SSRF)       | ✅ Done |

---

## 📌 Detailed Mapping and Notes

### 🔹 A01: Broken Access Control  
- **Issue:** Direct access to `/#/administration` bypassing authentication.  
- **Mitigation:** Implement role-based access control (RBAC) with server-side checks.

### 🔹 A02: Cryptographic Failures  
- **Issue:** No enforced HTTPS and insecure cookie attributes (missing `Secure`, `HttpOnly`).  
- **Mitigation:** Enforce HTTPS and secure all session tokens.

### 🔹 A03: Injection (SQLi)  
- **Issue:** SQL injection on login and search using payloads like `' OR 1=1--`.  
- **Mitigation:** Use parameterized queries and ORM input sanitization.

### 🔹 A04: Insecure Design  
- **Issue:** No CAPTCHA or rate-limiting on login.  
- **Mitigation:** Implement login attempt throttling and secure design practices.

### 🔹 A05: Security Misconfiguration  
- **Issue:** Missing headers (e.g., `X-Frame-Options`), stack traces exposed.  
- **Mitigation:** Harden HTTP headers and disable debug mode in production.

### 🔹 A06: Vulnerable and Outdated Components  
- **Issue:** Intentionally outdated AngularJS and Express.js packages.  
- **Mitigation:** Regularly patch/update dependencies and monitor CVEs.

### 🔹 A07: Identification and Authentication Failures  
- **Issue:** No brute-force protection or MFA on login.  
- **Mitigation:** Enforce MFA, account lockout, and strong password policies.

### 🔹 A08: Software and Data Integrity Failures  
- **Issue:** No integrity check (e.g., SRI) on external scripts.  
- **Mitigation:** Use Subresource Integrity (SRI) and secure CI/CD.

### 🔹 A09: Logging and Monitoring Failures  
- **Issue:** No alerts/logs for failed login attempts or suspicious behavior.  
- **Mitigation:** Integrate SIEM tools for centralized logging and alerts.

### 🔹 A10: Server-Side Request Forgery (SSRF)  
- **Issue:** Image upload by URL can trigger SSRF.  
- **Mitigation:** Validate/whitelist external URLs, block internal IPs.

---

## ✅ Conclusion

This task provided practical hands-on experience with common web application vulnerabilities and how attackers exploit them.  
By using tools like Burp Suite and targeting OWASP Juice Shop, we simulated real-world attack scenarios and understood mitigation strategies through the lens of the OWASP Top 10.

---

## 🙏 Acknowledgment

Thanks to **Future Interns** for the opportunity to explore web application security in a guided, real-world scenario.

---

**Task 1 completed successfully.**
