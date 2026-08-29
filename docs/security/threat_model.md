# GuardPay AI Security Threat Model

## 1. Assets

GuardPay must protect:

- User data
- Product/catalog data
- Application configuration
- LLM credentials
- API credentials
- Internal system information
- Business logic
- Tool permissions
- Payment-related operations
- Model inputs and outputs

## 2. Trust Boundaries

### Boundary 1 — User → GuardPay

User input is untrusted.

### Boundary 2 — GuardPay → LLM

The LLM must not be trusted to enforce business rules.

### Boundary 3 — LLM → Application

LLM-generated output must be validated before use.

### Boundary 4 — Application → Tools

Tools must have explicit permissions.

### Boundary 5 — Application → External Services

External services must not receive unrestricted internal data.

## 3. Threats

### Prompt Injection

An attacker attempts to manipulate the model through malicious instructions.

### Jailbreaking

An attacker attempts to bypass model or application restrictions.

### Sensitive Information Disclosure

The system accidentally exposes secrets or internal information.

### Tool Abuse

An attacker attempts to cause the AI system to perform unauthorized operations.

### Excessive Agency

The AI performs actions beyond what the user intended.

### Output Manipulation

Malicious or malformed model output influences application behavior.

### Denial of Service

An attacker sends expensive or excessive requests.

### Data Poisoning

Untrusted data influences retrieval, ranking, or model behavior.

## 4. Security Principles

GuardPay follows these principles:

1. Never trust raw user input.
2. Never trust raw LLM output.
3. Validate structured model output.
4. Keep business rules deterministic.
5. Apply least privilege to tools.
6. Separate planning from execution.
7. Log security-relevant events.
8. Never expose secrets or internal errors.
9. Fail closed for sensitive operations.
10. Every security decision should be observable.