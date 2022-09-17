from fastapi import FastAPI
import uvicorn
import streamlit
import querydb
import query_sql
import spark

app = FastAPI()

@app.get("/")
async def root():
    
    return {"result": querydb.querydb()}
    #return {"message": "Hello Databricks"}

@app.get("/querydb")
async def query():
    return {"message": "Hello Databricks"}
    #return {"result": querydb.querydb()}

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0")
