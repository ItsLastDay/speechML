## Requires
Python 3.2+

## Adding background noise to audio data
0. Install `pydub`:  
  `pip3 install pydub`
1. Change `NOISE_ROOT` in `add_bg_noise.py` to path with your noise files.
2. Run this to add noise to sample data from `audio` folder:  
  `python3 ./add_bg_noise.py -in_corpus_path ./audio -out_corpus_path ./audio_corrupted`
3. `-in_corpus_path` specifies input folder. All `.wav` and `.flac` files from it will be copied to `-out_corpus_path` with noise added. All other files will be copied as is.
