FROM python:3.7

# python
RUN DEBIAN_FRONTEND=noninteractive; \
    apt-get update &&\
    apt-get  -y -q install apt-utils &&\
    apt-get --yes -q install dialog vim curl

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# django-mssql-backend
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list &&\
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
ENV ACCEPT_EULA Y
RUN apt-get update &&\
    apt-get -y -q install mssql-tools unixodbc-dev

# python-ldap
RUN apt-get -y -q install libsasl2-dev libldap2-dev libssl-dev

# clean
RUN apt-get clean &&\
    apt-get autoclean

# Dev env
ENV LANG C.UTF-8
ENV PROJECT_NAME proj
WORKDIR /$PROJECT_NAME
COPY ./$PROJECT_NAME/requirements.txt .
COPY ./$PROJECT_NAME/packages/* ./packages/
RUN python -m pip install --upgrade pip &&\
    pip install -r requirements.txt

EXPOSE 8888
