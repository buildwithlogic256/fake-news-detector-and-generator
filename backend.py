from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, AutoTokenizer, AutoModelForSequenceClassification
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for local frontend use
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

gpt2_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
gpt2_model = GPT2LMHeadModel.from_pretrained("gpt2").to(device)

bert_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
bert_model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2).to(device)

class TextInput(BaseModel):
    text: str

@app.post("/generate")
def generate_fake_news(data: TextInput):
    inputs = gpt2_tokenizer.encode(data.text, return_tensors="pt").to(device)
    outputs = gpt2_model.generate(inputs, max_length=200, num_return_sequences=1,
                                  no_repeat_ngram_size=2, do_sample=True, temperature=0.7,
                                  top_k=50, top_p=0.95, early_stopping=True)
    generated_text = gpt2_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"generated_text": generated_text}

@app.post("/detect")
def detect_news(data: TextInput):
    inputs = bert_tokenizer(data.text, return_tensors="pt", truncation=True, padding=True).to(device)
    with torch.no_grad():
        outputs = bert_model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    confidence = torch.softmax(logits, dim=1)[0][predicted_class].item()
    label = "Fake News" if predicted_class == 0 else "Real News"
    return {"label": label, "confidence": confidence}
