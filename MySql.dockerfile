FROM mysql:5.7

RUN docker run --name mysql -p3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql