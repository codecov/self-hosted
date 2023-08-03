FROM --platform=linux/amd64 codecov/enterprise-api:latest-stable

USER root
RUN apk add --no-cache openssl postgresql libgcc libstdc++ ncurses-libs
RUN ln -s /usr/lib/libgcc_s.so.1 /usr/lib/libgcc_s-a04fdf82.so.1
USER codecov
