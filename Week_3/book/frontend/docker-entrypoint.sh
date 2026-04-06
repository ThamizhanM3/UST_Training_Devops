#!/bin/sh
set -e

# Replace placeholders in config.js with env vars (or defaults)
: "${API_BASE_URL:=http://localhost:3000}"
: "${API_TIMEOUT:=10000}"

# Simple sed replacements
sed -i "s#__API_BASE_URL__#${API_BASE_URL}#g" /usr/share/nginx/html/config.js
sed -i "s#__API_TIMEOUT__#${API_TIMEOUT}#g" /usr/share/nginx/html/config.js

exec "$@"
