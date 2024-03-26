# Microservice template with fastapi
## Overview
Base template example with two services that communicate with eachother via HTTP. Preconfigured for base development with the option to debug containers with `ipdb`, while attached to the container.

Run the setup on port `http://0.0.0.0:8000` and `http://0.0.0.0:8001`

```bash
$ docker compose up --build -d
...
service_two-1  | INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
service_two-1  | INFO:     Started reloader process [1] using statreload
service_one-1  | INFO:     Will watch for changes in these directories: ['/code']
service_one-1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
service_one-1  | INFO:     Started reloader process [1] using statreload
...
```

Debug service by adding `import ipdb; ipdb.set_trace()` in the code and then attach to the container
```bash
docker attach fastapi_microservice_template-service_one-1
```
