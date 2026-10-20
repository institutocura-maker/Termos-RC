# Mapa consolidado — linha de produção STT (Fase 0)

**Data:** 2026-10-20
**Lote:** `stt-lote-2026-10`
**Executor:** `ferramentas/fase0_ingestao_stt_lote_2026_10.py`
**Estado:** **Fase 0 concluída — triagem preparada, nenhuma mutação da Base.**

## Delimitação operacional

A linha de produção começa unicamente nas **309 cópias derivadas normalizadas**
em `normalizados_stt_lote_2026-10/`. Os STT em `uploads_recepcao/` não foram
abertos nem pesquisados por este executor; seus nomes e SHA-256 permanecem no
registro apenas como proveniência declarada nos manifestos que a normalização
selou. Portanto, esta geração não transforma o bruto em fonte operacional.

Também não criou ciclo, ficha, termo, relação, apostila ou alteração em
`ferramentas/dados_termos.py`. O `motor.py` permanece fora desta etapa e só
poderá ser chamado para uma fonte/lote após despacho curatorial específico.

## Portão de ingresso — aprovado

| Verificação | Resultado |
|---|---:|
| Fontes declaradas no manifesto de normalização | 309 |
| Derivados declarados | 309 |
| Derivados presentes e com SHA-256 conferido | 309 |
| Ligações unívocas por arquivo fonte ↔ derivado | 309 |
| Trocas no rastreio | 1306 |
| Trocas declaradas no manifesto | 1306 |
| Conteúdos brutos abertos nesta Fase 0 | **0** |

**Resultado:** os 309 derivados podem entrar em **triagem**, não em
materialização. Cada `ingresso_id` no `registro-mestre.jsonl` guarda o SHA do
derivado usado na produção e o SHA da fonte STT declarada no seu vínculo.

## Índice e mapa de linhas

- endereços textuais criados: **26389**;
- termos canônicos lidos da Base: **946**;
- aliases ambíguos excluídos do índice automático: **14**;
- sinais exatos e não ambíguos da Base: **11542**.

O endereço `Uxxxxx` é a linha física no derivado. O índice registra apenas uma
correspondência literal de grafia existente na Base; não é verificação contra
a fala, não é citação e não equivale a juízo editorial. A consulta operacional
é feita exclusivamente contra os derivados:

```bash
python3 ferramentas/fase0_ingestao_stt_lote_2026_10.py --buscar "Sophia"
```

### Distribuição de fila por tema primário

| Tema | Fontes |
|---|---:|
| `ANUNNAKI_GENETICA` | 31 |
| `ATLANTIDA_CIVILIZACOES` | 9 |
| `COSMOGONIA_CRIADOR` | 39 |
| `EXTRATERRESTRES_TECNOLOGIA` | 19 |
| `GERAL_SEM_SINAL_FORTE` | 1 |
| `MEDIUNIDADE_ESPIRITUALIDADE` | 71 |
| `MITOLOGIAS_ORIENTAIS` | 25 |
| `MORTE_REENCARNACAO_ETICA` | 15 |
| `REINTEGRACAO_CRISTO` | 35 |
| `SOCIEDADE_CONTEMPORANEA` | 64 |

## Planejamento de capacidade curatorial

Duração total informada: **245:56:52**. O plano
forma lotes sem sobreposição por família temática, buscando **10–12 h** e sem
fracionar uma transcrição. O teto de **25** é para candidatos de cotejo da Base
por lote, não para criação automática de pérolas.

