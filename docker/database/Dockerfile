FROM redis:7.0.11

LABEL maintainer="Erik Herazo <erickherazoj@gmail.com>"

EXPOSE 6379

COPY redis.conf /usr/local/etc/redis/redis.conf

CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]