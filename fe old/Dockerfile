FROM node:12
ENV HOST 0.0.0.0
EXPOSE 3000
ENV APP_ROOT /app
WORKDIR ${APP_ROOT}
RUN curl -o- -L https://yarnpkg.com/install.sh | bash
RUN npm install -g core-js@3
RUN npm install -g nuxt
COPY package.json /${APP_ROOT}/package.json
COPY yarn.lock /${APP_ROOT}/yarn.lock
RUN yarn install --ignore-engines

COPY . ${APP_ROOT}
