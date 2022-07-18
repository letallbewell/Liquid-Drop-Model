import pandas as pd

link = 'https://en.wikipedia.org/wiki/List_of_chemical_elements'

df = pd.read_html(link,header=1)[0]
df = df[df.columns[:3]]
df = df.iloc[2:]
df.columns = ['Z','Symbol','Name']
df.to_csv('Elements.csv', index=False)

print("Successfully fetched the elements from Wikipedia")