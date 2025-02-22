# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import pytest

from ..agents.fixtures import AGENTS_FIXTURES
from ..conftest import get_provider_fixture_overrides
from ..datasetio.fixtures import DATASETIO_FIXTURES
from ..inference.fixtures import INFERENCE_FIXTURES
from ..safety.fixtures import SAFETY_FIXTURES
from ..scoring.fixtures import SCORING_FIXTURES
from ..tools.fixtures import TOOL_RUNTIME_FIXTURES
from ..vector_io.fixtures import VECTOR_IO_FIXTURES
from .fixtures import EVAL_FIXTURES

DEFAULT_PROVIDER_COMBINATIONS = [
    pytest.param(
        {
            "eval": "meta_reference",
            "scoring": "basic",
            "datasetio": "localfs",
            "inference": "fireworks",
            "agents": "meta_reference",
            "safety": "llama_guard",
            "vector_io": "faiss",
            "tool_runtime": "memory_and_search",
        },
        id="meta_reference_eval_fireworks_inference",
        marks=pytest.mark.meta_reference_eval_fireworks_inference,
    ),
    pytest.param(
        {
            "eval": "meta_reference",
            "scoring": "basic",
            "datasetio": "localfs",
            "inference": "together",
            "agents": "meta_reference",
            "safety": "llama_guard",
            "vector_io": "faiss",
            "tool_runtime": "memory_and_search",
        },
        id="meta_reference_eval_together_inference",
        marks=pytest.mark.meta_reference_eval_together_inference,
    ),
    pytest.param(
        {
            "eval": "meta_reference",
            "scoring": "basic",
            "datasetio": "huggingface",
            "inference": "together",
            "agents": "meta_reference",
            "safety": "llama_guard",
            "vector_io": "faiss",
            "tool_runtime": "memory_and_search",
        },
        id="meta_reference_eval_together_inference_huggingface_datasetio",
        marks=pytest.mark.meta_reference_eval_together_inference_huggingface_datasetio,
    ),
]


def pytest_configure(config):
    for fixture_name in [
        "meta_reference_eval_fireworks_inference",
        "meta_reference_eval_together_inference",
        "meta_reference_eval_together_inference_huggingface_datasetio",
    ]:
        config.addinivalue_line(
            "markers",
            f"{fixture_name}: marks tests as {fixture_name} specific",
        )


def pytest_generate_tests(metafunc):
    if "eval_stack" in metafunc.fixturenames:
        available_fixtures = {
            "eval": EVAL_FIXTURES,
            "scoring": SCORING_FIXTURES,
            "datasetio": DATASETIO_FIXTURES,
            "inference": INFERENCE_FIXTURES,
            "agents": AGENTS_FIXTURES,
            "safety": SAFETY_FIXTURES,
            "vector_io": VECTOR_IO_FIXTURES,
            "tool_runtime": TOOL_RUNTIME_FIXTURES,
        }
        combinations = (
            get_provider_fixture_overrides(metafunc.config, available_fixtures) or DEFAULT_PROVIDER_COMBINATIONS
        )
        metafunc.parametrize("eval_stack", combinations, indirect=True)
