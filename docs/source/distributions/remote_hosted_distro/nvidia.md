<!-- This file was auto-generated by distro_codegen.py, please edit source -->
# NVIDIA Distribution

The `llamastack/distribution-nvidia` distribution consists of the following provider configurations.

| API | Provider(s) |
|-----|-------------|
| agents | `inline::meta-reference` |
| datasetio | `inline::localfs` |
| eval | `inline::meta-reference` |
| inference | `remote::nvidia` |
| post_training | `remote::nvidia` |
| safety | `remote::nvidia` |
| scoring | `inline::basic` |
| telemetry | `inline::meta-reference` |
| tool_runtime | `inline::rag-runtime` |
| vector_io | `inline::faiss` |


### Environment Variables

The following environment variables can be configured:

- `NVIDIA_API_KEY`: NVIDIA API Key (default: ``)
- `NVIDIA_USER_ID`: NVIDIA User ID (default: `llama-stack-user`)
- `NVIDIA_DATASET_NAMESPACE`: NVIDIA Dataset Namespace (default: `default`)
- `NVIDIA_ACCESS_POLICIES`: NVIDIA Access Policies (default: `{}`)
- `NVIDIA_PROJECT_ID`: NVIDIA Project ID (default: `test-project`)
- `NVIDIA_CUSTOMIZER_URL`: NVIDIA Customizer URL (default: `https://customizer.api.nvidia.com`)
- `NVIDIA_OUTPUT_MODEL_DIR`: NVIDIA Output Model Directory (default: `test-example-model@v1`)
- `GUARDRAILS_SERVICE_URL`: URL for the NeMo Guardrails Service (default: `http://0.0.0.0:7331`)
- `INFERENCE_MODEL`: Inference model (default: `Llama3.1-8B-Instruct`)
- `SAFETY_MODEL`: Name of the model to use for safety (default: `meta/llama-3.1-8b-instruct`)

### Models

The following models are available by default:

- `meta/llama3-8b-instruct (aliases: meta-llama/Llama-3-8B-Instruct)`
- `meta/llama3-70b-instruct (aliases: meta-llama/Llama-3-70B-Instruct)`
- `meta/llama-3.1-8b-instruct (aliases: meta-llama/Llama-3.1-8B-Instruct)`
- `meta/llama-3.1-70b-instruct (aliases: meta-llama/Llama-3.1-70B-Instruct)`
- `meta/llama-3.1-405b-instruct (aliases: meta-llama/Llama-3.1-405B-Instruct-FP8)`
- `meta/llama-3.2-1b-instruct (aliases: meta-llama/Llama-3.2-1B-Instruct)`
- `meta/llama-3.2-3b-instruct (aliases: meta-llama/Llama-3.2-3B-Instruct)`
- `meta/llama-3.2-11b-vision-instruct (aliases: meta-llama/Llama-3.2-11B-Vision-Instruct)`
- `meta/llama-3.2-90b-vision-instruct (aliases: meta-llama/Llama-3.2-90B-Vision-Instruct)`
- `nvidia/llama-3.2-nv-embedqa-1b-v2 `
- `nvidia/nv-embedqa-e5-v5 `
- `nvidia/nv-embedqa-mistral-7b-v2 `
- `snowflake/arctic-embed-l `


### Prerequisite: API Keys

Make sure you have access to a NVIDIA API Key. You can get one by visiting [https://build.nvidia.com/](https://build.nvidia.com/).


## Running Llama Stack with NVIDIA

You can do this via Conda (build code) or Docker which has a pre-built image.

### Via Docker

This method allows you to get started quickly without having to build the distribution code.

```bash
LLAMA_STACK_PORT=8321
docker run \
  -it \
  --pull always \
  -p $LLAMA_STACK_PORT:$LLAMA_STACK_PORT \
  -v ./run.yaml:/root/my-run.yaml \
  llamastack/distribution-nvidia \
  --yaml-config /root/my-run.yaml \
  --port $LLAMA_STACK_PORT \
  --env NVIDIA_API_KEY=$NVIDIA_API_KEY
```

### Via Conda

```bash
llama stack build --template nvidia --image-type conda
llama stack run ./run.yaml \
  --port 8321 \
  --env NVIDIA_API_KEY=$NVIDIA_API_KEY
  --env INFERENCE_MODEL=$INFERENCE_MODEL
```
