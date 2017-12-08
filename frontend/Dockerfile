FROM node:9
RUN npm config set user 0
RUN npm config set unsafe-perm true
RUN npm install -g @angular/cli@1.6.0
RUN mkdir /code
RUN mkdir /dist
WORKDIR /code
COPY ./ /code