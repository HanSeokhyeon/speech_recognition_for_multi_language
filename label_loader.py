"""
Copyright 2019-present NAVER Corp.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

#-*- coding: utf-8 -*-
import json


def load_label(label_path, language):
    with open(label_path, 'r') as f:
        if language == 'korean':
            char2index = dict()  # [ch] = id
            index2char = dict()  # [id] = ch

            for no, line in enumerate(f):
                if line[0] == '#':
                    continue

                index, char, freq = line.strip().split('\t')
                char = char.strip()
                if len(char) == 0:
                    char = ' '

                char2index[char] = int(index)
                index2char[int(index)] = char
        else:
            char2index63 = json.load(f)
            index2char = {char2index63[key]: key for key in char2index63}
            char2index = {index2char[key]: key for key in index2char}

    return char2index, index2char
