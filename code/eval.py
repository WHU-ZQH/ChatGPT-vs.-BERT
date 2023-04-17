import openai
import backoff
from datasets import load_dataset, load_metric
import argparse
import pandas as pd

# hyper-parameters
TASK = "sst2"
MODEL = "gpt-3.5-turbo"
NUMS = 10
RAND_SEED = 233

# dataset define
unsampled_dataset = load_dataset("glue", TASK, split="validation")
dateset = unsampled_dataset.select(range(NUMS))

# api key
API_KEY = "sk-..."


def mapping(answer, task=TASK):
    answer_map = {"sst2": {"negative": 0, "Negative": 0, "positive": 1, "Positive": 1, "negative.": 0, "Negative.": 0,
                           "positive.": 1, "Positive.": 1}}
    return answer_map[task].get(answer, 2)


def prompt(sentence, task):
    if task == "sst2":
        return "\"" + sentence + "\" the sentiment is:(positive/negative)"
    # if task == any


@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def query(question):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": question}],
        temperature=0.5
    )
    return response.choices[0]['message']['content']


def evaluate():
    # eval
    data = pd.DataFrame(columns=['sentence', 'label', 'prediction', 'response'])
    metric = load_metric("glue", TASK)
    for i in range(NUMS):
        print(i)
        question = prompt(dateset[i]['sentence'], TASK)
        answer = dateset[i]['label']
        response = query(question)
        predict = mapping(response, TASK)
        metric.add_batch(predictions=[predict], references=[answer])
        data.loc[i] = [dateset[i]['sentence'], answer, predict, response]
    print(metric.compute())
    end_time = pd.Timestamp.now().strftime("%m%d%H%M")
    data.to_csv("results/{task_name}_result_{end_time}.csv".format(task_name=TASK, end_time=end_time), index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', type=str, default=TASK)
    parser.add_argument('--model', type=str, default=MODEL)
    parser.add_argument('--nums', type=int, default=NUMS)
    parser.add_argument('--seed', type=int, default=RAND_SEED)
    parser.add_argument('--api_key', type=str)
    args = parser.parse_args()
    TASK = args.task
    MODEL = args.model
    NUMS = args.nums
    RAND_SEED = args.seed
    openai.api_key = args.api_key
    evaluate()
