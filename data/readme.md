# Data Format
Each instance consists of 9 items:
- **id**: the id of this instance in the original dev set.
- **sentence(s)**: the input sentence(s) of this instance. For the sentence pair tasks, taking MNLI as an example, we refer to the premise as "sentence1" and the hypothesis as "sentence2".
- **sentence4ChatGPT**: we fill the prompt template with the input sentence(s) and use it to ask ChatGPT.
- **label**: label of this instance
- **pred_bert-base**: prediction made by BERT-base
- **pred_bert-large**: prediction made by BERT-large
- **pred_roberta-base**: prediction made by RoBERTa-base
- **pred_roberta-large**: prediction made by RoBERTa-large
- **pred_ChatGPT**: prediction made by ChatGPT

Additionally, we also provide the evaluation results measured with the corresponding metrics for each task.
