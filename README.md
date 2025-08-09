# 🖼️ AI Image Generator API

A simple **FastAPI** wrapper around Hugging Face inference models to generate images.  
Includes a demo HTML page and instructions to deploy on **Vercel**.

> 👨‍💻 Credit: [bisug](https://github.com/bisug)

---

## 🚀 One-click Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/bisug/Ai-Image-Generator-API&env=HUGGINGFACE_TOKEN&project-name=ai-image-generator&repository-name=ai-image-generator)

When you click the button:
1. Select your Vercel account/team
2. Set `HUGGINGFACE_TOKEN` as an environment variable (required)
3. Deploy

---

## ⚙️ Endpoints

### `GET /`
Returns a demo HTML page showing available models and usage examples.

### `GET /generate`
Generates an image from a Hugging Face model.

**Parameters:**
- `model` — Model key from the list below (default: `realistic_vision`)
- `prompt` — Your text prompt (default: `"A futuristic city at sunset"`)

**Example:**
```bash
GET "/generate?model=sdxl&prompt=A+futuristic+city+at+sunset" --output result.png
```

---

## 📜 Available Models
| Model Key        | Hugging Face Model ID                                  |
|------------------|-------------------------------------------------------|
| realistic_vision | SG161222/Realistic_Vision_V5.1_noVAE                   |
| dreamshaper      | Lykon/DreamShaper-v7                                   |
| sdxl             | stabilityai/stable-diffusion-xl-base-1.0               |
| deliberate       | XpucT/Deliberate                                       |
| anything_v5      | stabilityai/stable-diffusion-2-1                       |
| protogen         | darkstorm2150/Protogen_x5.8                            |
| flux             | black-forest-labs/FLUX.1-dev                           |

---

## 🔧 Local Development

1. **Clone the repo**
```bash
git clone https://github.com/bisug/Ai-Image-Generator-API
cd Ai-Image-Generator-API
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set your Hugging Face token**
```bash
export HUGGINGFACE_TOKEN="your_token_here"
```

4. **Run locally**
```bash
uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
```

Then open:
```
http://127.0.0.1:8000/
```

---

## ⚠️ Notes
- Keep your `HUGGINGFACE_TOKEN` private — never expose it client-side.
- Hugging Face generation time depends on model complexity and queue.
- If a model returns a JSON error, this API will forward the error message.

🌟 **Made with ❤️ by [bisug](https://github.com/bisug)** • ⚡ **Supercharged by 🤖 ChatGPT**
