# ---- Base (build deps only for prod) ----
FROM node:20-alpine AS base
WORKDIR /app

# Install only production deps (no dev)
COPY package*.json ./
RUN npm ci --omit=dev

# Copy source
COPY . .

# ---- Runtime ----
FROM node:20-alpine
WORKDIR /app

# Copy node_modules and source
COPY --from=base /app/node_modules ./node_modules
COPY --from=base /app ./

# Use non-root user
RUN addgroup -S app && adduser -S app -G app
USER app

# Accept runtime envs
ENV NODE_ENV=production \
    PORT=5555

EXPOSE 5555

# Start the API
CMD ["npm", "start"]