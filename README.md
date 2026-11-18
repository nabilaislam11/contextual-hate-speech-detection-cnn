# Contextual Hate Speech Detection Using CNNs

**Original paper:** *Unlocking the Potential of NLP: CNN based Approaches for Contextual Hate Speech Detection*

Academic collaborative research examining convolutional neural networks (CNNs) for classifying English-language tweets as **hate speech**, **offensive language**, or **neither**.

> **Research status:** This repository preserves the original final group paper and documents its **reported** experimental setup and findings. The original training code, dataset copy, trained weights, and a reproducible environment have not been recovered or verified. Reported results have not been independently reproduced.

## Research overview

The study applies natural language processing and a CNN-based sentence classification approach to the **CrowdFlower Hate Speech Identification** dataset of **24,783 English tweets**.

| Label | Samples | Share |
| --- | ---: | ---: |
| Hate | 1,430 | 5.8% |
| Offensive | 19,190 | 77.4% |
| Neither | 4,163 | 16.8% |
| **Total** | **24,783** | **100%** |

The class distribution is highly imbalanced. This is critical to interpreting the model's results.

## Methodology reported in the paper

- **Text processing:** character cleaning, lowercasing, stemming and tokenization using Python/Keras tooling.
- **Split:** training **50%**, validation **30%**, test **20%**; the paper does not report cross-validation.
- **Embeddings:** pretrained **300-dimensional Word2Vec** vectors; the paper describes an input tensor shape of `(None, 100, 300)`.
- **CNN:** sentence-classification design inspired by **Kim (2014)**, with convolution filter sizes **3, 4 and 5**, **100 filters per size**, max pooling and softmax classification.
- **Training:** Adam optimizer, batch size **64**, **10 epochs**. The paper discusses a later learning-rate adjustment to **1e-4**.

These settings are transcribed from the original report, **not** from independently inspected source code. The paper does not provide a complete reproducible implementation specification.

## Reported findings and limitations

| Reported aggregate measure | Value |
| --- | ---: |
| Accuracy | **91%** |
| Recall | **0.90** |
| F1-score | **0.90** |
| Loss | **36%** (as described in the paper) |

**Critical limitation:** Despite the reported 91% aggregate accuracy, the paper states that **more than 80% of tweets in the hate class were classified incorrectly**. The class imbalance and bias toward predicting offensive language substantially limit the model's usefulness for detecting the minority hate-speech class. Aggregate metrics must **not** be presented as evidence of strong hate-class detection.

The paper contains training/validation loss and accuracy plots and a confusion matrix (pages 3–4). The precise evaluation population for each aggregate metric is not fully specified; values are therefore presented as **paper-reported**, not verified test-set scores.

Further limitations include a relatively small minority class, possible overfitting, absence of cross-validation and unavailable original runnable code. The paper also discusses ethical considerations such as classification bias and freedom of expression.

## Original paper and documentation

- [Read the unchanged final submitted paper (PDF)](research/Final%20Paper.pdf)
- [Research development history](docs/research-history.md)
- [Authorship and contributions](docs/contributions.md)
- [Original material inventory](docs/original-materials.md)

## Paper authorship

The final PDF lists the following **seven authors**, in this order:

1. Nabila Islam Borno
2. Ashfiqun Ahmed Miftah
3. Atikur Rahman
4. Gazi Asif Imtiaz
5. Md Sabbir Hossain
6. Mehnaz Ara Fazal
7. Annajiat Alim Rasel

The archived course submission READMEs identify the first four as **Group 4 members**. This distinction does not establish the individual responsibilities of any author; see [contributions](docs/contributions.md).

## Provenance

The original CSE438 coursework archive documents a progression from an initial gender-based hate comment detection proposal (submission 3), through a broader NLP paper draft (submission 4), to a CNN-focused draft and final submission (submissions 5–6).

This repository was organized later to preserve and explain that academic work. **No original software implementation is claimed to be present.** Any future reproduction or extension will be labeled separately and will not be described as the original submitted code.

## Reuse

No software or research-material license is asserted here. The PDF retains its original authorship and contents. Check permissions and third-party rights before reusing the paper, dataset, figures or any future recovered materials.
