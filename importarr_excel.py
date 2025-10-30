import pandas as pd


pd.set_option('display.max_rows', None)  # mostrar todas as linhas
pd.set_option('display.max_columns', None)  # mostrar todas as colunas
pd.set_option('display.width', None)        #ajusta corretamente a largura

arquivo = "dados/Base_Membros_Desempenho.csv"   #caminho para achar a tabela/arquivo
planilha = pd.read_csv(arquivo, sep = ",")                #le o arquivo excel/taabela e armazena na variavel planilha            

       


#Primeira parte do desafio - Padronizar coluna Nivel_Senioridade

planilha["Nivel_Senioridade"]= planilha["Nivel_Senioridade"].astype(str).str.strip().str.lower()

mapeamento = {
    "júnior": "Júnior",
    "jr": "Júnior",
    "p" : "Pleno",
    "pleno": "Pleno",
    "senior" : "Sênior",
    "sênior" : "Sênior",
    "n/d": None
    }

planilha["Nivel_Senioridade"]= planilha["Nivel_Senioridade"].replace(mapeamento)   #aplica o mapeamento na coluna nivel_superioridade

moda= planilha["Nivel_Senioridade"].mode()[0]   #calcula a moda 


planilha["Nivel_Senioridade"] = planilha["Nivel_Senioridade"].fillna(moda)

#segunda parte do desafio - padronizar colunas avaliacao_tecnica e avaliacao_comportamental


planilha["Avaliacao_Tecnica"]= planilha["Avaliacao_Tecnica"].astype(str).str.replace(",", ".", regex=False)    #converte para strinf e troca virgula por ponto
planilha["Avaliacao_Comportamental"]= planilha["Avaliacao_Comportamental"].astype(str).str.replace(",", ".", regex=False)


planilha["Avaliacao_Tecnica"]= pd.to_numeric(planilha["Avaliacao_Tecnica"], errors="coerce")                 #converte para tipo numerico / valores invalidos viram NaN
planilha["Avaliacao_Comportamental"] = pd.to_numeric(planilha["Avaliacao_Comportamental"], errors = "coerce")


media_tecnica= planilha["Avaliacao_Tecnica"].mean()
media_comportamental= planilha ["Avaliacao_Comportamental"].mean()

planilha["Avaliacao_Tecnica"] = planilha["Avaliacao_Tecnica"].fillna(media_tecnica)
planilha["Avaliacao_Comportamental"]= planilha["Avaliacao_Comportamental"].fillna(media_comportamental)


avaliacao_tecnica_num = planilha["Avaliacao_Tecnica"]   #armazena uma copia numerica antes de formatar 
avaliacao_comportamental_num = planilha["Avaliacao_Comportamental"]  


planilha["Avaliacao_Tecnica"] = planilha ["Avaliacao_Tecnica"].map(lambda x: f"{x:.1f}".replace(".", ","))
planilha["Avaliacao_Comportamental"]= planilha["Avaliacao_Comportamental"].map(lambda x : f"{x:.1f}".replace(".", ","))


#desafio 3 - tratar coluna Engajamento_PiGs:

planilha["Engajamento_PIGs"] = planilha["Engajamento_PIGs"].astype(str).str.strip().str.lower()


planilha["Engajamento_PIGs"] = planilha["Engajamento_PIGs"].replace(["n/a"], None)


planilha["Engajamento_PIGs"] = planilha["Engajamento_PIGs"].str.replace("%", "", regex=False)
planilha["Engajamento_PIGs"] = pd.to_numeric(planilha["Engajamento_PIGs"], errors="coerce") / 100


media_engajamento = planilha["Engajamento_PIGs"].mean()


planilha["Engajamento_PIGs"] = planilha["Engajamento_PIGs"].fillna(media_engajamento)

engajamento_num = planilha["Engajamento_PIGs"] # copia numerica antes da formatacao

planilha["Engajamento_PIGs"] = planilha["Engajamento_PIGs"].map(lambda x: f"{x:.1f}".replace(".", ","))


#parte 4
planilha["Score_Desempenho"] = (avaliacao_tecnica_num * 0.5) + (avaliacao_comportamental_num * 0.5)

# Formata o resultado com uma casa decimal e vírgula
planilha["Score_Desempenho"] = planilha["Score_Desempenho"].map(lambda x: f"{x:.1f}".replace(".", ","))


#quinta parte 

planilha["Status_Membro"] = ["Em Destaque" if (s >= 7.0 and e >= 0.8) else "Padrão"
                             for s, e in zip(planilha["Score_Desempenho"].astype(str).str.replace(",", ".").astype(float),
                                             engajamento_num)]

planilha.to_excel("dados/Base_Membros_Desempenho_Tratado.xlsx", index=False)

print(planilha.to_string(index=False))










  