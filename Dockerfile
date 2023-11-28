FROM node:lts-alpine3.17 AS builder
USER node
RUN mkdir -p /home/node/app && chown -R node:node /home/node/app
WORKDIR /home/node/app
COPY --chown=node:node . .
RUN npm install

EXPOSE 8000
CMD [ "npm", "start" ]