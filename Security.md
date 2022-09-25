# Security Policy

## Product Security
### SSO
All access and sign-ins are conducted via an SSO provider: GitHub, GSuite, and many other platforms are supported.
We can work with your IT team to integrate to your provider of choice. We do not store customer passwords.

### Credential Storage
We encrypt sensitive customer data (e.g. secrets, authentication tokens) at-rest with AES256 as described in Google's documentation.

## Permissions and Role-Based Access Control
Our permission levels inherit from the permissions you have assigned in GitHub.
Users with write access to a GitHub repository for a given app will be able to make changes in the administrative console.
Only users with admin access to a repository are able to deploy and delete apps.

## Network and Application Security
### Data Hosting
Our physical infrastructure is hosted and managed within Google Cloud Platform (GCP) using their secure data centers.
We leverage many of the platform's built-in security, privacy, and redundancy features. 
GCP continually monitors its data centers for risk and undergoes assessments to ensure compliance with industry standards. 
GCP's data centers have numerous accreditations, including ISO-27001, SOC 1 and SOC 2.

### Virtual Private Cloud
All of our servers are within a virtual private cloud (VPC) with firewalls and network access control lists (ACLs) to allow
external access to a select few API endpoints; all other internal services are only accessible within the VPC.

### Encryption
All apps are served entirely over HTTPS. All data sent to or from Application over the public internet is encrypted
in transit using 256-bit encryption. Our API and application endpoints are TLS only (v1.2). We use only strong cipher suites
and HTTP Secure Transport Security (HSTS) to ensure browsers interact with apps over HTTPS. 
We also encrypt data at rest using AES-256.

## Permissions and Authentication
Access to customer data is limited to authorized employees who require it for their job. We run a zero-trust corporate network
so there are no corporate resources or additional privileges gained from being on our internal network.
We utilize single sign-on, 2-factor authentication (2FA), and enforce strong password policies
to ensure access to all cloud-related services are protected.

## Incident Response
We have an internal protocol for handling security events which includes escalation procedures, rapid mitigation,
and documented post-mortems. We notify customers promptly and publicize security advisories at https://about.me/yugalnandurkar

## Penetration Testing
We use third-party security tools to scan for vulnerabilities on a regular basis.
Our security partners conduct periodic, intensive penetration tests on the platform.
Our product development team immediately responds to any identified issues or potential vulnerabilities to ensure
the quality and security of applications.

## Security and Compliance Programs
### Certifications
SOC 2 Type 1
We're committed to meeting industry security standards and are SOC2 readiness certified. SOC2 compliant

## People
### Background Checks
All employees go through a thorough background check before hiring.

### Training
We take a least-privilege approach to the access and handling of data. While we retain a minimal amount of 
customer data and limit internal access on a need-to-know basis, all employees are required to review related 
security policies and are trained on proper data handling to ensure they uphold our strict commitment to the
privacy and security of your data.

### Confidentiality
All employees sign a confidentiality agreement before they start.

## Vulnerability Control
### Vulnerability Management
We keep our systems up-to-date with the latest security patches and continuously monitor for new vulnerabilities
through compliance and security mailing lists. This includes automatic scanning of our code repositories for vulnerable dependencies.
