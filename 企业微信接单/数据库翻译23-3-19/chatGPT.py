import re
import openai
import pandas as pd

def chatgpt(question):
    openai.api_key = "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"
    model_engine = "text-davinci-003"
    prompt = "简短的翻译这个数据库字段:" + "{}".format(question)

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=15,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    # 子输出中文
    message = re.findall(r'[\u4e00-\u9fa5]', message)
    return "".join(message)


def fy():
    result_list = []
    list1 = pd.read_excel('fy.xlsx', header=None)[0]
    list1 = list1.tolist()
    a = 0
    for i in list1:
        a = a+1
        result = chatgpt(i)
        result_list.append(result)
        print('{} : {} : {}'.format(a, i, result))
    try:
        df1 = pd.DataFrame(list1)
        df1.to_excel('fy-chatgpt.xlsx')
    except:
        df1 = pd.DataFrame(list1)
        df1.to_excel('fy-chatgpt.xlsx')
        print('出错：'.format(i))


if __name__ == '__main__':
    fy()
