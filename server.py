from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

from model import Simulation

from run import sim_params_ebola
from run import sim_params_mers
from run import sim_params_covid

import argparse

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "blue",
                 "r": 0.8}

    if agent.infected:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:
        if agent.immune:
            portrayal["Color"] = "green"
            portrayal["Layer"] = 0
        else:
            portrayal["Color"] = "blue"
            portrayal["Layer"] = 0

    if not agent.alive:
        portrayal["Color"] = "black"
        portrayal["Layer"] = 0

    return portrayal
# Construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--virus", required=False, help="virus type")
args = ap.parse_args()

if args.virus == 'covid':
    sim_params = sim_params_covid
else :
    if args.virus == 'ebola':
        sim_params = sim_params_ebola
    else:
        if args.virus == 'mers':
            sim_params = sim_params_mers
        else:
            sim_params = sim_params_covid

grid = CanvasGrid(
    agent_portrayal,
    sim_params.get('grid_x'),
    sim_params.get('grid_y'),
    sim_params.get('grid_x') * 4,
    sim_params.get('grid_y') * 4)
chart = ChartModule([{"Label": "Infected",
                      "Color": "Red"},
                     {"Label": "Immune",
                      "Color": "Green"},
                     {"Label": "Deaths",
                      "Color": "Black"}],
                    data_collector_name='datacollector')
server = ModularServer(Simulation,
                       [grid, chart],
                       "COVID-19 Model",
                       {"params":sim_params})
server.port = 8521 # The default
server.launch()





