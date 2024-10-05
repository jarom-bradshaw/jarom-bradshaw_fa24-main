import pandas as pd
import palmerpenguins
from lets_plot import *

LetsPlot.setup_html()
LetsPlot.setup_html(isolated_frame=True)
penguins = load_penguins()
penguins