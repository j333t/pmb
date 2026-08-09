#!/usr/bin/env python3
"""Keep the prompt text embedded in index.html identical to prompts/*.txt.

The landing page copies prompts to the clipboard straight out of the DOM, so
that copying works however the page was opened — no fetch, no network. The
cost is that every prompt lives in two places. This script is what stops them
drifting apart.

    python tools/embed-prompts.py           rewrite index.html from prompts/
    python tools/embed-prompts.py --check   report drift, exit 1 if any

Each prompts/<name>.txt maps to a <script type="text/plain" id="prompt-<name>">
block in index.html. Script elements parse as raw text, so the prompt is
embedded verbatim — no escaping, and textContent hands it back unchanged.
"""

import io
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / "index.html"
PROMPTS = ROOT / "prompts"


def read(path):
    return io.open(path, encoding="utf-8").read()


def block_pattern(key):
    return re.compile(
        r'(<script type="text/plain" id="prompt-%s">)(.*?)(</script>)' % re.escape(key),
        re.S,
    )


def main():
    check_only = "--check" in sys.argv[1:]

    page = read(PAGE)
    original = page
    stale = []

    sources = sorted(PROMPTS.glob("*.txt"))
    if not sources:
        sys.exit("no prompts found in %s" % PROMPTS)

    for path in sources:
        key = path.stem
        text = read(path).strip()

        # A literal </script anywhere in the text would end the block early.
        if "</script" in text.lower():
            sys.exit("%s contains a closing script tag and cannot be embedded" % path)

        pattern = block_pattern(key)
        match = pattern.search(page)
        if not match:
            print("skip   prompts/%s.txt — no prompt-%s block in index.html"
                  % (key, key))
            continue

        if match.group(2) == text:
            print("ok     prompts/%s.txt" % key)
            continue

        stale.append(key)
        page = pattern.sub(lambda m: m.group(1) + text + m.group(3), page, count=1)

    if not stale:
        print("\nindex.html is in sync.")
        return 0

    if check_only:
        print("\ndrifted: %s" % ", ".join(stale))
        print("run: python tools/embed-prompts.py")
        return 1

    if page != original:
        io.open(PAGE, "w", encoding="utf-8", newline="\n").write(page)
    print("\nre-embedded: %s" % ", ".join(stale))
    return 0


if __name__ == "__main__":
    sys.exit(main())
