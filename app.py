from chat import chat
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return FileResponse('index.html')


@app.post('/')
async def api(request: Request):
    """
    api
    :param request: 请求
    :return: 响应
    """
    my_list = await request.json()
    print('请求数据：')
    print(my_list)
    print('\n')
    history = []
    for i in range(0, len(my_list) - 2, 2):
        t = (my_list[i], my_list[i+1])
        history.append(t)
    print('历史：')
    print(history)
    print('\n')
    req = my_list[-2]
    print('提示词：')
    print(req)
    print('\n')
    response, history = chat(
        req=req,
        history=history)
    return response


if __name__ == '__main__':
    uvicorn.run(app='app:app', port=80)
