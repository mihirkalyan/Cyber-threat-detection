THREAT_BRIEFS = {
    "normal": {
        "category": "Benign",
        "description": "Normal network traffic with no malicious indicators detected.",
        "mitre": "N/A",
        "severity": "NONE",
        "indicators": "Typical packet rates, balanced SYN/ACK ratio, standard port usage",
        "recommendation": "No action required. Continue baseline monitoring.",
    },
    "neptune": {
        "category": "DoS",
        "description": "SYN flood attack exhausting the TCP half-open connection queue on the target host.",
        "mitre": "T1498.001 - Direct Network Flood",
        "severity": "HIGH",
        "indicators": "High SYN rate, low ACK ratio, elevated dst_host_count, serror_rate > 0.9",
        "recommendation": "Enable SYN cookies, rate-limit inbound SYN packets, configure TCP half-open connection limits.",
    },
    "smurf": {
        "category": "DoS",
        "description": "ICMP amplification attack using broadcast addresses to flood the victim with echo replies.",
        "mitre": "T1498.002 - Reflection Amplification",
        "severity": "HIGH",
        "indicators": "High ICMP echo traffic, spoofed source IPs, dst_host_same_srv_rate near 1.0",
        "recommendation": "Block directed broadcast packets at router, disable IP broadcast forwarding, deploy ingress filtering.",
    },
    "teardrop": {
        "category": "DoS",
        "description": "Malformed IP fragmentation attack causing OS crash due to overlapping fragment offsets.",
        "mitre": "T1499 - Endpoint Denial of Service",
        "severity": "HIGH",
        "indicators": "Fragmented packets with overlapping offsets, wrong_fragment > 0, system instability",
        "recommendation": "Apply OS patches, deploy IDS rules for overlapping fragment detection, enable fragment reassembly limits.",
    },
    "back": {
        "category": "DoS",
        "description": "Apache web server DoS via requests for URLs containing many forward slashes.",
        "mitre": "T1499.002 - Service Exhaustion Flood",
        "severity": "MEDIUM",
        "indicators": "Repeated HTTP requests with malformed paths, high dst_bytes, low src_bytes",
        "recommendation": "Upgrade Apache, implement request path validation, deploy WAF rules.",
    },
    "pod": {
        "category": "DoS",
        "description": "Ping of Death — oversized ICMP packet causing buffer overflow on target.",
        "mitre": "T1499 - Endpoint Denial of Service",
        "severity": "MEDIUM",
        "indicators": "ICMP packets exceeding 65535 bytes, wrong_fragment spike",
        "recommendation": "Apply OS-level patches, block oversized ICMP at perimeter firewall.",
    },
    "ipsweep": {
        "category": "Probe",
        "description": "Surveillance sweep scanning multiple IP addresses to discover live hosts.",
        "mitre": "T1595.001 - Scanning IP Blocks",
        "severity": "MEDIUM",
        "indicators": "Sequential IP scanning pattern, low duration per connection, high count",
        "recommendation": "Deploy honeypots, enable port scan detection, block scanning source IPs.",
    },
    "nmap": {
        "category": "Probe",
        "description": "Network port scan using Nmap to enumerate open services on target hosts.",
        "mitre": "T1046 - Network Service Discovery",
        "severity": "MEDIUM",
        "indicators": "Sequential port probing, SYN-only packets, low duration, high srv_count",
        "recommendation": "Restrict unnecessary open ports, deploy IDS signatures for Nmap fingerprints.",
    },
    "satan": {
        "category": "Probe",
        "description": "SATAN security scanner probing for known vulnerabilities across network services.",
        "mitre": "T1595.002 - Vulnerability Scanning",
        "severity": "MEDIUM",
        "indicators": "Multi-service probing pattern, rapid connection attempts, varied destination ports",
        "recommendation": "Monitor for vulnerability scanner signatures, patch exposed services.",
    },
    "portsweep": {
        "category": "Probe",
        "description": "Port sweep scanning a single target across many ports to map available services.",
        "mitre": "T1046 - Network Service Discovery",
        "severity": "MEDIUM",
        "indicators": "Single destination IP, high dst_host_srv_count, low bytes per connection",
        "recommendation": "Implement port-knocking, deploy firewall with stateful inspection.",
    },
    "buffer_overflow": {
        "category": "U2R",
        "description": "User-to-Root exploit overflowing a buffer to gain elevated privileges.",
        "mitre": "T1203 - Exploitation for Client Execution",
        "severity": "CRITICAL",
        "indicators": "root_shell=1, su_attempted=1, num_compromised > 0, unexpected privilege escalation",
        "recommendation": "Enable ASLR and DEP, apply security patches immediately, isolate affected host.",
    },
    "rootkit": {
        "category": "U2R",
        "description": "Rootkit installation granting persistent root-level access to attacker.",
        "mitre": "T1014 - Rootkit",
        "severity": "CRITICAL",
        "indicators": "root_shell=1, num_root > 0, hidden processes, modified system binaries",
        "recommendation": "Immediate host isolation, forensic imaging, full OS reinstall recommended.",
    },
    "warezclient": {
        "category": "R2L",
        "description": "Remote-to-Local attack downloading pirated software via FTP from a compromised server.",
        "mitre": "T1105 - Ingress Tool Transfer",
        "severity": "MEDIUM",
        "indicators": "Large dst_bytes via FTP, num_file_creations > 0, logged_in=1",
        "recommendation": "Monitor FTP traffic, enforce egress filtering, audit file creation events.",
    },
    "warezmaster": {
        "category": "R2L",
        "description": "Remote attacker uploading pirated software to a compromised FTP server.",
        "mitre": "T1105 - Ingress Tool Transfer",
        "severity": "HIGH",
        "indicators": "Large src_bytes via FTP, anonymous login, num_file_creations spike",
        "recommendation": "Disable anonymous FTP, enforce upload restrictions, monitor file integrity.",
    },
    "guess_passwd": {
        "category": "R2L",
        "description": "Brute-force password guessing attack against remote login services.",
        "mitre": "T1110.001 - Password Guessing",
        "severity": "HIGH",
        "indicators": "num_failed_logins > 0, repeated login attempts, same source IP",
        "recommendation": "Enforce account lockout, deploy MFA, implement fail2ban or equivalent.",
    },
    "ftp_write": {
        "category": "R2L",
        "description": "Exploiting anonymous FTP write access to plant malicious files on the server.",
        "mitre": "T1190 - Exploit Public-Facing Application",
        "severity": "HIGH",
        "indicators": "Anonymous FTP session, num_file_creations > 0, write commands observed",
        "recommendation": "Disable anonymous FTP write, audit FTP permissions, monitor uploaded files.",
    },
    "imap": {
        "category": "R2L",
        "description": "Exploitation of IMAP buffer overflow vulnerability for unauthorized access.",
        "mitre": "T1190 - Exploit Public-Facing Application",
        "severity": "HIGH",
        "indicators": "Malformed IMAP commands, root_shell=1 post-connection, service crash",
        "recommendation": "Patch IMAP server immediately, restrict IMAP access by IP, monitor auth logs.",
    },
    "multihop": {
        "category": "R2L",
        "description": "Multi-hop attack using intermediate compromised hosts to obscure attacker origin.",
        "mitre": "T1090 - Proxy",
        "severity": "HIGH",
        "indicators": "Unusual routing paths, multiple intermediate hops, is_guest_login=1",
        "recommendation": "Deploy network flow analysis, monitor for lateral movement, enforce zero-trust segmentation.",
    },
}


