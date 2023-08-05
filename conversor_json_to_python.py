import pandas as pd

json_string = '''[
   {
      "Name":"Nik",
      "Age":30,
      "Activities":["Work", "Study", "Gym"]
   },
   {
      "Name":"Kate",
      "Age":32,
      "Activities":["Work", "Study"]
   },
   {
      "Name":"Evan",
      "Age":45,
      "Activities":["Study", "Gym"]
   }
]'''

# Carregamento do JSON dentro do Dataframe para a leitura do Panda
df = pd.read_json(json_string)

# Função explode do Panda para expandir os conteúdos do elemento "Actitivities" para diferentes linhas repetindo as demais informações

df_exploded = df.explode("Activities", ignore_index=True)

# Resetando o index de cada elemento
df_exploded.reset_index(drop=True, inplace=True)

# Gerando o arquivo CSV
df_exploded.to_csv('file.csv', index=False)

print(df_exploded)
