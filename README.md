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


## `Dockerfile` for web application
    FROM python:3.8

    WORKDIR /usr/src/app
    COPY . .

    RUN pip install Flask
    RUN pip install python-dotenv

    EXPOSE 5000

    CMD ["python", "./app.py"]

## `Dockerfile` for nginx
    FROM nginx:latest

    RUN rm /etc/nginx/conf.d/default.conf

    COPY nginx.conf /etc/nginx/nginx.conf

    # debugging
    #RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/nginx.conf
    #RUN service nginx start
    #RUN nginx -t

    EXPOSE 80

## Docker compose file `compose.yaml`
    version: '3.8'

    services:
        nginx-reverse-proxy:
            build:
                context: nginx-reverse-proxy/
                dockerfile: Dockerfile
            ports:
                - "80:80"
            depends_on:
                - flask
            networks:
                - back-tier

        flask:
            build:
                context: .
                dockerfile: Dockerfile
            ports:
                - "5000:5000"
            networks:
                - back-tier

    networks:
        back-tier:
            driver: bridge