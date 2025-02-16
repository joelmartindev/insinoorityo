from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from llm_app import main
from fastapi import File, UploadFile
from pydantic import BaseModel
import shutil, os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pdf_filepath = None


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def index():
    return FileResponse("front/dist/index.html")


@app.post("/question")
def chat(data: QuestionRequest):
    print(data.question)
    global pdf_filepath
    if pdf_filepath:
        res = main(pdf_filepath, data.question)
        return {"message": res}
    else:
        return {"Hello": "nothing to show :-("}


@app.post("/file")
async def upload_pdf(file: UploadFile = File(...)):
    global pdf_filepath
    if file.content_type != "application/pdf":
        return {"error": "Only PDF files are allowed"}

    os.makedirs("data", exist_ok=True)

    # Clear previous file before saving a new one
    for filename in os.listdir("data"):
        file_path = os.path.join("data", filename)
        os.remove(file_path)

    pdf_filepath = f"data/{file.filename}"

    with open(pdf_filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "message": "File uploaded successfully"}


app.mount("/", StaticFiles(directory="front/dist"), name="front")
