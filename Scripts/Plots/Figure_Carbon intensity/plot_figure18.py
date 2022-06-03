import pandas as pd
import numpy as np
from matplotlib import gridspec
from plotnine import *
import matplotlib.pyplot as plt
import seaborn as sns

region_cmap = {'CE': 'grey',
               'NO': '#FFBE00',
               'OR': '#BF008E',
               'SU': '#089701'}
region_order = ['CE', 'NO', 'OR', 'SU']

data1 = pd.read_csv("data_figure.csv")
data = data1


adjust_text_dict = {
    'expand_points': (1.8, 2),
    'ha': 'center',
    'va': 'center',
}

g3 = (ggplot(data=data) +
      aes(x=data['WAT'], y=data['Fossil'],fill=data['CO2']) +
      geom_point(alpha=0.35, size = 3.5) +
      geom_label(aes(label=data['Label_2']), size=8, adjust_text=adjust_text_dict) +
      scale_colour_manual(values=region_cmap, alpha=1) +
      scale_fill_distiller(type='div', palette='RdBu', direction=-1,limits = (9,350) ) +
      facet_wrap('Scenario', ncol=3, scales="free_x", labeller={'Normal year':'Normal years','Dry year':'Dry years','Wet year':'Wet years'}) +
      labs(x = 'Hydro Generation [TWh]', y='Fossil Generation [TWh]', fill='CO2 [kg/MWh]') +
      theme_minimal() +
      theme(legend_direction='vertical', panel_border=element_rect(color='black', size=1)) +
      scale_y_continuous(limits = (0, 3))  + scale_x_continuous(limits = (0, 3)) 
      )

g3

(ggsave(g3, "figure18b.png", width=15.5 / 2.5, height=7 / 2.5, dpi=300))

