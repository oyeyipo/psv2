FROM node:12.18.2-slim AS nodebase
WORKDIR /app
COPY package.json yarn.lock ./app/
RUN yarn && yarn cache clean --force
ENV PATH ./node_modules/.bin/:$PATH