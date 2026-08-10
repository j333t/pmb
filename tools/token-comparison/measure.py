"""Token cost of PMB against prose and against plain bullets.

    pip install tiktoken
    python tools/token-comparison/measure.py

Two tests. The first compares naturally written formats and is what most
people mean by the question. The second holds the wording identical and
changes only the leading marker, which is the one that isolates the notation
from the writing style it encourages. The second test is the honest one.
"""

import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    import tiktoken
except ImportError:
    sys.exit("tiktoken is not installed.  pip install tiktoken")

from corpus import DOCS

ENCODINGS = [('cl100k', 'cl100k_base'), ('o200k', 'o200k_base')]
SYMBOL = re.compile(r'^(\s*)([+\-!?*~])(\s)')


def to_same_word_bullets(pmb):
    """Same words, same indentation, plain '-' in place of every symbol.

    Unmarked lines get a bullet too: a bullet list has no way to say
    "this line is neutral", which is precisely the information PMB adds.
    """
    out = []
    for line in pmb.split('\n'):
        if not line.strip():
            out.append(line)
        elif SYMBOL.match(line):
            out.append(SYMBOL.sub(r'\1-\3', line))
        else:
            indent = line[:len(line) - len(line.lstrip())]
            out.append(indent + '- ' + line.strip())
    return '\n'.join(out)


def pct(a, b):
    return 100.0 * (a - b) / b


def main():
    encs = [(name, tiktoken.get_encoding(e)) for name, e in ENCODINGS]

    print()
    print('=' * 72)
    print('TEST 1  Naturally written formats, claim sets held constant')
    print('=' * 72)
    for title, claims, prose, bullets, pmb in DOCS:
        print('\n%s  -- %d claims in each format' % (title, claims))
        for name, enc in encs:
            p, b, m = (len(enc.encode(t)) for t in (prose, bullets, pmb))
            print('  %-7s prose %4d | bullets %4d | pmb %4d   '
                  'vs prose %+5.1f%%   vs bullets %+5.1f%%'
                  % (name, p, b, m, pct(m, p), pct(m, b)))

    print('\n%s\nTOTALS' % ('-' * 72))
    for name, enc in encs:
        p = sum(len(enc.encode(d[2])) for d in DOCS)
        b = sum(len(enc.encode(d[3])) for d in DOCS)
        m = sum(len(enc.encode(d[4])) for d in DOCS)
        print('  %-7s prose %4d | bullets %4d | pmb %4d   '
              'vs prose %+5.1f%%   vs bullets %+5.1f%%'
              % (name, p, b, m, pct(m, p), pct(m, b)))

    print()
    print('=' * 72)
    print('TEST 2  Identical wording and indentation. Only the marker differs.')
    print('=' * 72)
    print()
    enc = dict(encs)['o200k']
    tot_pmb = tot_bul = 0
    for title, claims, _prose, _bullets, pmb in DOCS:
        same = to_same_word_bullets(pmb)
        m, b = len(enc.encode(pmb)), len(enc.encode(same))
        tot_pmb += m
        tot_bul += b
        print('  %-38s pmb %4d | bullets %4d | %+5.1f%%'
              % (title, m, b, pct(m, b)))
    print('  %-38s pmb %4d | bullets %4d | %+5.1f%%'
          % ('TOTAL', tot_pmb, tot_bul, pct(tot_pmb, tot_bul)))

    print()
    print('=' * 72)
    print('DECOMPOSITION (o200k)')
    print('=' * 72)
    pr = sum(len(enc.encode(d[2])) for d in DOCS)
    bu = sum(len(enc.encode(d[3])) for d in DOCS)
    pm = sum(len(enc.encode(d[4])) for d in DOCS)
    print('  flowing prose              %4d' % pr)
    print('  bullets, rewritten         %4d   %+5.1f%% vs prose'
          % (bu, pct(bu, pr)))
    print('  PMB                        %4d   %+5.1f%% vs prose, %+5.1f%% vs bullets'
          % (pm, pct(pm, pr), pct(pm, bu)))
    print('  PMB vs same-word bullets   %4d   %+5.1f%%   <- the notation alone'
          % (tot_bul, pct(tot_pmb, tot_bul)))
    print()
    print('  Most of the saving comes from writing atomic claims, which any')
    print('  bullet list also gets. The symbol itself is close to free: a')
    print('  marked line costs what a bullet costs, and a neutral line costs')
    print('  nothing. What PMB buys is not compression. It is the role of')
    print('  every line, recorded at a bullet list\'s price.')
    print()
    print('  Tokens per claim (o200k)')
    for title, claims, prose, bullets, pmb in DOCS:
        print('    %-38s prose %5.1f | bullets %5.1f | pmb %5.1f'
              % (title, len(enc.encode(prose)) / claims,
                 len(enc.encode(bullets)) / claims,
                 len(enc.encode(pmb)) / claims))
    print()


if __name__ == '__main__':
    main()
