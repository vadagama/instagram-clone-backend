from fastapi import FastAPI, status, Response, Query, Body, Path, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse, FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict
from fastapi.staticfiles import StaticFiles


app = FastAPI()


@app.get("/")
def root():
    return "Hello"