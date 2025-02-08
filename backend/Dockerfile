FROM php:8.0-apache

WORKDIR /var/www/html

COPY . .

RUN apt-get update && apt-get install -y \
    libpq-dev \
    && docker-php-ext-install pdo pdo_pgsql
