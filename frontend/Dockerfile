# frontend/Dockerfile

# Use an official Nginx image as a parent image
FROM nginx:1.27-alpine

# Copy the static HTML content from the current directory to Nginx's web root directory
COPY ./index.html /usr/share/nginx/html/index.html

# (Optional) If you have other static assets like CSS, JS, or images, copy them too:
# COPY ./css/ /usr/share/nginx/html/css/
# COPY ./js/ /usr/share/nginx/html/js/
# COPY ./images/ /usr/share/nginx/html/images/

# Expose port 80 (Nginx default port)
EXPOSE 80

# The default Nginx command will start the server.
# No explicit CMD is needed unless you want to override the default.
