#!/usr/bin/env python
# coding=utf-8
# author: jige003
from collections import OrderedDict
from pprint import pformat
from argparse import RawTextHelpFormatter, ArgumentParser

import os

ELEMENTS = ['☰', '☱', '☲', '☳', '☴', '☵', '☶', '☷', '爻', '☯']

def init_args():
    parser = ArgumentParser(
        description="""
        以八卦元素混淆代码为一句话

        乾☰ 坤☷ 震☳ 艮☶  离☲ 坎☵ 兑☱ 巽☴
        
        记诵口诀:

        乾三连，坤六断；震仰盂，艮覆碗。
        离中虚，坎中满；兑上缺，巽下断。

        """, 
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument('-f', '--file', required=True, help='ob files')
    return parser.parse_args()

def ob(cts):
    d = OrderedDict(enumerate(ELEMENTS))
    rd = OrderedDict(zip(d.values(), d.keys()))
    return ('#!/usr/bin/env python\n# coding=utf-8\nfrom collections import OrderedDict\n'
            'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
            '"{}".split("  ")])))'.format(pformat(rd), '  '.join(
            ' '.join(d[int(i)] for i in str(ord(c))) for c in cts)))

def get_ob_filename(x):
    fname, ext = os.path.splitext(x)   
    return "{}_ob{}".format(fname, ext)

def main():
    args = init_args()
    ofname = get_ob_filename(args.file)
    with open(args.file) as f, open(ofname, 'w') as ff:
        ff.write(ob(f.read()))

if __name__ == '__main__':
    main()
