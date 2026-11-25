#!/usr/bin/env python3
"""Build the downloadable CV from the website's cv.qmd using Quarto/Typst."""

from pathlib import Path
import os
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://inikkim.github.io/ikim124.github.io/"


def main():
    quarto = os.environ.get("QUARTO_BIN") or shutil.which("quarto")
    rstudio_quarto = Path("/Applications/RStudio.app/Contents/Resources/app/quarto/bin/quarto")
    if not quarto and rstudio_quarto.is_file():
        quarto = str(rstudio_quarto)
    if not quarto:
        raise SystemExit("Install Quarto, or set QUARTO_BIN to its executable path.")

    source = (ROOT / "cv.qmd").read_text()
    body = re.sub(r"\A---\n.*?\n---\n", "", source, count=1, flags=re.S)
    body = re.sub(r" &nbsp; \| &nbsp; \[Download PDF\]\([^)]*\)", "", body)
    body = re.sub(r"^---\s*$", "", body, flags=re.M)
    # Conference entries are secondary to papers; limit smaller text to this section.
    body = body.replace(
        "## Conference Presentations",
        "```{=typst}\n#pagebreak()\n#block[\n#set text(size: 8.5pt)\n```\n\n## Conference Presentations",
        1,
    )
    body = body.replace("## Teaching Experience", "```{=typst}\n]\n```\n\n## Teaching Experience", 1)
    # Relative web downloads should remain useful in a standalone PDF.
    body = re.sub(r"\]\((pdfs/[^)]+)\)", lambda m: "](" + SITE + m[1] + ")", body)
    header = '''---
title: "Inik Kim"
subtitle: "Curriculum Vitae"
format:
  typst:
    papersize: us-letter
    fontsize: 9.5pt
    margin:
      x: 0.65in
      y: 0.55in
    number-sections: false
---

[ikim124@ucr.edu](mailto:ikim124@ucr.edu) · [Personal website](https://inikkim.github.io/ikim124.github.io/)

'''
    with tempfile.TemporaryDirectory(prefix="inik-cv-") as directory:
        temporary = Path(directory)
        qmd = temporary / "cv.qmd"
        qmd.write_text(header + body)
        subprocess.run([quarto, "render", str(qmd), "--to", "typst"], check=True, cwd=temporary)
        target = ROOT / "Kim_Inik_cv_26.pdf"
        shutil.copyfile(temporary / "cv.pdf", target)
        print(f"Updated {target}")


if __name__ == "__main__":
    main()
