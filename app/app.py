from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from datetime import datetime
from openai import OpenAI

app = FastAPI()

conversation = []

with open('app/sys_template.txt', 'r',) as f:
    Sys_prompt = f.read()
    # Sys_prompt = Sys_prompt.replace('\n','')

with open('styles.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

def OAI(Q: str):
    with open('misc/api_key.txt', 'r') as f:
        APIKEY = f.read()
    client = OpenAI(api_key= APIKEY)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
            messages= [
                {"role": "system", "content": f"{Sys_prompt}"},
                {"role": "user", "content": f"{Q}"} ],
            max_tokens=1500,
            n=1,
            stop=None,
            temperature=0.5
    )
    a = response.choices[0].message.content
    # print(a)
    return a



def log_question(question):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conversation.append({"timestamp": timestamp, "question": question, "response": None})
    with open("questions_log.txt", "a") as file:
        file.write(f"{timestamp}: {question}\n")

def log_response(response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conversation[-1]["response"] = response
    with open("questions_log.txt", "a") as file:
        file.write(f"{timestamp}: {response}\n")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return html_content
    

@app.post("/store_input/")
async def store_input(input: str = Form(...)):
    log_question(input) if len(conversation) % 2 == 0 else log_response(input)
    print(input)
    resp = OAI(input)
    resp = resp.replace('\n', '<br>')
    return {"message": f'{resp}'}


