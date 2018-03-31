#!/usr/bin/env python3
import pydub
import argparse

import sys
import glob
import os
import os.path
import shutil

import random


NOISE_ROOT = './bg_noise'

noise_files = []


def load_noise():
    for fl in glob.glob(NOISE_ROOT + '/**/*.wav'):
        noise_files.append(fl)


def main(in_dir, out_dir):
    load_noise()

    for subdir, dirs, files in os.walk(in_dir):
        new_dir = subdir.replace(in_dir, out_dir)
        os.makedirs(new_dir, exist_ok=True)

        for fl in files:
            cur_file_path = os.path.join(subdir, fl)
            new_file_path = os.path.join(new_dir, fl)
            if new_file_path.endswith('.flac'):
                new_file_path = new_file_path[:-len('.flac')] + '.wav'

            if fl.endswith('.wav') or fl.endswith('.flac'):
                audio_data = pydub.AudioSegment.from_file(cur_file_path)

                rnd_noise = random.choice(noise_files)
                noise_data = pydub.AudioSegment.from_file(rnd_noise)

                noised_audio = audio_data.overlay(noise_data, loop=True)

                noised_audio.export(new_file_path, format='wav')
            else:
                shutil.copyfile(cur_file_path, new_file_path)
            

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-in_corpus_path', help='Path to the original audio corpus to corrupt ',
                        required=True,
                        dest='in_corpus_path')
    parser.add_argument('-out_corpus_path', help='Output path to the corrupted corpus ',
                        required=True,
                        dest='out_corpus_path')
    args = parser.parse_args()
    sys.exit(main(args.in_corpus_path, args.out_corpus_path))