| Lote | Tema | Duração estimada | Fontes | Candidatos | Faixa 10–12h | Ressalva | Ingressos |
|---|---|---:|---:|---:|---|---|---|
| `STT26-01` | Anunnaki, genética e humanidade | 9:51:16 | 11 | 25/25 | aproximação | — | `STT-2026-10-001`<br>`STT-2026-10-011`<br>`STT-2026-10-014`<br>`STT-2026-10-024`<br>`STT-2026-10-025`<br>`STT-2026-10-026`<br>`STT-2026-10-028`<br>`STT-2026-10-029`<br>`STT-2026-10-030`<br>`STT-2026-10-035`<br>`STT-2026-10-034` |
| `STT26-02` | Anunnaki, genética e humanidade | 10:28:02 | 20 | 25/25 | sim | — | `STT-2026-10-039`<br>`STT-2026-10-040`<br>`STT-2026-10-046`<br>`STT-2026-10-049`<br>`STT-2026-10-071`<br>`STT-2026-10-059`<br>`STT-2026-10-069`<br>`STT-2026-10-111`<br>`STT-2026-10-120`<br>`STT-2026-10-141`<br>`STT-2026-10-146`<br>`STT-2026-10-167`<br>`STT-2026-10-182`<br>`STT-2026-10-180`<br>`STT-2026-10-209`<br>`STT-2026-10-230`<br>`STT-2026-10-236`<br>`STT-2026-10-244`<br>`STT-2026-10-266`<br>`STT-2026-10-288` |
| `STT26-03` | Cosmogonia, quedas e história cósmica | 10:11:02 | 10 | 25/25 | sim | — | `STT-2026-10-008`<br>`STT-2026-10-019`<br>`STT-2026-10-027`<br>`STT-2026-10-033`<br>`STT-2026-10-043`<br>`STT-2026-10-047`<br>`STT-2026-10-051`<br>`STT-2026-10-077`<br>`STT-2026-10-054`<br>`STT-2026-10-060` |
| `STT26-04` | Cosmogonia, quedas e história cósmica | 9:51:24 | 11 | 25/25 | aproximação | — | `STT-2026-10-055`<br>`STT-2026-10-057`<br>`STT-2026-10-095`<br>`STT-2026-10-105`<br>`STT-2026-10-117`<br>`STT-2026-10-124`<br>`STT-2026-10-134`<br>`STT-2026-10-132`<br>`STT-2026-10-136`<br>`STT-2026-10-137`<br>`STT-2026-10-144` |
| `STT26-05` | Cosmogonia, quedas e história cósmica | 9:18:16 | 9 | 25/25 | aproximação | — | `STT-2026-10-143`<br>`STT-2026-10-155`<br>`STT-2026-10-147`<br>`STT-2026-10-168`<br>`STT-2026-10-193`<br>`STT-2026-10-207`<br>`STT-2026-10-211`<br>`STT-2026-10-213`<br>`STT-2026-10-217` |
| `STT26-06` | Cosmogonia, quedas e história cósmica | 9:56:41 | 18 | 25/25 | aproximação | — | `STT-2026-10-223`<br>`STT-2026-10-229`<br>`STT-2026-10-235`<br>`STT-2026-10-239`<br>`STT-2026-10-240`<br>`STT-2026-10-252`<br>`STT-2026-10-249`<br>`STT-2026-10-257`<br>`STT-2026-10-267`<br>`STT-2026-10-037`<br>`STT-2026-10-041`<br>`STT-2026-10-097`<br>`STT-2026-10-110`<br>`STT-2026-10-129`<br>`STT-2026-10-297`<br>`STT-2026-10-295`<br>`STT-2026-10-302`<br>`STT-2026-10-306` |
| `STT26-07` | Extraterrestres, tecnologia e cosmos | 11:45:46 | 19 | 25/25 | sim | — | `STT-2026-10-032`<br>`STT-2026-10-036`<br>`STT-2026-10-048`<br>`STT-2026-10-081`<br>`STT-2026-10-092`<br>`STT-2026-10-099`<br>`STT-2026-10-121`<br>`STT-2026-10-119`<br>`STT-2026-10-135`<br>`STT-2026-10-148`<br>`STT-2026-10-153`<br>`STT-2026-10-181`<br>`STT-2026-10-245`<br>`STT-2026-10-243`<br>`STT-2026-10-247`<br>`STT-2026-10-282`<br>`STT-2026-10-290`<br>`STT-2026-10-303`<br>`STT-2026-10-301` |
| `STT26-08` | Experiência espiritual, morte e ética evolutiva | 10:03:19 | 5 | 25/25 | sim | — | `STT-2026-10-002`<br>`STT-2026-10-009`<br>`STT-2026-10-012`<br>`STT-2026-10-017`<br>`STT-2026-10-018` |
| `STT26-09` | Experiência espiritual, morte e ética evolutiva | 10:54:10 | 17 | 25/25 | sim | — | `STT-2026-10-021`<br>`STT-2026-10-023`<br>`STT-2026-10-031`<br>`STT-2026-10-063`<br>`STT-2026-10-062`<br>`STT-2026-10-075`<br>`STT-2026-10-067`<br>`STT-2026-10-068`<br>`STT-2026-10-052`<br>`STT-2026-10-090`<br>`STT-2026-10-088`<br>`STT-2026-10-086`<br>`STT-2026-10-087`<br>`STT-2026-10-093`<br>`STT-2026-10-094`<br>`STT-2026-10-098`<br>`STT-2026-10-101` |
| `STT26-10` | Experiência espiritual, morte e ética evolutiva | 11:06:11 | 22 | 25/25 | sim | — | `STT-2026-10-102`<br>`STT-2026-10-103`<br>`STT-2026-10-108`<br>`STT-2026-10-113`<br>`STT-2026-10-116`<br>`STT-2026-10-115`<br>`STT-2026-10-126`<br>`STT-2026-10-133`<br>`STT-2026-10-125`<br>`STT-2026-10-128`<br>`STT-2026-10-127`<br>`STT-2026-10-138`<br>`STT-2026-10-156`<br>`STT-2026-10-160`<br>`STT-2026-10-166`<br>`STT-2026-10-178`<br>`STT-2026-10-174`<br>`STT-2026-10-169`<br>`STT-2026-10-173`<br>`STT-2026-10-163`<br>`STT-2026-10-164`<br>`STT-2026-10-185` |
| `STT26-11` | Experiência espiritual, morte e ética evolutiva | 10:42:07 | 20 | 25/25 | sim | — | `STT-2026-10-195`<br>`STT-2026-10-184`<br>`STT-2026-10-189`<br>`STT-2026-10-186`<br>`STT-2026-10-198`<br>`STT-2026-10-197`<br>`STT-2026-10-204`<br>`STT-2026-10-208`<br>`STT-2026-10-226`<br>`STT-2026-10-215`<br>`STT-2026-10-218`<br>`STT-2026-10-216`<br>`STT-2026-10-221`<br>`STT-2026-10-238`<br>`STT-2026-10-242`<br>`STT-2026-10-246`<br>`STT-2026-10-260`<br>`STT-2026-10-261`<br>`STT-2026-10-272`<br>`STT-2026-10-273` |
| `STT26-12` | Experiência espiritual, morte e ética evolutiva | 11:23:12 | 22 | 25/25 | sim | — | `STT-2026-10-279`<br>`STT-2026-10-271`<br>`STT-2026-10-278`<br>`STT-2026-10-270`<br>`STT-2026-10-298`<br>`STT-2026-10-296`<br>`STT-2026-10-307`<br>`STT-2026-10-066`<br>`STT-2026-10-079`<br>`STT-2026-10-056`<br>`STT-2026-10-058`<br>`STT-2026-10-073`<br>`STT-2026-10-104`<br>`STT-2026-10-149`<br>`STT-2026-10-157`<br>`STT-2026-10-200`<br>`STT-2026-10-201`<br>`STT-2026-10-231`<br>`STT-2026-10-234`<br>`STT-2026-10-232`<br>`STT-2026-10-237`<br>`STT-2026-10-276` |
| `STT26-13` | Mitologias, tradições e eixo de reintegração | 10:00:17 | 8 | 25/25 | sim | — | `STT-2026-10-005`<br>`STT-2026-10-010`<br>`STT-2026-10-020`<br>`STT-2026-10-074`<br>`STT-2026-10-091`<br>`STT-2026-10-106`<br>`STT-2026-10-112`<br>`STT-2026-10-145` |
| `STT26-14` | Mitologias, tradições e eixo de reintegração | 10:38:06 | 10 | 25/25 | sim | — | `STT-2026-10-159`<br>`STT-2026-10-176`<br>`STT-2026-10-171`<br>`STT-2026-10-187`<br>`STT-2026-10-202`<br>`STT-2026-10-196`<br>`STT-2026-10-199`<br>`STT-2026-10-210`<br>`STT-2026-10-219`<br>`STT-2026-10-222` |
| `STT26-15` | Mitologias, tradições e eixo de reintegração | 10:56:31 | 10 | 25/25 | sim | — | `STT-2026-10-233`<br>`STT-2026-10-241`<br>`STT-2026-10-253`<br>`STT-2026-10-254`<br>`STT-2026-10-248`<br>`STT-2026-10-256`<br>`STT-2026-10-264`<br>`STT-2026-10-265`<br>`STT-2026-10-263`<br>`STT-2026-10-274` |
| `STT26-16` | Mitologias, tradições e eixo de reintegração | 10:18:10 | 14 | 25/25 | sim | — | `STT-2026-10-275`<br>`STT-2026-10-269`<br>`STT-2026-10-283`<br>`STT-2026-10-286`<br>`STT-2026-10-292`<br>`STT-2026-10-289`<br>`STT-2026-10-300`<br>`STT-2026-10-022`<br>`STT-2026-10-044`<br>`STT-2026-10-070`<br>`STT-2026-10-078`<br>`STT-2026-10-109`<br>`STT-2026-10-114`<br>`STT-2026-10-118` |
| `STT26-17` | Mitologias, tradições e eixo de reintegração | 10:55:18 | 8 | 25/25 | sim | — | `STT-2026-10-123`<br>`STT-2026-10-131`<br>`STT-2026-10-140`<br>`STT-2026-10-151`<br>`STT-2026-10-165`<br>`STT-2026-10-175`<br>`STT-2026-10-191`<br>`STT-2026-10-205` |
| `STT26-18` | Mitologias, tradições e eixo de reintegração | 10:07:17 | 11 | 25/25 | sim | — | `STT-2026-10-206`<br>`STT-2026-10-225`<br>`STT-2026-10-224`<br>`STT-2026-10-220`<br>`STT-2026-10-250`<br>`STT-2026-10-258`<br>`STT-2026-10-259`<br>`STT-2026-10-262`<br>`STT-2026-10-281`<br>`STT-2026-10-299`<br>`STT-2026-10-162` |
| `STT26-19` | Sociedade, comportamento e atualidades | 10:31:38 | 5 | 25/25 | sim | — | `STT-2026-10-003`<br>`STT-2026-10-004`<br>`STT-2026-10-006`<br>`STT-2026-10-007`<br>`STT-2026-10-013` |
| `STT26-20` | Sociedade, comportamento e atualidades | 9:16:02 | 11 | 25/25 | aproximação | — | `STT-2026-10-015`<br>`STT-2026-10-016`<br>`STT-2026-10-038`<br>`STT-2026-10-042`<br>`STT-2026-10-045`<br>`STT-2026-10-050`<br>`STT-2026-10-072`<br>`STT-2026-10-065`<br>`STT-2026-10-064`<br>`STT-2026-10-053`<br>`STT-2026-10-076` |
| `STT26-21` | Sociedade, comportamento e atualidades | 9:17:23 | 21 | 25/25 | aproximação | — | `STT-2026-10-061`<br>`STT-2026-10-082`<br>`STT-2026-10-089`<br>`STT-2026-10-084`<br>`STT-2026-10-083`<br>`STT-2026-10-085`<br>`STT-2026-10-080`<br>`STT-2026-10-096`<br>`STT-2026-10-100`<br>`STT-2026-10-107`<br>`STT-2026-10-122`<br>`STT-2026-10-130`<br>`STT-2026-10-142`<br>`STT-2026-10-139`<br>`STT-2026-10-161`<br>`STT-2026-10-150`<br>`STT-2026-10-152`<br>`STT-2026-10-158`<br>`STT-2026-10-154`<br>`STT-2026-10-170`<br>`STT-2026-10-177` |
| `STT26-22` | Sociedade, comportamento e atualidades | 8:31:14 | 9 | 25/25 | aproximação | — | `STT-2026-10-172`<br>`STT-2026-10-183`<br>`STT-2026-10-188`<br>`STT-2026-10-194`<br>`STT-2026-10-179`<br>`STT-2026-10-190`<br>`STT-2026-10-192`<br>`STT-2026-10-212`<br>`STT-2026-10-203` |
| `STT26-23` | Sociedade, comportamento e atualidades | 9:50:33 | 9 | 25/25 | aproximação | — | `STT-2026-10-214`<br>`STT-2026-10-228`<br>`STT-2026-10-227`<br>`STT-2026-10-251`<br>`STT-2026-10-255`<br>`STT-2026-10-280`<br>`STT-2026-10-268`<br>`STT-2026-10-277`<br>`STT-2026-10-287` |
| `STT26-24` | Sociedade, comportamento e atualidades | 10:02:57 | 9 | 25/25 | sim | — | `STT-2026-10-284`<br>`STT-2026-10-285`<br>`STT-2026-10-293`<br>`STT-2026-10-291`<br>`STT-2026-10-294`<br>`STT-2026-10-305`<br>`STT-2026-10-304`<br>`STT-2026-10-308`<br>`STT-2026-10-309` |

Os membros e a evidência inicial de cada fila estão em
`ingestao_stt_lote_2026-10/lotes-planejados.json`. A seleção de 25 candidatos
usa frequência de sinais exatos da Base como **ordem de leitura**, não como
prova, nem como abertura de termo ou alteração de ficha.

## Próximo despacho necessário

Para um lote `STT26-xx`, a curadoria deve deliberar em bloco:

1. quais, se houver, candidatos de cotejo tornam-se pérolas/citações elegíveis;
2. quais hipóteses permanecem pendentes ou são descartadas;
3. qual fonte derivada e quais âncoras entram em um `ciclo.toml` próprio;
4. se algum resultado autoriza o Motor a alterar a Base.

Até esse despacho, o estado de todos os lotes é
`AGUARDANDO-DESPACHO-CURATORIAL` e a Fase 0 é somente um mapa recuperável e
reproduzível.

## Reprodução e retomada segura

```bash
python3 ferramentas/fase0_ingestao_stt_lote_2026_10.py --force
```

A geração valida tudo antes de publicar, constrói os artefatos em diretório
temporário e só troca a versão anterior quando a saída completa está pronta.