def generate_brief(detected_classes: list, model_name: str, confidences: dict = None) -> str:
    lines = []
    lines.append("=" * 65)
    lines.append("        THREAT INTELLIGENCE BRIEF")
    lines.append(f"        Model: {model_name}")
    lines.append("=" * 65)

    threat_classes = [c for c in detected_classes if c != "normal"]
    if not threat_classes:
        lines.append("\n[INFO] No threats detected. All traffic classified as normal.\n")
        lines.append("=" * 65)
        return "\n".join(lines)

    for cls in threat_classes:
        info = THREAT_BRIEFS.get(cls, {
            "category": "Unknown",
            "description": f"Unknown threat class: {cls}",
            "mitre": "N/A",
            "severity": "UNKNOWN",
            "indicators": "N/A",
            "recommendation": "Investigate manually.",
        })

        confidence_str = ""
        if confidences and cls in confidences:
            confidence_str = f"  |  Confidence: {confidences[cls]:.1f}%"

        lines.append(f"\n[THREAT DETECTED] {cls.upper()} ({info['category']}){confidence_str}")
        lines.append("-" * 65)
        lines.append(f"Description:     {info['description']}")
        lines.append(f"MITRE ATT&CK:    {info['mitre']}")
        lines.append(f"Severity:        {info['severity']}")
        lines.append(f"Indicators:      {info['indicators']}")
        lines.append(f"Recommended:     {info['recommendation']}")
        lines.append("-" * 65)

    lines.append("\n[NOTE] This brief simulates a RAG retrieval layer. In a production")
    lines.append("system, these summaries would be generated by querying a vector")
    lines.append("database of MITRE ATT&CK entries and CVE records via an LLM.")
    lines.append("=" * 65)
    return "\n".join(lines)
