from flask import Flask, render_template

app = Flask(__name__)

PROFILE = {
    "name": "Saira S Elizabeth",
    "title": "Cybersecurity Analyst",
    "headline": "Cybersecurity • VAPT • Application Security • Secure Software Development",
    "email": "sairaselizabeth20@gmail.com",
    "github": "https://github.com/SairaSEliz",
    "degree": "B.E. Computer Science & Engineering",
    "experience": "1.5+ years of professional software development experience",
    "course": "Cyber Security Analyst Course — ICT Academy of Kerala",
    "course_year": "2024",
}

SKILLS = [
    ("Cybersecurity", "Vulnerability Assessment, Penetration Testing, Web Security, Application Security, OWASP Top 10"),
    ("Security Tools", "Burp Suite, Nmap, Wireshark, Netcat, Metasploit, Frida, Genymotion"),
    ("Programming", "Python, Java, PHP, C++, SQL, JavaScript, HTML, CSS, Git"),
    ("Security Assessment", "CIS Benchmarks, configuration review, hardening, security reporting"),
    ("Systems & Networking", "Linux, Windows, TCP/IP, HTTP, networking fundamentals"),
]

PROJECTS = [
    {
        "type": "PYTHON • SECURITY AUTOMATION",
        "title": "Security Log Threat Analyzer",
        "description": "Python-based portfolio project for parsing authentication and system logs, identifying suspicious patterns, and producing security-focused findings.",
        "tags": ["Python", "Log Analysis", "Threat Detection", "Security"],
    },
    {
        "type": "WEB APPLICATION SECURITY",
        "title": "Web Application Security Enhancement",
        "description": "Developed custom ModSecurity rules to detect and block SQL Injection and Cross-Site Scripting attack patterns.",
        "tags": ["ModSecurity", "SQL Injection", "XSS", "WAF"],
    },
    {
        "type": "MOBILE APPLICATION SECURITY",
        "title": "Android Application VAPT",
        "description": "Performed Android application security testing using static and dynamic analysis and documented findings and remediation strategies.",
        "tags": ["Burp Suite", "Frida", "Genymotion", "OWASP"],
    },
    {
        "type": "SECURITY ASSESSMENT",
        "title": "CIS Benchmark Security Assessment",
        "description": "Reviewed Windows and Cisco configurations against CIS Benchmarks and prepared security assessment reports.",
        "tags": ["CIS", "Windows", "Cisco", "Hardening"],
    },
]

EXPERIENCE = [
    {
        "period": "Professional Experience",
        "role": "Software Developer",
        "company": "Mahatma Gandhi University",
        "points": [
            "Worked for approximately 1.5 years in software development.",
            "Developed and maintained applications using Java, Python and PHP.",
            "Worked on university portals and application workflows.",
            "Applied secure development practices and worked with web technologies.",
            "Integrated payment gateway APIs and responsive interfaces.",
        ],
    },
    {
        "period": "2024",
        "role": "ICT Intern — Cybersecurity",
        "company": "Active Bytes",
        "points": [
            "Performed CIS Benchmark-based security reviews.",
            "Conducted Android mobile application VAPT.",
            "Used Burp Suite, Frida and Genymotion.",
            "Documented vulnerabilities and remediation strategies.",
        ],
    },
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        projects=PROJECTS,
        experience=EXPERIENCE,
    )

if __name__ == "__main__":
    app.run(debug=True)
