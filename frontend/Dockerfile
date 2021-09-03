FROM node:16-alpine3.11
WORKDIR /frontend_docker
COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . .
CMD ["npm", "start"]