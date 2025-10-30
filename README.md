# 📈 Desafio de Análise e Padronização de Dados 

## 👤 Contexto

Como Analista de Dados recém-chegado(a) ao time de **Gente e Gestão**, a tarefa proposta foi **analisar e padronizar uma base de dados** com informações sobre o desempenho e o engajamento dos membros da organização.  

A base original estava despadronizada, apresentando variações de texto, tipos incorretos e valores nulos, exigindo tratamento completo antes de ser utilizada em relatórios e dashboards.

---

## 🧰 Ferramentas Utilizadas

- **Google Planilhas** → Base de dados original compartilhada pela equipe.  
- **VS Code** → Ambiente de desenvolvimento utilizado para o tratamento e análise dos dados.  
- **Python** → Linguagem utilizada para o tratamento e padronização dos dados.  
- **Biblioteca Pandas** → Responsável pelas operações de limpeza, transformação e análise.  
- **Exportação .xlsx** → Base final tratada e padronizada para visualizações e dashboards.

---

## ⚙️ Etapas do Processamento

### 1️⃣ Padronização da Coluna `Nivel_Senioridade`
- A coluna apresentava valores inconsistentes, como *“Jr”*, *“P”*, *“pleno”*, *“N/D”*, entre outros.  
- Todos foram **padronizados para apenas três categorias:**  
  - `Júnior`  
  - `Pleno`  
  - `Sênior`  
- Valores nulos foram preenchidos com a **moda** (categoria mais frequente).

---

### 2️⃣ Padronização das Colunas `Avaliacao_Tecnica` e `Avaliacao_Comportamental`
- As avaliações apresentavam números com **ponto decimal (ex: 8.5)** e alguns valores **nulos (NaN)**.  
- Todos os valores foram convertidos para o formato numérico com **vírgula decimal (ex: 8,5)**.  
- Valores nulos foram tratados da seguinte forma:  
  - `Avaliacao_Tecnica` → preenchida com a **média aritmética** da coluna.  
  - `Avaliacao_Comportamental` → preenchida com a **média aritmética** da coluna.

---

### 3️⃣ Tratamento da Coluna `Engajamento_PIGs`
- A coluna estava em formato de texto (ex: `90%`, `75%`, `N/A`).  
- Todos os valores foram convertidos para **decimal numérico** (ex: `90%` → `0.9`).  
- Valores nulos e inválidos foram substituídos pela **média aritmética** dos valores válidos.

---

### 4️⃣ Criação da Coluna `Score_Desempenho`
- Foi criada uma nova coluna calculada com a seguinte **fórmula**:
- 
- Essa métrica representa o **desempenho geral** do membro, considerando o equilíbrio entre habilidades técnicas e comportamentais.

---

### 5️⃣ Criação da Coluna `Status_Membro`
- Critério definido:  
- Se `Score_Desempenho >= 7.0` **e** `Engajamento_PIGs >= 0.8` → **Em Destaque**  
- Caso contrário → **Padrão**  
- Essa etapa permitiu **classificar os membros** com base em desempenho e engajamento.

---

## 📊 Resultado Final

- Base final exportada em formato **.xlsx** com todas as colunas tratadas e novas métricas adicionadas.  
- Dados prontos para visualização em dashboards e relatórios de **Engajamento, Desenvolvimento e Performance**.





