import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
from tqdm.auto import tqdm
import plotly.express as px

# Load elements list
df = pd.read_csv('Elements.csv') 
Zs = df['Z'].tolist()
Symbols = df['Symbol'].tolist()

# Liquid drop model paramenters
a_V = 16
a_S = 20
a_C = 0.75
a_Sym = 21
c = 299792458 
delta = 11.2/(c**2)

# Binding energy calculation
def BE(Z,N):
    
    A = N + Z
    
    E = a_V*A - a_S*A**(2/3) - a_C*(Z**2/A**(1/3)) - a_Sym*(A-2*Z)**2/A
    
    E = E - ((NN%2 == 0) & (ZZ%2 == 0)) * delta\
        + ((NN%2 == 1) & (ZZ%2 == 1)) * delta

    E = E/A

    return E

# Grid
N = np.linspace(0,118,118)
Z = N
ZZ, NN = np.meshgrid(Z,N)
AA = ZZ + NN 

# Calculate binding energy
E = BE(ZZ,NN)
E[np.isnan(E)] = 0
E[E<0] = 0

# Calculate most stable neutron numbers from binding energy
Ns = np.argmax(E, axis=1)
Es = [E[z-1,n] for z,n in tqdm(zip(Zs,Ns))]



c = plt.pcolor(ZZ,NN,E, cmap='hot')
plt.xlabel('$Z$')
plt.ylabel('$N$')
plt.colorbar(c)
plt.savefig('Binding Energy 2D projection.png')

plt.clf()
plt.scatter(Zs+Ns,Es)
plt.xlabel('$A$')
plt.ylabel('Binding energy/ nucleon (MeV)')
plt.savefig('Binding Energy vs Mass Number.png')


fig = go.Figure(data=[go.Surface(z=E.T, x=ZZ, y=NN, colorscale='RdBu',
								hovertemplate ='<b>Z</b>: %{x}'+\
					            '<br><b>N</b>: %{y}'+\
					            '<br><b>Binding Energy</b>: %{z}', 
					     		opacity=0.5),])

fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))

fig.add_scatter3d(x = Zs, y = Ns, z = Es, 
				 text = df['Symbol'].tolist(),
				 hovertemplate ='<b>Z</b>: %{x}'+\
					            '<br><b>N</b>: %{y}'+\
					            '<br><b>Binding Energy</b>: %{z}'+\
					            '<br><b>Element</b>: %{text}',
				  mode='markers')
print(Zs)
print(df['Symbol'])

fig.update_layout(title='Nuclear Binding Energy - Liquid Drop Model',
				  autosize=False, width=800, height=900)

fig.update_layout(scene = dict(
                    xaxis_title='Z',
                    yaxis_title='N',
                    zaxis_title='Binding energy/ nucleon'))

fig.update_layout(hovermode='closest')

fig.write_html('Binding Energy Per Nucleon (Interactive).html')
