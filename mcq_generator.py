from typing import Annotated
from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from mcq_generator import * 
from scrapper import *
from openai_handler import *

router_gen_mcq = APIRouter(
    prefix='/process',
    tags=['process']
)


class URL(BaseModel): 
    url: str

@router_gen_mcq.post("/urls", response_model= list[dict])
async def process_urls(url: URL):
    data_scrapper = data_scrapper()
    data_scrapper.scrape_web_content(url)
    data = data_scrapper.myWebData
    data = data[:1500]
    '''
    for the sake of simplicity we will consider only three chuncks of 500 words
    CHUNK_SIZE = 500
    chunk1 = data[:CHUNK_SIZE]
    chunk2 = data[CHUNK_SIZE:CHUNK_SIZE*2]
    chunk3 = data[CHUNK_SIZE*2:CHUNK_SIZE*3]
    '''
    
    mcq_generate_obj = MCQGenerator()
    mcq_generate_obj.generate(data)
    
    return mcq_generate_obj.mcqs
    
@router_gen_mcq.post("/pdf", response_model= list[dict])
async def upload_pdf(pdf: UploadFile = File(...)):
    
    # Check if the uploaded file is a PDF
    if pdf.filename.endswith(".pdf"):
        data_scrapper = data_scrapper()
        data_scrapper.scrape_pdf_content(pdf)
        data = data_scrapper.myPdfData
        data = data[:1500]
        
        mcq_generate_obj = MCQGenerator()
        mcq_generate_obj.generate(data)
    
        return mcq_generate_obj.mcqs
    
    else:
        return JSONResponse(content={"error": "Please upload a PDF file"}, status_code=400)