import compas
from compas.datastructures import Network
from compas.plotters import NetworkPlotter

network = Network.from_obj(compas.get('lines.obj'))

plotter = NetworkPlotter(network)

plotter.draw_vertices(
    text='key',
    facecolor={key: '#ff0000' for key in network.leaves()},
    radius=0.15
)
plotter.draw_edges()

plotter.show()