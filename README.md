# Microservice template with fastapi
## Overview
Base template example with two services that communicate with eachother via HTTP. Configured and ready for base development.

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
