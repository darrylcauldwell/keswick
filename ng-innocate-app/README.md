Run python flask app

```bash
python3 app.py
```

It should then be accessible at http://localhost:5000

Build the Docker image from the Dockerfile in your project directory:

```bash
docker build -t flask-docker-image .
```

Once the image is built, you can run a container from it:

```bash
docker run -p 4000:80 flask-docker-image
```

This command maps port 4000 on your host machine to port 80 in the Docker container. You can choose a different port if needed.

Access your Flask app by opening a web browser and navigating to http://localhost:4000 
