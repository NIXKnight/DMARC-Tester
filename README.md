# DMARC Tester

This repo contains a docker-compose.yml file that spins up a Postfix open relay and uses the script `scripts/send_email.py` to send an email through the open relay.

If the DMARC record is setup to be strict, the email from this open relay will be bounced.

Use it as follows. Export the variables as per your requirement:
```bash
export ALLOWED_SENDER_DOMAINS=example.com
export SENDER_EMAIL=default_sender@example.com
export RECIPIENT_EMAIL=default_recipient@example.com
docker compose up
```
