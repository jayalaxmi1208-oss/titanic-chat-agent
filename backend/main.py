from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

from agent import create_agent
from visualizer import generate_visualization
from logger import setup_logger

app = FastAPI()
logger = setup_logger()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Correct static path


base_dir = os.path.dirname(os.path.abspath(__file__))
static_path = os.path.join(base_dir, "static")

app.mount("/static", StaticFiles(directory=static_path), name="static")

llm, df, prompt = create_agent()

class Query(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "Backend running successfully"}

@app.post("/ask")
async def ask_question(query: Query):
    try:
        formatted_prompt = prompt.format(
          rows=len(df),
          columns=", ".join(df.columns),
          question=query.question
)

        response = llm.invoke(formatted_prompt)
        answer = response.content
        plot_path = generate_visualization(df, query.question)

        logger.info(f"Question: {query.question}")

        return {
            "answer": answer,
            "plot": plot_path
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))