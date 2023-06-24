FROM redis:7.0.11

WORKDIR /data

RUN mkdir /redis_data
RUN chmod 777 /redis_data

COPY . .

CMD ["redis-server", "--dir", "/redis_data"]