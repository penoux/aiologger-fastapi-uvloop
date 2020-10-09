# aiologger-fastapi-uvloop

Sample projet to reproduce locally the crash issue [#82](https://github.com/b2wdigital/aiologger/issues/82) on `aiologger` with `uvloop`.

It uses `uvicorn` and [FastAPI](https://fastapi.tiangolo.com/).

To reproduce the issue, I use [K6](https://k6.io/) load testing tool with the simple script `k6_load.js` to send simple GET('http://127.0.0.1:8000/') requests in parallel. Any other simple test tool, even `curl` may be used, as soon as it can send requests in parallel.

```bash
# In one terminal T1, launch uvicorn app: simple root API endpoint with logging.
uvicorn main:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [8715] using watchgod
INFO:     Started server process [8726]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

# In another terminal T2, K6 load https://k6.io/
# Single request OK
k6 run k6_load.js

# Few load (10 virtual users, 1O reqs/user)
k6 run k6_load.js --vus 10 --iterations 100
...
CTRL-C (app crashed)

# In terminal T1:
...
Assertion failed: (loop->watchers[w->fd] == w), function uv__io_stop, file src/unix/core.c, line 932.
```
