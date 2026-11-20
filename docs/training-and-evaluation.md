# CNN Training and Evaluation

## Input format

The pipeline accepts a CSV containing `tweet` and `class` (CrowdFlower-style column names), or `text` and `label`. An optional `context` column is joined to the input text with markers. The public dataset's class labels represent hate speech, offensive language and neither.

## Experimental workflow

1. Read and prepare labeled tweets.
2. Stratify into 50% training, 30% validation and 20% test partitions.
3. Fit a tokenizer on training text and pad sequences to 100 tokens.
4. Train a CNN with a 300-dimensional trainable embedding, filter widths 3, 4 and 5, global max pooling, dropout and a softmax output.
5. Export per-class metrics, a confusion matrix, the model, tokenizer, label mapping and configuration.

## Commands

```bash
pip install -r requirements.txt
python src/train.py --csv /path/to/tweets.csv --epochs 10 --output artifacts
python src/predict.py --text "Example tweet"
```

The accompanying [research paper](../research/Final%20Paper.pdf) describes experiments using pretrained Word2Vec features. The runnable companion script uses its own trainable embeddings and generates evaluation files for each execution.
