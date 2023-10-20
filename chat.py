import torch.cuda
from transformers import AutoTokenizer, AutoModel


def chat(req, history=None):
    """
    chat
    :param req: 提示词
    :param history: 历史
    :return: 生成文本，历史
    """
    try:
        print('开始加载模型……\n')
        tokenizer = AutoTokenizer.from_pretrained("model/chatglm2-6b-int4", trust_remote_code=True)
        if torch.cuda.is_available():
            model = AutoModel.from_pretrained("model/chatglm2-6b-int4", trust_remote_code=True).half().cuda()
        else:
            model = AutoModel.from_pretrained("model/chatglm2-6b-int4", trust_remote_code=True).half()
        print('\n所处设备：')
        print(model.device)
        print('\n')
        model = model.eval()
        print('模型加载完成，正在生成文本……\n')
        response, history = model.chat(tokenizer, req, history=history)
        print('生成文本：')
        print(response)
        print('\n')
        return response, history
    except Exception as e:
        print(e)
        return e, []
