from fastapi import FastAPI
from route import router

app = FastAPI()

app.include_router(router)

@app.get("/")
async def read_root():
    return {"message": "Server is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)