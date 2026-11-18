# Research development history

The CSE438 group project developed through several research and presentation milestones:

| Stage | Research milestone | Document |
| --- | --- | --- |
| Submission 3 | Initial investigation of gender-based hate comment detection with NLP | Project presentation |
| Submission 4 | Expanded research direction toward contextual hate speech detection | First paper draft |
| Submission 5 | CNN-focused methodology and research paper development | Revised paper draft |
| Submission 6 | Final research paper and presentation | [Final paper](../research/Final%20Paper.pdf) |

## Final research focus

The completed paper, *Unlocking the Potential of NLP: CNN based Approaches for Contextual Hate Speech Detection*, investigates a CNN-based approach to classifying **24,783 English tweets** into hate speech, offensive language, and neither.

Its experimental setup describes **Word2Vec embeddings**, multi-filter CNN layers, **Adam optimization**, and a **50/30/20** training/validation/test split.

The paper reports **91% overall accuracy**, while its class-level analysis identifies significant difficulty detecting hate speech in the minority class. This finding highlights the importance of class-sensitive evaluation and balanced training data.

## Research directions

The paper proposes further work on classification error analysis, dataset diversity, parameter optimization, and improved discrimination between hate speech and offensive language.
