"""Gera index.html a partir de src/template.html.

Injeta o d3 (vendor/) e os dados do grafo de src/rastros-da-cibernetica.html,
para que index.html seja um arquivo único que roda offline.
Uso: python3 build.py
"""
from pathlib import Path

root = Path(__file__).parent
template = (root / "src/template.html").read_text(encoding="utf-8")
rastros = (root / "src/rastros-da-cibernetica.html").read_text(encoding="utf-8")
d3 = (root / "vendor/d3-7.8.5.min.js").read_text(encoding="utf-8")

data = rastros[rastros.index("const TYPES="):rastros.index("const byId=")]
assert "</script" not in d3.lower()
for marker in ("/*RASTROS_DATA*/", "/*D3_LIB*/"):
    assert template.count(marker) == 1, marker

out = template.replace("/*RASTROS_DATA*/", data).replace("/*D3_LIB*/", d3)
(root / "index.html").write_text(out, encoding="utf-8")
print(f"index.html: {len(out):,} bytes")
