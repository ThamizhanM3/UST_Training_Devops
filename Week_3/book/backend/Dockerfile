# backend/Dockerfile
FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
# Prefer dev deps not installed in prod images
# If nodemon is in dependencies, move it to devDependencies first.
RUN npm ci --omit=dev

COPY . .

ENV NODE_ENV=production
EXPOSE 5555
CMD ["node", "index.js"]
