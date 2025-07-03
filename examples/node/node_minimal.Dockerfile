FROM node:18

WORKDIR /app

COPY . .

RUN npm ci && npm run build && npm prune --production

CMD ["node", "dist/server.js"]
