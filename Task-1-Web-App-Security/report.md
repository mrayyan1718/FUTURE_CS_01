🛡️ Security Assessment Report – Task 1

📌 Objective

To perform security testing on a vulnerable web application (OWASP Juice Shop) and identify common web application vulnerabilities. This simulation reflects how real-world ethical hackers assess applications for exploitable issues like SQL injection, XSS, and authentication flaws.

---

🧰 Tools Used

- Burp Suite Community Edition
- Chromium (via Burp)
- OWASP Juice Shop – [https://demo.owasp-juice.shop](https://demo.owasp-juice.shop)

---

 🧪 Vulnerabilities Discovered

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

📂 Screenshots Included

- Proxy tab: Captured login/search request  
- Repeater tab: Modified requests sent and responses observed  
- Decoder tab: Analyzed encoded payloads (Base64, URL)  
- Comparer tab: Difference between success/fail responses  
- Target tab: Application structure analysis  

All screenshots are available in the `/screenshots` directory.

---

🧠 Skills Gained

- Web application penetration testing  
- Manual attack simulation using Burp Suite  
- HTTP request/response analysis  
- Identification of OWASP Top 10 vulnerabilities  
- Real-world reporting techniques

---

📝 OWASP Top 10 Mapping

| Vulnerability                 | OWASP Category                       |
|-------------------------------|--------------------------------------|
| Reflected XSS                 | A7:2021 – Cross-Site Scripting (XSS) |  
| SQL Injection (Login Bypass)  | A1:2021 – Injection                  |
| Insecure Authentication       | A2:2021 – Broken Authentication      |

---

✅ Conclusion

This task provided practical hands-on exposure to common web application security issues. The experience helped in understanding how attackers think and how developers can mitigate such issues with secure coding practices.

Task 1 completed successfully. 

