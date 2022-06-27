import pandas as pd
from plotnine import *

data_toplot = pd.read_csv("data_HourlyGeneration.csv")

g = (ggplot(data_toplot) +
     aes(x=data_toplot['hour'], y=data_toplot['capacity'], fill=data_toplot['type_label'],account = False) +
     geom_area() +
     theme_light() +
     scale_fill_manual(values={ 'Wind power': "#41afaaff", 'Solar power': "#e6a532", 'Hydro-power': "#00a0e1ff", 
                               'Gas' :'#d7642dff','Oil' :  'magenta','Biomass' :'#7daf4bff'},
                       name=' ') +
     facet_wrap('Scenario', ncol=2, scales="free_x", labeller={'Scenario1':'Min demand','Scenario2':'Max demand'})+
     scale_x_continuous(breaks=range(0, 23, 2)) +
     scale_y_continuous() +
     labs(x="hour", y="Total capacity") +
     theme_minimal()
     )

(ggsave(g, "HourlyGeneration.png", width=6, height=2.5))


