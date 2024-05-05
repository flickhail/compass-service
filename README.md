Finished project that contains simple web server + nginx reverse proxy configuration for that web application.
Both nginx and web server have dockerfiles for building them and compose.yaml for building and starting their containers.

- **curl_docker_image** is for debugging purposes
- **flask** is a folder that contains Flask library
- **nginx-reverse-proxy** is a folder that contains a configuration file for nginx as a reverse proxy and a dockerfile for building a container
- **templates** is a folder that contains a html template (or other potentional templates) for flask app to render
- **.env** is a file that contains IP_ADDRESS and PORT enviromental variables for Flask App to listen to
- **Dockerfile** is a file to build the Flask Web server
- **app.py** is a file with python code that contains web server implementation
- **compose.yaml** contains configuration for docker compose that builds web server and nginx dockerfiles