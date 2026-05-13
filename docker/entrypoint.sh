#!/bin/bash
set -e

# ============================================================
# Network firewall: whitelist-only outbound access
# Only allow DNS + OpenAI API + Azure OpenAI API
# Everything else (GitHub, Google, etc.) is blocked
# ============================================================

# Allow loopback
iptables -A OUTPUT -o lo -j ACCEPT

# Allow established connections (replies to our requests)
iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow DNS (needed to resolve API hostnames)
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 53 -j ACCEPT

# Whitelist API domains by resolving their IPs
# OpenAI API
API_HOSTS="api.openai.com"

# Azure OpenAI (if AZURE_OPENAI_HOST is set)
if [ -n "${AZURE_OPENAI_HOST:-}" ]; then
    API_HOSTS="$API_HOSTS $AZURE_OPENAI_HOST"
fi

for host in $API_HOSTS; do
    for ip in $(dig +short "$host" 2>/dev/null | grep -E '^[0-9]'); do
        iptables -A OUTPUT -d "$ip" -p tcp --dport 443 -j ACCEPT
        echo "[entrypoint] Allowed: $host -> $ip"
    done
done

# Drop everything else
iptables -A OUTPUT -j DROP

echo "[entrypoint] Firewall configured: only API endpoints allowed, all other traffic blocked"

# Fix ownership of mounted config files for bench user
if [ -f /mnt/codex-config.toml ]; then
    mkdir -p /home/bench/.codex
    cp /mnt/codex-config.toml /home/bench/.codex/config.toml
    chown -R bench:bench /home/bench/.codex
fi

# Drop privileges and exec the command as bench user
exec gosu bench "$@"
