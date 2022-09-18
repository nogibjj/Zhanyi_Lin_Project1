from fastapi import FastAPI
import uvicorn
import querydb
import query_sql
import spark

app = FastAPI()


@app.get("/")
async def root():
    
    #return {"result": querydb.querydb(team1, team2)}
    return {"message": "Give more information to get the result"}

@app.get("/{team1}/{team2}")
async def test_query(team1, team2):
    
    return {"result": querydb.querydb(team1, team2)}
    #return {"result": querydb.querydb()}

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0")
