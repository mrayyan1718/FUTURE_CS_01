Task 1 - Web Application Security Testing Report

 Objective

To perform security testing on a vulnerable web application (OWASP Juice Shop) and identify common web application vulnerabilities. This simulation reflects how real-world ethical hackers assess applications for exploitable issues like SQL injection, XSS, and authentication flaws.

---

 Tools Used

- Burp Suite Community Edition
- Chromium (via Burp)
- OWASP Juice Shop – [https://demo.owasp-juice.shop](https://demo.owasp-juice.shop)

---

  Vulnerabilities Discovered

1. Reflected XSS (Cross-Site Scripting)

- Endpoint:`/#/search?q=`
- Payload Used: `<script>alert(1)</script>`
- Description: The application reflects unsanitized input back to the user without encoding, leading to script execution in the browser.
- Impact: Attacker can steal session tokens or redirect users.
- Severity: Medium
- Mitigation: Implement input sanitization and output encoding.

---

2. SQL Injection (Login Bypass)

- Endpoint: `/rest/user/login`
- Payload Used: `' OR '1'='1`
- Description: Bypasses authentication logic by injecting always-true condition.
- Impact: Unauthorized access to user accounts or admin panel.
- Severity: High
- Mitigation: Use prepared statements and parameterized queries.

---

3. Insecure Authentication Tokens

- Observation: JWT token in login response is predictable and easily reusable.
- Impact: Session hijacking is possible if token is intercepted.
- Severity: Medium
- Mitigation: Secure token generation, HTTPS-only cookies, short token lifespan.

---

 Screenshots Included

- Proxy tab: Captured login/search request  
- Repeater tab: Modified requests sent and responses observed  
- Decoder tab: Analyzed encoded payloads (Base64, URL)  
- Comparer tab: Difference between success/fail responses  
- Target tab: Application structure analysis  

All screenshots are available in the `/screenshots` directory.

---

Skills Gained

- Web application penetration testing  
- Manual attack simulation using Burp Suite  
- HTTP request/response analysis  
- Identification of OWASP Top 10 vulnerabilities  
- Real-world reporting techniques

---

 OWASP Top 10 Mapping

| OWASP ID | Vulnerability Name                       | Status  |
|----------|------------------------------------------|---------|
| A01      | Broken Access Control                    |  Done   |
| A02      | Cryptographic Failures                   |  Done   |
| A03      | Injection (SQLi)                         |  Done   | 
| A04      | Insecure Design                          |  Done   |
| A05      | Security Misconfiguration                |  Done   |
| A06      | Vulnerable and Outdated Components       |  Done   | 
| A07      | Identification & Authentication Failures |  Done   |
| A08      | Software and Data Integrity Failures     |  Done   |
| A09      | Logging and Monitoring Failures          |  Done   |
| A10      | Server-Side Request Forgery (SSRF)       |  Done   |

Below is a detailed mapping of vulnerabilities identified in OWASP Juice Shop to the OWASP Top 10:

🔹 A01: Broken Access Control
We were able to directly access restricted pages like /#/administration without proper authentication. This confirms missing access control checks on sensitive endpoints.
→ Mitigation: Implement role-based access control (RBAC) and validate user roles on the server side.

🔹 A02: Cryptographic Failures
The application does not enforce HTTPS everywhere and stores tokens in cookies without Secure or HttpOnly flags. This exposes sensitive data during transmission.
→ Mitigation: Enforce HTTPS and secure cookie attributes.

🔹 A03: Injection (SQLi)
By injecting special characters like ' OR 1=1-- in the product search bar, we observed abnormal backend behavior, confirming SQL injection.
→ Mitigation: Use parameterized queries and ORM tools to sanitize inputs.

🔹 A04: Insecure Design
There is no rate-limiting or CAPTCHA on login forms, making it susceptible to brute-force attacks.
→ Mitigation: Implement secure design principles such as input validation, rate-limiting, and error handling from the start.

🔹 A05: Security Misconfiguration
We found verbose error messages, missing security headers (like X-Frame-Options), and visible stack traces.
→ Mitigation: Harden HTTP headers, disable debug in production, and handle errors gracefully.

🔹 A06: Vulnerable & Outdated Components
OWASP Juice Shop uses intentionally outdated packages (e.g., AngularJS and Express.js versions).
→ Mitigation: Regularly update dependencies and monitor CVEs (Common Vulnerabilities and Exposures).

🔹 A07: Identification and Authentication Failures
Login forms had no brute-force protection or MFA. Attackers can guess passwords easily.
→ Mitigation: Enforce account lockouts, MFA, and strong password policies.

🔹 A08: Software and Data Integrity Failures
There is no verification mechanism for packages or scripts loaded externally. Unsigned scripts pose a risk of supply chain attacks.
→ Mitigation: Use subresource integrity (SRI), code signing, and secure CI/CD pipelines.

🔹 A09: Security Logging and Monitoring Failures
Login failures and suspicious actions are not logged or flagged.
→ Mitigation: Implement centralized logging and real-time alerting via SIEM tools.

🔹 A10: Server-Side Request Forgery (SSRF)
We simulated SSRF by uploading an image via URL and observed the backend interacting with external/internal URLs.
→ Mitigation: Whitelist valid URLs, block internal IP access from user input, and validate user-provided URLs.

---

Conclusion

This task provided practical hands-on exposure to common web application security issues. The experience helped in understanding how attackers think and how developers can mitigate such issues with secure coding practices.

---

Acknowledgment

Thanks to Future Interns for this hands-on opportunity in real-world cybersecurity!

Task 1 completed successfully. 

