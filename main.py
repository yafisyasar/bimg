# main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

# Create a FastAPI app instance
app = FastAPI()

# This is the crucial part: "Mounting" the static files directory.
# This tells FastAPI to serve all files from the 'web' directory
# when a request comes in. The 'html=True' part tells it to
# automatically look for 'index.html' when a directory is requested.
app.mount("/", StaticFiles(directory="bimg", html=True), name="web")

# This is a standard Python practice to make the script runnable
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
