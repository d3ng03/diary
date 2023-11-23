# Use the official MySQL image as the base image
FROM mysql:latest

# Set environment variables for MySQL configuration
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=diary
ENV MYSQL_USER=cn_user
ENV MYSQL_PASSWORD=cn_password
ENV MYSQL_CHARSET=utf8mb4
ENV MYSQL_COLLATION=utf8mb4_unicode_ci
ENV MYSQL_AUTH_PLUGIN=mysql_native_password

# Copy the initialization SQL script to the /docker-entrypoint-initdb.d/ directory
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the MySQL port
# EXPOSE 3306

