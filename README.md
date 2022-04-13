# Spatio-Temporal-Attention-based-Video-Captioning

Files:
1) preprocess.py : File to convert raw training data to csv format.
2) data.csv : Contains all the annotated captions for every video ID in the MSVD dataset.
3) dict_youtube_mapping.pkl : Has all the mappings between file names and video IDs used for extracting local features.
4) extract_local_features.ipynb : Used for extracting local features. (global and motion features are extracted in the LSTM/GRU model notebooks).
5) LSTM_Model_Final.ipynb : LSTM based encoder-decoder model for video captioning.
5) GRU_Model_Final.ipynb : GRU based encoder-decoder model for video captioning.