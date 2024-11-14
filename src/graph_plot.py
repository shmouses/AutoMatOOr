
from pyvis.network import Network

# Create a new network graph
net = Network(directed=True, height='750px', width='100%', notebook=True, cdn_resources='in_line')

# Add nodes for each class with color coding for their functionalities
data_handling_color = "skyblue"
statistical_analysis_color = "lightgreen"
ml_model_color = "lightcoral"
active_learning_color = "lightyellow"
workflow_color = "lightgray"

# Add nodes
nodes = [
    ('DataLoader', data_handling_color),
    ('DataObject', data_handling_color),
    ('DataCurator', data_handling_color),
    ('StatisticalAnalyzer', statistical_analysis_color),
    ('ModelTrainer', ml_model_color),
    ('ModelOptimizer', ml_model_color),
    ('SurrogateGenerator', ml_model_color),
    ('PredictionModule', ml_model_color),
    ('DataAcquisition', active_learning_color),
    ('WorkflowManager', workflow_color)
]

for node, color in nodes:
    net.add_node(node, label=node, color=color)

# Add edges to show relationships
edges = [
    ('DataLoader', 'DataObject', 'loads'),
    ('DataCurator', 'DataObject', 'curates'),
    ('StatisticalAnalyzer', 'DataObject', 'analyzes'),
    ('StatisticalAnalyzer', 'DataCurator', 'informs curation'),
    ('ModelTrainer', 'DataObject', 'trains'),
    ('ModelOptimizer', 'ModelTrainer', 'optimizes'),
    ('SurrogateGenerator', 'ModelTrainer', 'provides surrogate'),
    ('PredictionModule', 'ModelTrainer', 'uses model'),
    ('PredictionModule', 'SurrogateGenerator', 'predicts on surrogate'),
    ('DataAcquisition', 'PredictionModule', 'acquires'),
    ('StatisticalAnalyzer', 'PredictionModule', 'evaluates predictions'),
    ('WorkflowManager', 'DataLoader', 'manages'),
    ('WorkflowManager', 'ModelTrainer', 'manages'),
    ('WorkflowManager', 'ModelOptimizer', 'manages'),
    ('WorkflowManager', 'PredictionModule', 'manages'),
    ('WorkflowManager', 'DataAcquisition', 'manages')
]

for source, target, title in edges:
    net.add_edge(source, target, title=title)

# Generate and save the interactive HTML file
net.show('software_flow_chart.html')