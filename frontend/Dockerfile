# Use an official Nginx runtime as a parent image
FROM nginx:latest

# Copy frontend files (HTML, CSS, JavaScript, etc.) to the Nginx default serving directory
COPY . /usr/share/nginx/html

# Copy the custom nginx.conf into the container
# RUN rm /etc/nginx/conf.d/default.conf

# COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 to the outside world
# EXPOSE 80

# Start Nginx when the container is run
CMD ["nginx", "-g", "daemon off;"]
