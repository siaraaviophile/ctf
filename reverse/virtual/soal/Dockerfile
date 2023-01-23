FROM php:7.3
RUN apt update && apt upgrade -y && apt update --fix-missing
RUN apt install socat -y

COPY . .
RUN echo "ITCLUB{s1mpl3_v1rtual_sh3ll_23342}" > flag.txt

RUN chmod 700 /usr/bin/* /bin/* /tmp /dev/shm
RUN chmod 755 /usr/bin/env /bin/dash /bin/bash /bin/sh /bin/cat /usr/bin/groups /usr/bin/id /bin/ls

EXPOSE 30000

CMD socat TCP-LISTEN:30000,reuseaddr,fork EXEC:"php main.php",su=nobody
