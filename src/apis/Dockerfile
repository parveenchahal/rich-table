FROM python:3.9.0b5-alpine3.12
COPY . /app
WORKDIR /app

RUN apk update
RUN apk add bash
RUN apk add curl
RUN apk add jq
RUN apk add g++
RUN apk add --no-cache unixodbc-dev
RUN apk add libffi-dev
RUN apk add libressl-dev
RUN python -m pip install --upgrade pip
RUN pip install -r python-dependencies.txt

#Download the desired package(s)
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.5.2.2-1_amd64.apk
RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/mssql-tools_17.5.2.1-1_amd64.apk

#Install the package(s)
RUN apk add --allow-untrusted msodbcsql17_17.5.2.2-1_amd64.apk
RUN apk add --allow-untrusted mssql-tools_17.5.2.1-1_amd64.apk

EXPOSE 5000/tcp
RUN chmod +x startup.sh
CMD ["bash", "startup.sh"]