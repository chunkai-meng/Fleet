FROM ubuntu:18.04



# python
RUN apt-get update &&\
    apt-get --yes install vim curl
RUN apt-get update &&\
    apt-get --yes install python3.7 python3-pip

# django-mssql-backend
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list &&\
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
ENV ACCEPT_EULA Y
RUN apt-get update &&\
    apt-get --yes install mssql-tools unixodbc-dev

# python-ldap
RUN apt-get --yes install libsasl2-dev libldap2-dev libssl-dev

# clean
RUN apt-get clean &&\
    apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* &&\
ln -sf /usr/bin/python3.7 /usr/local/bin/python &&\
ln -s /usr/bin/pip3 /usr/bin/pip

# Dev env
ENV LANG C.UTF-8
ENV PROJECT_NAME proj
WORKDIR /$PROJECT_NAME
COPY ./$PROJECT_NAME/requirements.txt .
COPY ./$PROJECT_NAME/packages/* ./packages/
RUN pip install -r requirements.txt

EXPOSE 8888
