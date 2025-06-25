<!-- Language Bar (automated on commit) -->
{{lang_url_bar}}

---

<!-- File Header Metadata Block -->
{{file_header_block}}

---

<img src="docs/en/assets/bw-git-banner.png" alt="Bluewater"/>

# 🛡️ Bluewater Scripts Security Policy

## Supported Versions

We support the latest stable release of the **Bluewater Scripts** repository.  
Please use the most recent version to ensure you have the latest security patches and safe automation practices.

| Version    | Supported        | Security Updates |
|------------|------------------|------------------|
| 1.x        | ✔️ Yes (current) | ✔️ Yes           |
| 0.x (beta) | ❌ No             | ❌ No             |

---

## Reporting a Vulnerability

**Please do NOT open a public issue or pull request for security concerns involving scripts or automation.**

If you discover a security vulnerability or sensitive issue in Bluewater scripts, onboarding tools, or Git hooks, report it privately by email:

- Email: **security@bluewaterphp.org**  
  (update this address as needed for your team)

To help us triage and resolve your report, please use the template below.

---

### Security Report Email Template

Copy and fill out this template, then email it to [security@bluewaterphp.org](mailto:security@bluewaterphp.org).

```

Subject: \[Security] Vulnerability Report for Bluewater Scripts

Hello Bluewater Team,

I would like to report a security vulnerability in Bluewater's automation scripts, onboarding tools, or Git hooks.

## Summary

A brief, high-level description of the issue.

## Affected script(s) or workflow(s)

Specify where the vulnerability exists (e.g., script filename, onboarding process, workflow step).

## Details and Steps to Reproduce

1. Step-by-step instructions to trigger the vulnerability
2. Example payload, command, or misuse scenario

## Impact

Explain the risk or possible consequences (e.g., code execution, privilege escalation, data loss, supply-chain risk).

## Remediation suggestions (optional)

If you have an idea for a fix, describe it here.

## Disclosure preference

* [ ] You may credit me publicly
* [ ] I wish to remain anonymous

## Contact info

How we can reach you for follow-up (if not this email)

Thank you for handling this report responsibly.

```

---

## What Happens Next

- **Acknowledgment:** We will confirm receipt of your report within 72 hours.
- **Investigation:** Maintainers will review and assess the issue.
- **Coordination:** We will coordinate with you about progress and fixes. You may choose to be credited or remain anonymous.
- **Resolution:** If confirmed, we will fix the issue as quickly as possible and coordinate responsible disclosure if necessary.
- **Public Advisory:** When a fix is released, we will publish a security advisory and credit the reporter if desired.

---

## Security Researcher Guidelines

- Act in good faith to avoid privacy violations, privilege escalation, or service interruption.
- Avoid accessing or modifying data that is not your own.
- Give us reasonable time (we aim for 30 days max) to resolve the issue before any public disclosure.

---

## Scope

This policy applies to vulnerabilities in **all automation scripts, onboarding tools, Git hooks, and supporting workflows** maintained by the Bluewater project.

- If your issue relates to the framework or documentation, see the relevant SECURITY.md in those repositories.
- Supply-chain, dependency, or workflow misconfiguration vulnerabilities are covered.

## 📝 License

All content in this repository is licensed under the [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/).

---

{{last_updated}}
