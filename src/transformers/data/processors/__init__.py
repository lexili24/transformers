# flake8: noqa
# There's no way to ignore "F401 '...' imported but unused" warnings in this
# module, but to preserve other warnings. So, don't check this module at all.

### changes were made to reflect superglue benchmark 
from .glue import glue_convert_examples_to_features, glue_output_modes, glue_processors, glue_tasks_num_labels
from .superglue import superglue_convert_examples_to_features, superglue_output_modes, superglue_processors, superglue_tasks_num_labels
from .squad import SquadExample, SquadFeatures, SquadV1Processor, SquadV2Processor, squad_convert_examples_to_features
from .utils import DataProcessor, InputExample, InputFeatures, InputFeatures_w, SingleSentenceClassificationProcessor, COPAInputExample, WiCInputExample, WSCInputExample
from .xnli import xnli_output_modes, xnli_processors, xnli_tasks_num_labels
