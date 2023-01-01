FROM ruby:2.7.7-slim-bullseye

COPY . /docs/

WORKDIR /docs

RUN apt-get update \ 
    && apt-get install -y ubuntu-dev-tools \
    && gem install bundler:1.16.0 \
    && bundle install

CMD ["bundle", "exec", "jekyll", "serve", "--livereload", "--host", "0.0.0.0"]