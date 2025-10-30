🧩 Desafio de Análise e Padronização de Dados — Gente e Gestão


👤 Contexto

Como Analista de Dados recém-chegado(a) ao time de Gente e Gestão, a tarefa proposta foi analisar e padronizar uma base de dados com informações sobre o desempenho e o engajamento dos membros da organização.
A base original estava despadronizada, apresentando variações de texto, tipos incorretos e valores nulos, exigindo tratamento completo antes de ser utilizada em relatórios e dashboards.

🛠️ Ferramentas Utilizadas

Google Planilhas → Base de dados original compartilhada pela equipe.

Python → Linguagem utilizada para o tratamento e padronização dos dados.

Biblioteca Pandas → Responsável pelas operações de limpeza, transformação e análise.

Visual Studio Code (VS Code) → Ambiente de desenvolvimento utilizado para escrever e executar o script Python.

CSV (.csv) → Formato intermediário de importação e exportação dos dados.

Excel (.xlsx) → Formato final entregue após o tratamento e enriquecimento da base.

📊 Objetivos do Desafio

Padronizar e corrigir informações inconsistentes na base de dados.

Tratar valores ausentes e uniformizar formatos numéricos e textuais.

Criar novas colunas e indicadores para enriquecer a análise de desempenho dos membros.

🧠 Etapas Realizadas
1. Obtenção da Base de Dados

A base foi disponibilizada em Google Planilhas.
Para realizar o tratamento, o arquivo foi exportado no formato .csv e importado para o VS Code, onde foi utilizado o Python com a biblioteca Pandas para manipulação dos dados.

2. Análise Inicial da Base

Foi feita uma análise exploratória da estrutura dos dados, identificando:

Colunas com formatações incorretas;

Variações nos nomes de níveis de senioridade;

Presença de valores ausentes e inconsistências numéricas;

Tipos de dados incorretos (exemplo: números armazenados como texto).

3. Padronização da Coluna “Nivel_Senioridade”

A coluna apresentava variações como “Jr”, “pleno”, “S”, “N/D”, entre outras.

Todos os valores foram padronizados para: “Júnior”, “Pleno” e “Sênior”.

Os valores nulos foram substituídos pela moda (valor mais frequente da coluna).

4. Padronização das Colunas de Avaliação

As colunas Avaliacao_Tecnica e Avaliacao_Comportamental possuíam diferentes formatações (ponto, vírgula, texto).

Ambas foram convertidas para valores numéricos no padrão de 0 a 10.

Os valores nulos foram preenchidos com a média aritmética de cada coluna, garantindo uniformidade.

5. Tratamento da Coluna “Engajamento_PIGs”

Essa coluna representava a porcentagem de participação nas capacitações (PIGs).

Os dados estavam em formato de texto, como “90%”, “75%” e “N/A”.

Todos foram convertidos para valores decimais (exemplo: 90% → 0,9).

Valores ausentes foram substituídos pela média geral da coluna.

6. Cálculo do “Score_Desempenho”

Foi criada uma nova métrica que representa o desempenho geral do membro, combinando igualmente as avaliações técnica e comportamental.

Fórmula utilizada:
Score_Desempenho = (Avaliacao_Tecnica × 0.5) + (Avaliacao_Comportamental × 0.5).

Essa métrica trouxe uma visão equilibrada da performance de cada membro.

7. Criação da Coluna “Status_Membro”

O objetivo dessa coluna foi classificar os membros conforme o desempenho e engajamento.

Critério utilizado:

“Em Destaque” → quando o Score_Desempenho ≥ 7,0 e Engajamento_PIGs ≥ 0,8;

“Padrão” → nos demais casos.

Essa categorização facilita a identificação de talentos e a tomada de decisões de desenvolvimento.

8. Exportação da Base Final

Após todas as etapas de tratamento e enriquecimento, a base foi exportada em formato .xlsx (Excel), permitindo visualização mais amigável e integração com relatórios e dashboards.
