from __future__ import annotations

from pathlib import Path

import gensim.downloader as api


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    models_dir = base / "models" / "w2v_authors"
    models_dir.mkdir(parents=True, exist_ok=True)

    model_name = "word2vec-ruscorpora-300"
    dst = models_dir / "rucorpora.kv"

    kv = api.load(model_name)
    kv.save_word2vec_format(dst, binary=False)

    print("Saved:", dst)


if __name__ == "__main__":
    main()

