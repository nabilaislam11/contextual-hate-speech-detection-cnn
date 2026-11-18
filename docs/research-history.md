# Original CSE438 research development history

This chronology is based on the original group submission README records and repository file inventory. The final submitted PDF has now been inspected; earlier presentation and draft binaries have not yet been analyzed in full.

| Stage | Title in original README | Identified artifact | Verification |
| --- | --- | --- | --- |
| Submission 3 | Gender-Based Hate Comment Detection with NLP | Initial presentation | README and file listing verified |
| Submission 4 | Unlocking the Potential of NLP: Novel Approaches for Contextual Hate Speech Detection | First paper draft | README and file listing verified |
| Submission 5 | Unlocking the Potential of NLP: CNN based Approaches for Contextual Hate Speech Detection | Revised paper draft | README and file listing verified |
| Submission 6 | Unlocking the Potential of NLP: CNN based Approaches for Contextual Hate Speech Detection | Final paper and slides | Final paper read and preserved; slides not yet analyzed |

## Verified final paper details

The [unchanged final paper](../research/Final%20Paper.pdf) describes:

- 24,783 English tweets, with three classes: hate (1,430), offensive (19,190) and neither (4,163).
- Keras-based preprocessing, Word2Vec embeddings and a Kim-inspired CNN.
- A 50/30/20 train/validation/test split, Adam optimizer, batch size 64 and 10 epochs.
- Reported 91% accuracy, 0.90 recall and 0.90 F1, but **more than 80% of hate-class examples incorrectly classified**.
- Class imbalance, possible overfitting and the need for better minority-class evaluation.

These are **claims reported in the original PDF**, not independently reproduced results.

## Further archival work

1. Examine the original slide decks and first/second drafts for changes in methodology and results.
2. Recover any original training code, data processing scripts or trained weights, if they still exist.
3. Verify dataset provenance and sharing conditions before including data.
4. Confirm individual contribution descriptions with the collaborators.

The first two submissions in the other student's course archive were individual literature-review assignments on unrelated topics and are not part of this group research chronology.
