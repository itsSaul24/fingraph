from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv(".env.local")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("FinGraph API starting up...")
    # Stuff
    yield
    # Shutdown
    print("FinGraph API shutting down...")
    # More stuff


app = FastAPI(
    title="FinGraph API",
    description="Financial Entity Intelligence Platform API",
    version="0.1.0",
    lifespan=lifespan,
)

# Configure CORS - frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://your-domain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to FinGraph API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
