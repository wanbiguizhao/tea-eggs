FROM ubuntu:18.04
ADD ./sources.list /etc/apt/sources.list

RUN apt-get update -y && apt-get upgrade -y && apt-get install ssh -y
ADD ./sshd_config /etc/ssh/sshd_config
RUN mkdir /var/run/sshd
RUN echo 'root:tea-eggs' |chpasswd
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN mkdir /root/.ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCV0SMm8r9tycALVtCEKWlebDpcRQRq0iunZsu3sFoQaTjG8me9d603c5dnXbEMDNCSNgKvaz6gfJbsFfYq4Gg8qWAPSb10TeveZq65QAzOlpCK0xk/GpyZcJlaXQT5ymbN8I9BlMUosYIWKLwMqC33LoHqycsnxvJKdw++VvgUO3KFrUm+YaHr3/3XxCeBRYzYyUmHiAreqmnaLIcELYmhuk7PiX3Z8gYPJ/DprplDyDUWguwlp+1msBvNJR2afUA22tALP3ZDoEZ5iUHxR1Ml+GkIo1LtH1KWFMtlljwwpymINAz3pUXAg/aZmcN2UFKuivSbALV6TJt6j1pgnTl3 tea-eggs" > /root/.ssh/authorized_keys && chmod 644 /root/.ssh/authorized_keys
RUN apt-get install openssl sudo -y # 安装必须的环境 
# RUN useradd -d /home/ops -p ` openssl passwd -1 'tea-eggs' ` -s /bin/bash ops
RUN useradd ops -m && usermod -aG sudo ops
# 创建测试用户
USER ops
RUN mkdir -p /home/ops/.ssh/  && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCV0SMm8r9tycALVtCEKWlebDpcRQRq0iunZsu3sFoQaTjG8me9d603c5dnXbEMDNCSNgKvaz6gfJbsFfYq4Gg8qWAPSb10TeveZq65QAzOlpCK0xk/GpyZcJlaXQT5ymbN8I9BlMUosYIWKLwMqC33LoHqycsnxvJKdw++VvgUO3KFrUm+YaHr3/3XxCeBRYzYyUmHiAreqmnaLIcELYmhuk7PiX3Z8gYPJ/DprplDyDUWguwlp+1msBvNJR2afUA22tALP3ZDoEZ5iUHxR1Ml+GkIo1LtH1KWFMtlljwwpymINAz3pUXAg/aZmcN2UFKuivSbALV6TJt6j1pgnTl3 tea-eggs" > /home/ops/.ssh/authorized_keys 
RUN chmod   640  /home/ops/.ssh/authorized_keys 
USER root
RUN echo 'ops:tea-eggs' |chpasswd 
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EXPOSE 22
CMD    ["/usr/sbin/sshd", "-D"]