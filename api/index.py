# Bisu G
from fastapi import FastAPI, Query
from fastapi.responses import Response, HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import os
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

MODELS = {
    "realistic_vision": "SG161222/Realistic_Vision_V5.1_noVAE",
    "dreamshaper": "Lykon/DreamShaper-v7",
    "sdxl": "stabilityai/stable-diffusion-xl-base-1.0",
    "deliberate": "XpucT/Deliberate",
    "anything_v5": "stabilityai/stable-diffusion-2-1",
    "protogen": "darkstorm2150/Protogen_x5.8",
    "flux": "black-forest-labs/FLUX.1-dev"
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Homepage showing how to use the API"""
    return templates.TemplateResponse("index.html", {"request": request, "models": MODELS})

@app.get("/generate")
async def generate_image(
    model: str = Query("realistic_vision"),
    prompt: str = Query("A futuristic city at sunset")
):
    """Generate image from Hugging Face model"""
    token = os.getenv("HUGGINGFACE_TOKEN")
    if not token:
        return JSONResponse({"error": "Missing Hugging Face API token"}, status_code=401)

    model_id = MODELS.get(model, MODELS["realistic_vision"])
    url = f"https://api-inference.huggingface.co/models/{model_id}"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"inputs": prompt}

    try:
        resp = requests.post(url, headers=headers, json=payload)
        if resp.status_code != 200:
            return JSONResponse({
                "error": "Failed to fetch from Hugging Face API",
                "details": resp.json()
            }, status_code=resp.status_code)

        return Response(content=resp.content, media_type="image/png")
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
