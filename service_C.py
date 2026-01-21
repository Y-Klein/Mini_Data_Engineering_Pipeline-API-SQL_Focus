from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post("/")
def root(data_from_service_b:list[dict]):
    return data_from_service_b

if __name__=="__main__":
    uvicorn.run(app,port=8002)