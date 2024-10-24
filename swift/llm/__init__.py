# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from swift.utils.import_utils import _LazyModule

if TYPE_CHECKING:
    # Recommend using `xxx_main`
    from .app_ui import gradio_chat_demo, gradio_generation_demo, app_ui_main
    from .infer import (deploy_main, infer_main, merge_lora_main, merge_lora, VllmEngine, InferRequest, RequestConfig,
                        InferStats, LmdeployEngine, PtEngine)
    from .export import export_main
    from .eval import eval_main
    from .train import sft_main, pt_main, rlhf_main
    from .argument import (EvalArguments, InferArguments, SftArguments, ExportArguments, DeployArguments, RLHFArguments,
                           WebuiArguments, AppUIArguments)
    from .template import TEMPLATE_MAPPING, Template, Word, get_template, TemplateType, register_template
    from .model import MODEL_MAPPING, ModelType, get_model_tokenizer, safe_snapshot_download, HfConfigFactory
    from .dataset import (AlpacaPreprocessor, MessagesPreprocessor, AutoPreprocessor, DatasetName, DATASET_MAPPING,
                          MediaResource, register_dataset, register_dataset_info, dataset_map, stat_dataset, LLMDataset,
                          LLMIterableDataset, LazyLLMDataset, ConstantLengthDataset, print_example, sort_by_max_length,
                          standard_keys, load_dataset, DATASET_TYPE)
    from .utils import (deep_getattr, to_device, Messages, History, decode_base64, history_to_messages,
                        messages_to_history, safe_tokenizer_decode)
    from .module_mapping import MODEL_KEYS_MAPPING, MultiModelKeys
else:
    _extra_objects = {k: v for k, v in globals().items() if not k.startswith('_')}
    _import_structure = {
        'app_ui': ['gradio_chat_demo', 'gradio_generation_demo', 'app_ui_main'],
        'rlhf': ['rlhf_main'],
        'infer': [
            'deploy_main', 'merge_lora', 'infer_main', 'merge_lora_main', 'VllmEngine', 'InferRequest', 'RequestConfig',
            'InferStats', 'LmdeployEngine', 'PtEngine'
        ],
        'export': ['export_main'],
        'eval': ['eval_main'],
        'train': ['sft_main', 'pt_main', 'rlhf_main'],
        'argument': [
            'EvalArguments', 'InferArguments', 'SftArguments', 'ExportArguments', 'WebuiArguments', 'DeployArguments',
            'RLHFArguments', 'AppUIArguments'
        ],
        'template': ['TEMPLATE_MAPPING', 'Template', 'Word', 'get_template', 'TemplateType', 'register_template'],
        'model': ['MODEL_MAPPING', 'ModelType', 'get_model_tokenizer', 'safe_snapshot_download', 'HfConfigFactory'],
        'dataset': [
            'AlpacaPreprocessor', 'ClsPreprocessor', 'ComposePreprocessor', 'MessagesPreprocessor', 'DatasetName',
            'DATASET_MAPPING', 'MediaResource', 'register_dataset', 'register_dataset_info', 'dataset_map',
            'stat_dataset', 'LLMDataset', 'LLMIterableDataset', 'LazyLLMDataset', 'ConstantLengthDataset',
            'print_example', 'sort_by_max_length', 'standard_keys', 'load_dataset', 'DATASET_TYPE'
        ],
        'utils': [
            'deep_getattr', 'to_device', 'History', 'Messages', 'decode_base64', 'history_to_messages',
            'messages_to_history', 'safe_tokenizer_decode'
        ],
        'module_mapping': ['MODEL_KEYS_MAPPING', 'MultiModelKeys']
    }

    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects=_extra_objects,
    )
