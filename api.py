from fastapi import FastAPI
from starlette.responses import FileResponse
import os

from uuid import uuid4
from graphing import *
from enum import Enum


class Types(str, Enum):
    age = 'age'
    gender = 'gender'
    marital = 'marital'
    language = 'language'
    state = 'state'
    country = 'country'


app = FastAPI()
if not os.path.exists("graph_output"):
    os.makedirs('graph_output')


@app.get("/")
async def read_root():
    return {"message" : "Welcome to the demographic Bar Charting Service. You can eiher search for data using"
                        "/data/{type}, or by requesting a graph by using /graph/{type}.",
            "types": ["age", "gender", "marital", "language", "state", "country"]}


@app.get("/graph/{graph_type}")
async def get_graph(graph_type: Types):
    data = None
    if graph_type == Types.age:
        data = agegraph()
    if graph_type == Types.gender:
        data = gendergraph()
    if graph_type == Types.marital:
        data = maritalgraph()
    if graph_type == Types.language:
        data = languagegraph()
    if graph_type == Types.state:
        data = stategraph()
    if graph_type == Types.country:
        data = countrygraph()

    if data is not None:
        filename = str(uuid4()) + ".png"
        data.savefig(os.path.join("graph_output", filename))
        return FileResponse(os.path.join("graph_output", filename))
    else:
        return{"message": "Something has went wrong"}


@app.get("/data/{data_type}")
async def get_data(data_type : Types):

    data = None
    if data_type == Types.age:
        data = agedata()
    if data_type == Types.gender:
        data = genderdata()
    if data_type == Types.marital:
        data = maritaldata()
    if data_type == Types.language:
        data = languagedata()
    if data_type == Types.state:
        data = statedata()
    if data_type == Types.country:
        data = countrydata()

    return{"data": data}

