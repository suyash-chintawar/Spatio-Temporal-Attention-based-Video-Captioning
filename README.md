# Spatio-Temporal-Attention-based-Video-Captioning
Video captioning is the automatic generation of short texts summarizing video clips. Attention mechanism is widely inspired by the human characteristics where we focus selectively on important regions of images and videos to gain insightful information. Spatial attention focuses on focusing on certain important regions in the video frames while the temporal attention refers to selectively focusing on certain frames to generate the captions.
Local, motion and global features are used to implement the spatio-temporal attention mechanisms. Spatial attention requires local features while all three types of feaatures are required for temporal attention. We implement the spatio-temporal attention using an encoder-decoder network model. RNNs such as LSTM and GRU have been used to encode the feature vectors of the video clips. On the other hand, LSTM and GRU have been alternatively used as language models to generate captions for the videos. Both models were evaluated on the MSVD dataset. The LSTM-based model obtained BLEU-4 score of 0.305, a METEOR score of 0.240 and CIDEr score of 0.339. The GRU-based model outperformed the LSTM-based model with a BLEU-4 score of 0.391, a METEOR score of 0.310 and a CIDEr score of 0.58.

## Files:
1) preprocess.py : File to convert raw training data to csv format.
2) data.csv : Contains all the annotated captions for every video ID in the MSVD dataset.
3) dict_youtube_mapping.pkl : Has all the mappings between file names and video IDs used for extracting local features.
4) extract_local_features.ipynb : Used for extracting local features. (global and motion features are extracted in the LSTM/GRU model notebooks).
5) LSTM_Model_Final.ipynb : LSTM based encoder-decoder model for video captioning.
5) GRU_Model_Final.ipynb : GRU based encoder-decoder model for video captioning.

## Contributors
- Naveen Shenoy
- Suyash Chintawar