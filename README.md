# Subdomain Takeover: A Comprehensive Guide

## Introduction

Subdomain takeover is a serious security vulnerability where an attacker gains control over a subdomain (e.g., `vuln.g-ml.it`) of a target domain. This typically occurs when a subdomain's DNS record (CNAME) points to an external service that has been removed or deactivated.

**Analogy:** Imagine a subdomain as an electrical outlet. If you remove your appliance (host) from the outlet, someone else can plug in their device. To prevent this, you must cut the power at the source (DNS).

## Impact

If an attacker successfully takes over a subdomain, they can:

* **Read cookies** set from the main domain, potentially compromising user sessions.
* Perform **cross-site scripting (XSS)** attacks to inject malicious code.
* **Circumvent content security policies (CSP)**, undermining security measures.

## How It Happens

### 1. Provisioning (Setup) Phase

If you set up a subdomain to point to an external service (e.g., a blog platform) before the service is fully active, an attacker might be faster and claim the subdomain on that service first.

### 2. Deprovisioning Phase

If you remove the service but forget to remove the DNS record, an attacker can create a new account on that service and claim your subdomain.

### CNAME Records and Expired Domains

Subdomain takeovers can also occur when a CNAME record points to a domain that has expired. The attacker can register the expired domain and gain control of the subdomain.

## Prevention

1. **Define standardized processes:** Establish clear procedures for both provisioning and deprovisioning hosts.
2. **Order of operations:**
   * **Provisioning:** Claim the virtual host on the external service *before* creating DNS records.
   * **Deprovisioning:** Remove DNS records *before* removing the virtual host.
3. **Inventory management:** Maintain a complete inventory of all domains, subdomains, and their associated services. Regularly update this inventory to identify dangling DNS records.

## Additional Notes

* **Subdomain takeovers are a significant security risk.** Always treat them seriously and report any findings responsibly.
* **This guide provides an overview of subdomain takeover vulnerabilities.** Deeper research and understanding are recommended for comprehensive protection.

## Esempio Pratico: Attacco su GitHub Pages

1. **Acquisto Dominio:** Ho acquistato il dominio `g-ml.it` su register.it.
2. **Creazione Sottodominio:** Ho creato il sottodominio vulnerabile `vuln.g-ml.it`.
3. **Configurazione DNS Errata:** Ho aggiunto un record CNAME nel DNS che punta a un servizio inesistente (`nonexistent-dotcom.github.io`) su GitHub Pages.
4. **Verifica della Vulnerabilità:** Dopo la propagazione del record, ho verificato che il sottodominio restituisse un errore 404, confermando la vulnerabilità.
5. **Creazione Account GitHub:** Ho creato un account GitHub con lo stesso nome del servizio inesistente (`nonexistent-dotcom`).
6. **Creazione Repository:** Ho creato un repository pubblico su GitHub chiamato `nonexistent-dotcom.github.io`.
7. **Preparazione del Contenuto:**
   * Ho inserito un file `index.html` con il mio contenuto dannoso.
   * Ho inserito un file `CNAME` contenente il nome del sottodominio vulnerabile (`vuln.g-ml.it`).
8. **Deploy Automatico:** GitHub Pages ha effettuato il deploy automatico, verificando la disponibilità del dominio e assegnandocelo.
9. **Takeover Completato:** Dopo la propagazione del record, visitando `vuln.g-ml.it`, il mio contenuto è stato servito dal provider della vittima.
10. **Possibili Attacchi:** A questo punto, potrei sfruttare il sottodominio per attacchi come:
    * Furto di cookie
    * Phishing
    * Aggiramento della CORS policy
   
## Additional Notes on the attack
Se non avessi indizi non ho altra possibilità se non utilizzare strumenti come amass per ottenere informazioni riguardo possibili sottodomini,
Lancio il comando : `amass enum -d example.com`
nell'output cerco dei CNAME record
