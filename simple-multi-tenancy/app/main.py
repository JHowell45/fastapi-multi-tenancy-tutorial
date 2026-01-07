import uvicorn
from fastapi import FastAPI

from app.routers import bands

app = FastAPI(title="Simple Multi Tenancy")

app.include_router(bands.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
