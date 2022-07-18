# Liquid-Drop-Model
The stability of the nucleus can be explained to some degree by the liquid drop model. Here is a plot of the binding energy per nucleon according to this simple model.

# The model

The mass of an atomic nucleus, for $N$ neutrons, $Z$ protons, and therefore $A=N+Z$ nucleons, is given by

$$ m=Zm_{\rm {p}}+Nm_{\rm {n}}-{\frac {E_{\rm {B}}(N,Z)}{c^{2}}}$$

where $m_{\rm {p}}$ and $m_{\rm {n}}$ are the rest mass of a proton and a neutron, respectively, and $E_{\rm {B}}$ is the binding energy of the nucleus.

The semi-empirical mass formula states the binding energy is:
$$E_{B} = a_{V} A - a_{S} A^{2/3} - a_{C} \frac{Z^2}{A^{\frac{1}{3}}} - a_{Sym} \frac{\left( N -Z \right)^{2}}{A} - \frac{\delta}{A^{\frac{1}{2}}}.$$

These parameters are empirically set to $a_{V} = 16 MeV$, $a_{S} = 20 MeV$, $a_{C} = 0.75 MeV$, $a_{Sym} = 21 MeV$, and $\delta = \pm 11.2 MeV \text{or} 0$ depending on the eveness of $Z$ and $A$. 

For more detailed discussion see [Nuclear models:
The liquid drop model
Fermi-Gas Model ](http://atlas.physics.arizona.edu/~shupe/Indep_Studies_2015/Notes_Goethe_Univ/A2_Nuclear_Models_LiqDrop_FermiGas.pdf) or any standard nucler physics textbook.

<p float="left">
  <img src="/Binding Energy 2D projection.png" width="300" />
  <img src="Binding Energy vs Mass Number.png" width="300" /> 
</p>

## Interactive Plot

# Running the code

## Install requirements
```bash
pip3 install -r requirements.txt
```
## Get element symmbols from wikipedia and save it to *Elements.csv*
```bash
python get_elements.py
```

## Generate Plots
```bash
python create_plots.py
```
