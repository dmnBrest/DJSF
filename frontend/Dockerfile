FROM node:9
RUN npm config set user 0
RUN npm config set unsafe-perm true
RUN npm install --global webpack@3.10.0
RUN mkdir /code
RUN mkdir /dist
WORKDIR /code
COPY ./ /code
RUN npm install