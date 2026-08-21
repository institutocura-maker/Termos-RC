#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera apostila.md no padrão TOP a partir do ART-2025-08-01 (Fornos Replicadores).
Transforma o texto do curador em 3 PARTES com subseções, citações em bloco,
notas do editor e glossário local A–D."""
import re
from pathlib import Path

BASE = Path("/home/user/rc-terminologia/apostilas/2025-08-01_fornos_replicadores")
ORIG = BASE / "original.txt"
SAIDA = BASE / "apostila.md"

CABECALHO = """@titulo: Fornos Replicadores – Awayen, Awaylengan e Awaymaion
@autor: Edson Cella Mendes (material do curador — baseado estritamente em livros e palestras de Jan Val Ellam)
@data: 01/08/2025
@local: —
@subtitulo: Apostila de estudo — Texto integral do curador (ART-2025-08-01), organizado em 3 PARTES com remissões à Base Terminológica RC.
@nota_editor: Esta apostila é a versão "padrão apostila" do material de curadoria **ART-2025-08-01** — "Fornos Replicadores: Awayen de Brahma; Awaylengan de Shiva e Awaymaion de Vishnu", de **Edson Cella Mendes (o curador)**, baseado estritamente em livros e palestras de Jan Val Ellam. **Natureza do material:** sistematização própria do curador — NÃO é obra primária do autor; tudo permanece "leitura de Ellam via sistematização do curador". O texto foi preservado integralmente, organizado em **3 PARTES** (uma por forno), com subseções por prefácio/capítulos/epílogo, citações em bloco, notas do editor e glossário local A–D. **Utilidade para a KB (ciclo ART-2025-08-01, Devolutiva O-1 a O-7 aprovadas):** resolveu os STT históricos "[REVISAR] forno de Alamaior" (= Awaymaion) e "[REVISAR] projeto tal" (= Projeto Talm); criou o nó-guarda-chuva **RC-771 (Fornos Replicadores)** — autorização excepcional do curador; corrigiu RC-500 (Almaior/Alamaior → remissão a RC-499); promoveu RC-499; materializou RC-132 (Val Tam); ampliou 10 fichas; cadastrou B083 ("Awayen – A Central de Realidades" — anunciada; [REVISAR grafia 'Awayem']). Alegações teológicas, científicas e históricas são **leitura da RC via curador, não consenso validado** — em especial: a "doença do Criador"/CFDP; as datas (Shiva ~12,17 bi anos; Vishnu ~4,1 bi anos; cérebro bilatério ~4 bi anos) [REVISAR — conferir B050]; a taxonomia radiata/bilatério (leitura da RC, não neurociência).
"""

GLOSSARIO = """## GLOSSÁRIO LOCAL

### A. Termos e grafias canônicas usados nesta apostila

| Termo | Remissão na Base | Observação |
|---|---|---|
| Fornos Replicadores | RC-771 | nó-guarda-chuva criado neste ciclo (autorização excepcional O-3) |
| Awayen (forno de Brahma/Javé) | RC-771 (sub-ente) | Central de Realidades; ovóide; Val Tam acoplada |
| Awaylengan (forno de Shiva) | RC-771 (sub-ente) | primeiro forno; mais ativo; demol/demobiol |
| Awaymaion (forno de Vishnu) | RC-499 | promovido ⚪→🟡; biodemo; Olm |
| Almaior / Alamaior | RC-500 | erro histórico de STT → remissão a RC-499 |
| Projeto Talm | RC-091 | programa dos três fornos (Nidana→Saccidanandhagana) |
| Val Tam | RC-132 | ficha materializada neste ciclo; acoplada a Awayen |
| Sophia | RC-009 | produzida nas instalações de Awaymaion |
| Olm (Quarto Logos) | RC-092 | surgiu "a partir" do forno de Vishnu → Asphezian |
| Mohen So | RC-081 | avatar Keshava; fenvans → Sophia |
| Fenvans | RC-064 | seres-cobaias (ampliação retida — sem ficha física) |
| Radiatas | RC-093 | 1 banda cerebral (ampliação retida) |
| Bilatérios | RC-035 | 2 hemisférios; origem via encontro dos fornos (ampliação retida) |
| Cérebro Radiata | RC-631 | ampliado (radiata emocionais × racionais) |
| Biodemos | RC-036 | gênero emergido de Awaymaion |
| Nidana | RC-154 | ovo cósmico/doença (ampliação retida) |
| Shiva (Tártaro) | RC-102 | Segundo Logos; Tamas; Pai dos Demos |
| Brahma/Javé (Caos) | RC-037 | Primeiro Logos; CFDP doente |
| Trimurti | RC-104 | Lila; construtora dos fornos |
| Asphezian | RC-025 | nave onde Olm apareceu após o forno |

### B. Conceitos deste material absorvidos pela Base (ciclo ART-2025-08-01)

| Conceito | Ação | Resultado |
|---|---|---|
| STT "forno de Alamaior" | Resolução | = Awaymaion (RC-499) — [REVISAR] limpo em RC-009/RC-092 |
| STT "projeto tal" | Resolução | = Projeto Talm (RC-091) |
| Fornos Replicadores | **RC-771 criado** | nó-guarda-chuva estrutural (exceção à Navalha de Ockham, autorizada) |
| Almaior/Alamaior | RC-500 corrigido | ficha de remissão direta a RC-499 |
| Forno de Awaymaion | RC-499 promovido | ⚪→🟡 com ficha física |
| Val Tam × Awayen | RC-132 materializado | conexão inédita: consciência de Val Tam acoplada/prisioneira |
| "Awayen – A Central de Realidades" | B083 cadastrada | obra anunciada [REVISAR grafia 'Awayem'] |
| ART-2025-08-01 | Registrado na BIBLIO | obra complementar do curador |

