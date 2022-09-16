from fastapi import FastAPI
import uvicorn
import streamlit
import querydb

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Databricks"}

@app.get("/querydb")
async def query():
    return query.querydb()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
