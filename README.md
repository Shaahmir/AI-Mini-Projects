# AI-Mini-Projects

A growing collection of small, practical AI projects, experiments, and implementations.

The goal of this repository is simple: **build things, learn by doing, and keep useful experiments in one place.** Projects range from AI agents and multimodal applications to LLM APIs, inference, tokenization, interfaces, and Retrieval-Augmented Generation (RAG).

Most projects are intentionally self-contained, so you can open a project folder, inspect the notebook/source code, and experiment without navigating a large application codebase.

## Projects

### AI Applications & Agents

| Project | What it covers |
|---|---|
| [AI Website Summarizer](./AI%20Website%20Summarizer/) | Summarizes website content with an AI workflow. |
| [AI Website Summarizer (Local Models)](./AI%20Website%20Summarizer%20(Local%20Models)/) | Website summarization using locally run models. |
| [AI Brochure Generator](./AI%20Brochure%20Generator/) | Generates an AI-assisted brochure workflow. |
| [AI Flight Assistant](./AI%20Flight%20Assistant/) | AI-assisted flight search and travel workflow. |
| [AI Flight Assistant (Multimodal)](./AI%20Flight%20Assistant%20(Multimodal)/) | A multimodal extension of the flight-assistant project. |
| [AI Meeting Minutes Generator](./AI%20Meeting%20Minutes%20Generator/) | Turns meeting audio into structured meeting notes/minutes. |
| [AI Synthetic Data Generator](./AI%20Synthetic%20Data%20Generator/) | Experiments with generating synthetic data using AI models. |
| [AI Best Deal Finder Agent](./AI%20Best%20Deal%20Finder%20Agent/) | An agent-oriented project for finding and comparing product deals. |

### Interfaces, Multimodal & AI Experiments

| Project | What it covers |
|---|---|
| [AI Interfaces in Gradio](./AI%20Interfaces%20in%20Gradio/) | Building interactive AI interfaces with Gradio. |
| [AI Logits Visualiser](./AI%20Logits%20Visualiser/) | Visualizing model logits/token-level model behavior. |
| [Eavesdropping on AI](./Eavesdropping%20on%20AI/) | An experiment focused on observing/interacting with AI behavior. |
| [Jev](./Jev/) | A small AI/LLM experiment. |

### LLM APIs, Inference & Model Tooling

| Project | What it covers |
|---|---|
| [Inference on Modal](./Inference%20on%20Modal/) | Running model inference with Modal. |
| [LLAMA Tokenizer](./LLAMA%20Tokenizer/) | Experiments with LLaMA-style tokenization and token data. |
| [OpenAI Batch API](./OpenAI%20Batch%20API/) | Exploring batch-style OpenAI API workflows. |
| [OpenAI FineTune API](./OpenAI%20FineTune%20API/) | Exploring model fine-tuning workflows through the OpenAI API. (Deprecated) |

### RAG & Retrieval

The repository also contains a dedicated set of RAG experiments covering different parts of the retrieval pipeline:

- [AI Simple RAG Implementation](./AI%20Simple%20RAG%20Implementation/)
- [AI Vector Databases](./AI%20Vector%20Databases/)
- [AI Rag Implementation (Embeddings)](./AI%20Rag%20Implementation%20(Embeddings)/)
- [AI Rag with LangChain](./AI%20Rag%20with%20LangChain/)
- [AI Rag Evaluation](./AI%20Rag%20Evaluation/)

These projects are kept in a compact section rather than mixed into the main application list because they form a coherent **RAG learning track** involving embeddings, vector databases, reranking, evaluation, and different implementation approaches.

## Running a Project

Projects use slightly different dependencies and entry points, so check the selected project's folder first.

For projects that include `pyproject.toml` and `uv.lock`, a typical setup is:

```bash
git clone https://github.com/Shaahmir/AI-Mini-Projects.git
cd AI-Mini-Projects
uv sync
```

Then open the project's notebook or run its Python entry point as appropriate.

Some projects require API keys or other environment variables. Configure those according to the files and instructions inside that project.

## Philosophy

This is a **learning-by-building repository** rather than a single production application. Some projects are tiny experiments, while others are more complete AI workflows. The emphasis is on exploring concepts, testing ideas, and turning what I learn into runnable code.

## Growing Over Time

More projects will be added as I explore:

- AI agents and tool use
- Multimodal AI
- LLM application patterns
- Local and hosted inference
- Evaluation and observability
- RAG and retrieval systems
- Model APIs and fine-tuning
- AI interfaces and automation

## License

This repository is licensed under the [MIT License](./LICENSE).
