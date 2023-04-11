# ChatGPT vs. BERT
<b>Can ChatGPT Understand Too? A Comparative  Study on ChatGPT and Fine-tuned BERT</b>. ([Full report, v2](https://arxiv.org/pdf/2302.10198v2.pdf)) ([v1](https://arxiv.org/pdf/2302.10198v1.pdf))


This repository releases the evaluated sets and the outputs predicted by BERT-style models (BERT-Base/Large and RoBERTa-Base/Large) and [ChatGPT](https://chat.openai.com/chat), for the replication of the study.

## Data and Predictions

For each task of the [GLUE](https://gluebenchmark.com/tasks) benchmark, we randomly sample 25 instances for each class from the dev set for evaluation, except for STS-B, where we randomly sample 50 instances from a uniform distribution. The data and its corresponding predictions can be obtained in "[./data](./data/)".

The task statistics and prompts are shown as follows:
<div align="center">
    <img width="80%" alt="image" src="https://github.com/WHU-ZQH/ChatGPT-vs.-BERT/blob/main/sources/task.png">
</div>

Additionally, we also provide the script for sampling and preprocessing the data in "[get_data.py](./get_data.py)". Taking the CoLA task as an example, you can resample k-instances by the following command:
```
python3 get_data.py --num 25 --task cola --model_pred BERT_pred_path --save_path save_data_path
```

## Results and Findings

1. Overall, ChatGPT attains a comparable understanding ability compared with fine-tuned BERT-base, but still underperforms the other powerful BERT-style models, such as RoBERTa-large, by a clear margin.

    > Overall results on GLUE:
<div align="center">
    <img width="80%" alt="image" src="https://github.com/WHU-ZQH/ChatGPT-vs.-BERT/blob/main/sources/main.png">
</div>


2. ChatGPT falls short in handling paraphrase and similarity tasks. Specifically, ChatGPT performs poorly in negative paraphrase and neutral similarity samples, respectively.

    > Per-class accuracy on paraphrase task (Left) and analysis on similarity task (Right):
<div align="center">
    <img width="85%" alt="image" src="https://github.com/WHU-ZQH/ChatGPT-vs.-BERT/blob/main/sources/mrpc.png">
</div>


3. ChatGPT outperforms all BERT-style models on inference tasks by a large margin, indicating its impressive reasoning ability.

    > Per-class accuracy on inference tasks:
<div align="center">
    <img width="70%" alt="image" src="https://github.com/WHU-ZQH/ChatGPT-vs.-BERT/blob/main/sources/nli.png">
</div>


4. Despite its good performance on inference tasks, ChatGPT may generate some contradictory or unreasonable responses, which would be its potential limitations.

    > Case of inference tasks:

<div align="center">
    <img width="70%" alt="image" src="https://github.com/WHU-ZQH/ChatGPT-vs.-BERT/blob/main/sources/case_nli.png">
</div>


## More results with advanced prompting techniques  (update on 2 Mar. 2023)

In addition to analyzing the ChatGPT itself, we also explore the complementarity of ChatGPT and some advanced prompting strategies, i.e., the standard few-shot prompting, manual few-shot chain-of-thought (CoT) prompting and zero-shot CoT prompting. 

 >Some input/output examples:

<div align="center">
    <img width="80%" alt="image" src="https://github.com/WHU-ZQH/ChatGPT-vs.-BERT/blob/main/sources/prompting.png">
</div>


 >The overall results of ChatGPT equipped with advanced prompting strategies:

<div align="center">
    <img width="80%" alt="image" src="https://github.com/WHU-ZQH/ChatGPT-vs.-BERT/blob/main/sources/few-shot-result.png">
</div>


Based on these results, we can further find that:
- ChatGPT benefits from all these prompting strategies, among which the manual-CoT brings the most performance improvements. 
- The performance of in-context learning is unstable and relatively sensitive to the provided examples, especially in the 1-shot scenario. 

	> More detailed analysis on the 1-shot prompting:
<div align="center">
    <img width="40%" alt="image" src="https://github.com/WHU-ZQH/ChatGPT-vs.-BERT/blob/main/sources/1-shot-result.png">
</div>


- With the help of few-shot CoT, ChatGPT achieves impressive performance improvement (up to 7.5% average score), but still fails to beat the current SOTA models, especially on some NLU tasks. 

Please refer to our full [report](https://arxiv.org/pdf/2302.10198v2.pdf) for more details.

## TODO 
More results of ChatGPT equipped with the following strategies:  
- [x] Zero-shot Chain-of-Thought <i> (before 24 Feb. 2023) </i>
- [x] Few-shot Chain-of-Thought <i> (before 24 Feb. 2023) </i>
- [x] Standard few-shot In-Context Learning <i> (before 24 Feb. 2023) </i>

Add the few-shot results and analyses in our report:
- [x] update our report and release the v2 version <i> (before 28 Feb. 2023) </i>

## Citation
If you find this work helpful, please consider citing as follows:  

```ruby
@article{zhong2023chat,
  title={Can ChatGPT Understand Too? A Comparative  Study on ChatGPT and Fine-tuned BERT},
  author={Zhong, Qihuang and Ding, Liang and Liu, Juhua and Du, Bo and Tao, Dacheng},
  journal={arXiv preprint},
  url={https://arxiv.org/abs/2302.10198},
  year={2023}
}
```
