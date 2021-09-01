FROM node
WORKDIR /frontend_docker
COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . .
CMD ["npm", "start"]