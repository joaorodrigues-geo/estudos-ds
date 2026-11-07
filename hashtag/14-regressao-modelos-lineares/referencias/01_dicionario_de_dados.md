# Dicionário de dados

Base `dados/processados/diabetes_tratado.csv` — 442 doentes, uma linha por doente.

| Coluna | Original | Descrição | Tipo |
|---|---|---|---|
| `idade` | age | Idade (anos) | Numérico |
| `sexo` | sex | Sexo, codificado 1 ou 2 (a fonte não diz qual é qual) | Categórico |
| `imc` | bmi | Índice de massa corporal (kg/m²) | Numérico |
| `pressao_media` | bp | Pressão arterial média | Numérico |
| `colesterol_total` | s1 (tc) | Colesterol total no soro | Numérico |
| `ldl` | s2 | Lipoproteínas de baixa densidade | Numérico |
| `hdl` | s3 | Lipoproteínas de alta densidade | Numérico |
| `colesterol_hdl` | s4 (tch) | Rácio colesterol total / HDL | Numérico |
| `triglicerideos_log` | s5 (ltg) | Logaritmo dos triglicerídeos no soro | Numérico |
| `glicose` | s6 (glu) | Glicose no sangue | Numérico |
| `progressao` | target | Medida quantitativa da progressão da doença um ano após o início (alvo) | Numérico |
