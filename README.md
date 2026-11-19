# Contextual Hate Speech Detection Using CNNs

**Research paper:** *Unlocking the Potential of NLP: CNN based Approaches for Contextual Hate Speech Detection*

An academic research project exploring **natural language processing (NLP)** and **convolutional neural networks (CNNs)** for three-class hate speech detection in social media text.

## Research at a glance

| Focus | Details |
| --- | --- |
| Task | Classify English tweets as hate speech, offensive language, or neither |
| Dataset | CrowdFlower Hate Speech Identification dataset — 24,783 tweets |
| Approach | CNN-based sentence classification inspired by Kim (2014) |
| Techniques | Text preprocessing, Word2Vec embeddings, multi-filter convolutions, max pooling |
| Reported overall accuracy | **91%** |
| Key research challenge | Class imbalance and reliable detection of minority-class hate speech |

[**Read the research paper (PDF)**](research/Final%20Paper.pdf)

## Research objective

Hate speech detection is challenging because language depends on context and because offensive language does not always constitute hate speech. This study investigates how CNN-based text classification can distinguish three categories of tweets and evaluates the strengths and limitations of the approach.

## Dataset

The study uses **24,783 English tweets** from the CrowdFlower Hate Speech Identification dataset.

| Class | Number of tweets | Percentage |
| --- | ---: | ---: |
| Hate speech | 1,430 | 5.8% |
| Offensive language | 19,190 | 77.4% |
| Neither | 4,163 | 16.8% |
| **Total** | **24,783** | **100%** |

The pronounced class imbalance is an important factor in interpreting classification performance.

## Methodology

### 1. Text preprocessing

The research describes text cleaning, lowercasing, stemming, and tokenization using Python and Keras tooling.

### 2. Word representations

Tweets are represented with **300-dimensional pretrained Word2Vec embeddings**. The paper describes an embedding input tensor with shape `(None, 100, 300)`.

### 3. CNN architecture

The model follows a sentence-classification approach inspired by **Kim (2014)**, using:

- Convolutional filters of sizes **3, 4, and 5**, with **100 filters per size**
- Max-pooling operations to capture salient features
- A softmax output layer for three-class prediction

### 4. Experimental configuration

| Parameter | Configuration described in the paper |
| --- | --- |
| Training / validation / test | 50% / 30% / 20% |
| Optimizer | Adam |
| Batch size | 64 |
| Epochs | 10 |
| Learning-rate adjustment discussed | `1e-4` |
| Evaluation | Accuracy, recall, F1-score, confusion matrix, loss/accuracy curves |

## Results and discussion

The final paper reports the following aggregate results:

| Metric | Reported result |
| --- | ---: |
| Accuracy | **91%** |
| Recall | **0.90** |
| F1-score | **0.90** |
| Loss | **36%** |

The research also highlights a significant challenge: **more than 80% of hate-class tweets were classified incorrectly**, despite the strong overall accuracy. This illustrates how class imbalance can obscure weak performance on a minority class and why class-specific evaluation is essential for responsible content moderation.

The paper includes accuracy/loss plots and a confusion matrix and discusses overfitting, dataset size, and ethical concerns around automated moderation.

## Research significance

This project examines both the potential and the practical challenges of CNN-based NLP for content classification. Its findings motivate further investigation into class imbalance, model tuning, error analysis, and fair evaluation of hate speech detection systems.

## Authors

The final paper credits:

1. Nabila Islam Borno
2. Ashfiqun Ahmed Miftah
3. Atikur Rahman
4. Gazi Asif Imtiaz
5. Md Sabbir Hossain
6. Mehnaz Ara Fazal
7. Annajiat Alim Rasel

See [authorship and contributions](docs/contributions.md) for the distinction between paper authors and the course project group.

## Related implementation

A [CNN training and prediction implementation](https://github.com/nabilaislam11/nabila-portfolio/tree/main/projects/05-contextual-hate-speech-cnn) explores the text classification workflow in Python and TensorFlow. The academic paper and its reported findings remain documented in this research repository.

## Research materials

- [Final research paper](research/Final%20Paper.pdf)
- [Research development history](docs/research-history.md)
- [Authorship and contributions](docs/contributions.md)
- [Research materials](docs/original-materials.md)

## Future directions

The paper identifies error analysis, stronger minority-class detection, improved data balance, and further CNN optimization as areas for future work.
