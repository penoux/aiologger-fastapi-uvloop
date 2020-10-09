import uvicorn
from fastapi import FastAPI
from aiologger import Logger


logger = Logger.with_default_handlers(name='my-logger')

app = FastAPI()

@app.get("/")
async def test_aiologger():
    # Default : stdout
    await logger.debug("debug")
    await logger.info("info")

    # Default : stderr
    await logger.warning("warning")
    await logger.error("error")
    await logger.critical("critical")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, loop="uvloop")
    # Test : http://127.0.0.1:8000/docs