### C. Incertezas do texto (marcadas [REVISAR])

Grafia "Awayem" (título do livro) × "Awayen" (forno); datas — Shiva ~12,17 bi anos / Vishnu ~4,1 bi anos / cérebro bilatério ~4 bi anos (conferir B050); "desconstituição Adhydaiva de Vishnu em 2016"; "Frankstein" [sic] no original; "Sai Baba edificado a partir do que veio de Krishna"; "recriar a Colmeia Trimurtiana em moldes biológicos".

### D. Quarentenas aplicadas

- **Teológica (crítica):** "doença do Criador", CFDP "já doente", "zumbi de si mesmo", "refém do progresso das suas criaturas", "favor divino" — leitura de Ellam via curador, não fato;
- **Científica:** taxonomia radiata/bilatério e "banda cerebral" = leitura da RC, não neurociência; elementos pesados/3ª geração de estrelas = contexto narrativo;
- **Natureza do material:** texto do curador baseado em Ellam (ART-2025-08-01) — não é fonte primária do autor; falas/afirmações não viram ontologia sem devolutiva;
- **Datas:** todas as cronologias [REVISAR] até conferência com B050.
"""

def quebrar_paragrafos(texto, limite=380):
    """Quebra um parágrafo longo em blocos de até ~limite caracteres (em frases)."""
    frases = re.split(r"(?<=[.!?…])\s+", texto.strip())
    blocos, atual = [], ""
    for f in frases:
        if len(atual) + len(f) > limite:
            blocos.append(atual)
            atual = f
        else:
            atual = (atual + " " + f).strip()
    if atual:
        blocos.append(atual)
    return [b for b in blocos if b.strip()]

def main():
    linhas = [l.rstrip("\r") for l in ORIG.read_text(encoding="utf-8-sig").splitlines()]
    partes = {}  # num -> {'titulo':..., 'secoes': [(subtitulo, [linhas...])]}
    # identifica início das partes
    idx_parte = [i for i, l in enumerate(linhas) if re.match(r"^Parte (I|II|III)", l)]
    idx_parte.append(len(linhas))

    def nome_parte(l):
        m = re.match(r"^Parte (I{1,3}) ?2?[::]?\s*(.*)", l)
        if m:
            rom = m.group(1)
            num = {"I": "I", "II": "II", "III": "III"}[rom]
            return f"{num}", m.group(2).strip()
        return None, None

    for k in range(3):
        i0, i1 = idx_parte[k], idx_parte[k + 1]
        num, titulo = nome_parte(linhas[i0])
        corpo = linhas[i0 + 1:i1]
        partes[num] = {"titulo": titulo, "corpo": corpo}

    out = [CABECALHO]

    titulo_partes = {
        "I": "PARTE I — Awayen: A Central de Realidades de Brahma/Javé",
        "II": "PARTE II — Awaylengan: O Misterioso Forno de Shiva",
        "III": "PARTE III — Awaymaion: O Forno da Esperança de Vishnu",
    }

    for num in ["I", "II", "III"]:
        p = partes[num]
        corpo = p["corpo"]
        out.append(f"\n# {titulo_partes[num]}\n")
        # separa seções: linhas que são títulos (Dossiê:, Prefácio:, Capítulo X:, Epílogo:) ou bullets contínuos
        secao_atual = "## Introdução"
        blocos = {}
        for l in corpo:
            s = l.strip()
            if not s:
                continue
            m = re.match(r"^(Dossiê:[^\n]*|Prefácio:[^\n]*|Capítulo [IVX]+:[^\n]*|Epílogo:[^\n]*)$", s)
            if m:
                secao_atual = "## " + s
                blocos.setdefault(secao_atual, [])
                continue
            # bullets • do sumário/introdução — agrupa como introdução
            blocos.setdefault(secao_atual, []).append(s)
        # monta
        primeiro = True
        for sec, linhas_sec in blocos.items():
            if not linhas_sec:
                continue
            # título da seção: usa o próprio (## ...) ou "## Introdução"
            if sec == "## Introdução" and primeiro:
                out.append("## Introdução — o que esta parte cobre\n")
            elif sec != "## Introdução":
                out.append(sec + "\n")
            primeiro = False
            # junta bullets (•) separadamente
            bullets = [x for x in linhas_sec if x.startswith("•")]
            normais = [x for x in linhas_sec if not x.startswith("•")]
            if normais:
                for par in quebrar_paragrafos(" ".join(normais)):
                    out.append(f"> {par}\n")
            if bullets:
                for b in bullets:
                    # quebra bullets longos
                    for par in quebrar_paragrafos(b.lstrip("• ").strip()):
                        out.append(f"> • {par}\n")
        out.append("")

    out.append(GLOSSARIO)
    SAIDA.write_text("\n".join(out), encoding="utf-8")
    total = sum(len(l.split()) for l in out)
    print(f"apostila.md gerado: {len(out)} linhas, ~{total} palavras")

if __name__ == "__main__":
    main()
