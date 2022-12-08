from function_to_csv import function_to_csv
from format import csv_to_vtp
from reord.graph_structure import Graph
from reord.reord import parse_csv, set_minimas, reord_algorithm
from reord.mst_algo import kruskal_mst
import math

def wave_function(x, y):
    return math.sin(math.sqrt(x*x + y*y))

function_to_csv.main(step=1, size=18, function=wave_function)

csv_paths = {
    "points" : "function_to_csv/generated_csv/points.csv",
    "lines" : "function_to_csv/generated_csv/lines.csv",
    "triangles" : "function_to_csv/generated_csv/triangles.csv",
    "output": "format/generated_vtp/output_graph.vtu"
}

csv_reord_path = {
    "points" : "function_to_csv/generated_csv/reord_points.csv",
    "lines" : "function_to_csv/generated_csv/reord_lines.csv",
    "triangles" : "function_to_csv/generated_csv/reord_triangles.csv",
    "output": "format/generated_vtp/reord_output_graph.vtu"
}

csv_dual_paths = {
    "points" : "function_to_csv/generated_csv/points_dual.csv",
    "lines" : "function_to_csv/generated_csv/lines_dual.csv",
    "output": "format/generated_vtp/output_dual_graph.vtu"
}

csv_mst_dual_paths = {
    "points" : "function_to_csv/generated_csv/points_dual_mst.csv",
    "lines" : "function_to_csv/generated_csv/lines_dual_mst.csv",
    "output": "format/generated_vtp/output_dual_graph_mst.vtu"
}

csv_comp_dual_paths = {
    "points" : "function_to_csv/generated_csv/points_dual_comp.csv",
    "lines" : "function_to_csv/generated_csv/lines_dual_comp.csv",
    "output": "format/generated_vtp/output_dual_graph_comp.vtu"
}

"""
### Revaluation
graph = Graph(2)
graph = parse_csv(graph, csv_paths)
csv_to_vtp.main(csv_paths)
graph = set_minimas(graph)
graph = reord_algorithm(graph)
graph.convert_to_csv(csv_reord_path)

#Graph before revaluation
dual_non_rev = graph.create_dual()
dual_non_rev.convert_to_csv(csv_dual_paths)

#Application of mst
dual_mst, dual_mst_comp = kruskal_mst(dual_non_rev)
dual_mst.convert_to_csv(csv_mst_dual_paths)
dual_mst_comp.convert_to_csv(csv_comp_dual_paths)

### Generate vtu filecsv_to_vtp.main(csv_reord_path)
csv_to_vtp.main(csv_reord_path)
csv_to_vtp.main(csv_dual_paths)
csv_to_vtp.main(csv_mst_dual_paths)
csv_to_vtp.main(csv_comp_dual_paths)
"""

graph = Graph(2)
graph = parse_csv(graph, csv_paths)
csv_to_vtp.main(csv_paths)
graph = set_minimas(graph)
graph = reord_algorithm(graph,video=True)

graph.convert_to_csv(csv_reord_path)
csv_to_vtp.main(csv_reord_path)