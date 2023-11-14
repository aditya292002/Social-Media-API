# from typing import Annotated
from fastapi import APIRouter
from icecream import ic
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from mcq_generator import * 
from scrapper import *
from openai_handler import *
import asyncio

router_gen_mcq = APIRouter(
    prefix='/process',
    tags=['process']
)


class URL(BaseModel): 
    url: str




async def test(user_input):
    ic(user_input)
    
    thread = client.beta.threads.create()
    
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input
    )

    ic(client.beta.threads.messages.list(thread_id=thread.id).data)
    
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
        instructions="""
        Generate at most 1 multiple choice questions. 
        user json format for each question, and return list of json objects [
            {
                question : "question1"
                options : [option1, option2, option3, option4]
                answer: "optionx with, 1 line explantion"
            }
            ....
        ]
        """
    )    
    
    

    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        await asyncio.sleep(3)
        print(run.status)
        print(user_input[:10])
        if run.status in ("completed", "failed"):
            break
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    latest_message = messages.data[0]
    text = latest_message.content[0].text.value

    # deleting the thread
    response = client.beta.threads.delete(thread.id)
    ic(response)

    return text
        


@router_gen_mcq.post("/urls")
async def process_urls(url: URL):
    print(url)
    data_scrapper_obj = data_scrapper()
    print(data_scrapper_obj)
    data_scrapper_obj.scrape_web_content(url.url)
    data = data_scrapper_obj.myWebData
    
    # for the sake of simplicity and avoid overuse of API i am considering only 3 chunks of data
    data = data[:min(len(data), 1600)]
    chunks = []
    ind = 0
    count_chunks = 0
    while(ind < len(data) and count_chunks < 3):
        chunks.append(' '.join(data[ind:ind+500][:30]))
        ind += 500
        count_chunks += 1
        
    ic(chunks)

    L = await asyncio.gather(*(test(chunk) for chunk in chunks))
    return L
      
    
    
@router_gen_mcq.post("/pdf", response_model= list[dict])
async def upload_pdf(pdf: UploadFile = File(...)):
    
    # Check if the uploaded file is a PDF
    if pdf.filename.endswith(".pdf"):
        data_scrapper = data_scrapper()
        data_scrapper.scrape_pdf_content(pdf)
        data = data_scrapper.myPdfData
        data = data[:1500]
        
        # for the sake of simplicity and avoid overuse of API i am considering only 3 chunks of data
        data = data[:min(len(data), 1600)]
        chunks = []
        ind = 0
        count_chunks = 0
        while(ind < len(data) and count_chunks < 3):
            chunks.append(' '.join(data[ind:ind+500][:30]))
            ind += 500
            count_chunks += 1
            
        ic(chunks)

        L = await asyncio.gather(*(test(chunk) for chunk in chunks))
        return L
        
    else:
        return JSONResponse(content={"error": "Please upload a PDF file"}, status_code=400)
    
    
    
    
    
    
    
    
    
    
    