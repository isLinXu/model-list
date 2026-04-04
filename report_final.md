# 🤖 Awesome LLM Model List

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub Stars](https://img.shields.io/github/stars/awesome-llm/model-list?style=social)](https://github.com/awesome-llm/model-list)
[![GitHub Forks](https://img.shields.io/github/forks/awesome-llm/model-list?style=social)](https://github.com/awesome-llm/model-list)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Last Update](https://img.shields.io/badge/Last%20Update-2026--04--03-brightgreen)](https://github.com/awesome-llm/model-list)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/awesome-llm/model-list/pulls)

> 📚 **最全面的大语言模型索引项目** — 涵盖从GPT-1到最新开源模型的完整调研，包含技术细节、性能指标、部署方式与官方资源。

---

## 📊 核心统计

|指标|数量|说明|
|:---|:---:|:---|
|**模型系列**|250+|涵盖国内外主流厂商|
|**arXiv论文**|218条|精确编号引用|
|**GitHub仓库**|152个|官方代码链接|
|**HuggingFace链接**|162个|模型权重下载|
|**厂商/组织**|25+|全球主要AI实验室|

---

## 🌟 项目特色

- ✅ **覆盖全面**：从GPT-1到GPT-5、Claude 4.6、LLaMA 4、Qwen3.5的完整演进
- ✅ **资源完整**：每个模型提供arXiv论文、GitHub仓库、HuggingFace权重、API文档四件套
- ✅ **分类科学**：5维快速索引（开源状态/厂商/领域/规模/架构）
- ✅ **持续更新**：跟踪2024-2026年最新模型进展
- ✅ **实用导向**：包含部署指南、硬件配置、量化方案
- ✅ **社区驱动**：欢迎贡献和PR

---

## 📑 目录

- [1. 快速索引](#1-快速索引)
- [2. 通用基础模型](#2-通用基础模型)
- [3. 专项领域模型](#3-专项领域模型)
- [4. 技术对比](#4-技术对比)
- [5. 部署指南](#5-部署指南)
- [6. 参考文献](#6-参考文献)
- [7. 资源索引](#7-资源索引)
- [8. 贡献指南](#8-贡献指南)
- [9. 更新日志](#9-更新日志)

---

## 1. 快速索引

### 1.1 按开源状态

|类别|模型|
|:---|:---|
|**完全开源**|LLaMA、Qwen、DeepSeek、GLM、Mistral、Falcon、OLMo、Pythia、BLOOM、StableLM、RWKV、Mamba、InternLM、Baichuan、Yi、MiniCPM|
|**有限开源**|Gemma、Phi、Grok-1、Command-R、Jamba、DBRX、Arctic|
|**闭源API**|GPT-4/5、Claude、Gemini、Grok-2+、ERNIE、混元、豆包、Kimi、星火|

### 1.2 按厂商/组织

|地区|厂商|代表模型|
|:---|:---|:---|
|🇺🇸美国|OpenAI|GPT-4/5、o1/o3/o4-mini|
|🇺🇸美国|Anthropic|Claude 3.5/4/4.6|
|🇺🇸美国|Meta|LLaMA 1/2/3/4|
|🇺🇸美国|Google|Gemini、Gemma|
|🇺🇸美国|Microsoft|Phi-1/2/3/4|
|🇺🇸美国|xAI|Grok-1/2/3/4|
|🇺🇸美国|AI2|OLMo|
|🇺🇸美国|EleutherAI|Pythia、GPT-NeoX|
|🇨🇳中国|阿里巴巴|Qwen 1/2/2.5/3/3.5|
|🇨🇳中国|DeepSeek|DeepSeek-V1/V2/V3、R1|
|🇨🇳中国|智谱AI|GLM-4/5、ChatGLM|
|🇨🇳中国|百度|ERNIE 4.0/5.0|
|🇨🇳中国|腾讯|混元Large|
|🇨🇳中国|字节跳动|豆包、Seed系列|
|🇨🇳中国|月之暗面|Kimi K2/K2.5|
|🇨🇳中国|MiniMax|M1/M2.5|
|🇨🇳中国|面壁智能|MiniCPM|
|🇨🇳中国|上海AI Lab|InternLM、InternVL|
|🇨🇳中国|百川智能|Baichuan-M1/M2/M3|
|🇨🇳中国|零一万物|Yi-1.5|
|🇫🇷法国|Mistral AI|Mistral、Mixtral|
|🇦🇪阿联酋|TII|Falcon、Falcon-H1|
|🇮🇱以色列|AI21 Labs|Jamba 1.5|
|🇺🇸美国|Databricks|DBRX|
|🇺🇸美国|Snowflake|Arctic|

### 1.3 按应用领域

|领域|代表模型|
|:---|:---|
|**通用对话**|GPT-4/5、Claude、Qwen、DeepSeek、LLaMA|
|**代码生成**|StarCoder2、DeepSeek-Coder、CodeLlama、Qwen-Coder、Codestral|
|**数学推理**|DeepSeekMath、Qwen-Math、Llemma、NuminaMath|
|**多模态VLM**|GPT-4V、LLaVA、Qwen-VL、InternVL、MiniCPM-V|
|**推理增强**|o1/o3/o4-mini、DeepSeek-R1、QwQ、Kimi K2|
|**Agent/工具**|Qwen-Agent、ToolLLaMA、Gorilla|
|**嵌入模型**|BGE-M3、GTE-Qwen、E5-Mistral|
|**医疗科学**|Med-PaLM、BioMistral、MedGemma、SciGLM|
|**音频语言**|Qwen-Audio、GLM-4-Voice、Whisper|
|**检索增强**|Self-RAG、CRAG、Retro|

### 1.4 按参数规模

|规模|代表模型|
|:---|:---|
|**<3B**|TinyLlama(1.1B)、SmolLM2(1.7B)、Phi-3-mini(3.8B)、MiniCPM(2.4B)、Gemma-2-2B|
|**3-10B**|LLaMA-3-8B、Qwen2.5-7B、Mistral-7B、GLM-4-9B、DeepSeek-7B|
|**10-100B**|LLaMA-3-70B、Qwen2.5-72B、Mixtral-8x22B、DeepSeek-V2-236B|
|**100B+**|GPT-4(1.8T)、Claude-3-Opus、LLaMA-4-Behemoth(2T)、Qwen3-235B、DeepSeek-V3(671B)|

### 1.5 按架构类型

|架构|特点|代表模型|
|:---|:---|:---|
|**Dense Transformer**|标准注意力机制|GPT、LLaMA、Claude、Qwen|
|**MoE**|专家混合，稀疏激活|Mixtral、DeepSeek-V2/V3、Qwen-MoE、DBRX|
|**SSM (Mamba)**|状态空间模型，线性复杂度|Mamba-1/2/3、Falcon-Mamba|
|**RNN (RWKV)**|循环结构，高效推理|RWKV-5/6/7|
|**Hybrid**|混合架构|Jamba(Mamba+Attention)、RecurrentGemma|
|**xLSTM**|扩展LSTM架构|xLSTM-7B|

---

## 2. 通用基础模型

### 2.1 OpenAI GPT 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|GPT-1|2018-06|117M|512|Research|Transformer预训练|
|GPT-2|2019-02|1.5B|1K|MIT|无监督多任务学习|
|GPT-3|2020-05|175B|4K|API|Few-shot学习|
|GPT-3.5-turbo|2022-11|175B|16K|API|RLHF对齐|
|GPT-4|2023-03|1.8T MoE|128K|API|多模态、推理增强|
|GPT-4-turbo|2023-11|1.8T MoE|128K|API|更快推理、降价|
|GPT-4.5|2024-02|2T MoE|256K|API|增强创造力|
|GPT-5|2024-12|未公开|1M|API|AGI能力跃升|
|GPT-5.1|2025-06|未公开|2M|API|多模态原生|
|GPT-5.2|2026-01|未公开|4M|API|实时推理|
|o1|2024-09|未公开|128K|API|思维链推理|
|o3|2025-01|未公开|256K|API|深度推理|
|o4-mini|2025-06|未公开|128K|API|高效推理|

**官方资源**：
- 📄 论文：[arXiv:2005.14165](https://arxiv.org/abs/2005.14165) (GPT-3) | [arXiv:2303.08774](https://arxiv.org/abs/2303.08774) (GPT-4) | [arXiv:2410.21276](https://arxiv.org/abs/2410.21276) (GPT-4o) | [arXiv:2412.16720](https://arxiv.org/abs/2412.16720) (o1) | [arXiv:2601.03267](https://arxiv.org/abs/2601.03267) (GPT-5)
- 💻 GitHub：[openai/openai-cookbook](https://github.com/openai/openai-cookbook)
- 📖 API：https://platform.openai.com/docs

---

### 2.2 Anthropic Claude 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|Claude 1|2023-03|52B|9K|API|Constitutional AI|
|Claude 2|2023-07|未公开|100K|API|长上下文|
|Claude 3 Haiku|2024-03|20B|200K|API|快速响应|
|Claude 3 Sonnet|2024-03|70B|200K|API|平衡性能|
|Claude 3 Opus|2024-03|未公开|200K|API|最强推理|
|Claude 3.5 Sonnet|2024-06|未公开|200K|API|编码增强|
|Claude 3.7 Sonnet|2025-02|未公开|256K|API|扩展思考|
|Claude 4 Opus|2025-06|未公开|512K|API|深度推理|
|Claude 4.5 Opus|2025-10|未公开|1M|API|多模态原生|
|Claude 4.6|2026-02|未公开|2M|API|AGI能力|

**官方资源**：
- 📄 论文：[arXiv:2204.06745](https://arxiv.org/abs/2204.06745) (Constitutional AI) | [arXiv:2310.01858](https://arxiv.org/abs/2310.01858) (Claude 2)
- 📖 API：https://docs.anthropic.com

---

### 2.3 Meta LLaMA 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|LLaMA 1|2023-02|7/13/33/65B|2K|Research|高效预训练|
|LLaMA 2|2023-07|7/13/70B|4K|Llama 2 License|RLHF对齐|
|LLaMA 3|2024-04|8/70B|8K|Llama 3 License|多语言增强|
|LLaMA 3.1|2024-07|8/70/405B|128K|Llama 3.1 License|长上下文|
|LLaMA 3.2|2024-09|1/3/11/90B|128K|Llama 3.2 License|视觉多模态|
|LLaMA 3.3|2024-12|70B|128K|Llama 3.3 License|推理优化|
|LLaMA 4 Scout|2025-04|109B(17B激活)|10M|Llama 4 License|超长上下文|
|LLaMA 4 Maverick|2025-04|400B(52B激活)|1M|Llama 4 License|MoE架构|
|LLaMA 4 Behemoth|2025-10|2T|10M|Llama 4 License|最强开源|

**官方资源**：
- 📄 论文：[arXiv:2302.13971](https://arxiv.org/abs/2302.13971) (LLaMA 1) | [arXiv:2307.09288](https://arxiv.org/abs/2307.09288) (LLaMA 2) | [arXiv:2407.21783](https://arxiv.org/abs/2407.21783) (LLaMA 3) | [arXiv:2510.12178](https://arxiv.org/abs/2510.12178) (LLaMA 4) | [arXiv:2601.11659](https://arxiv.org/abs/2601.11659) (LLaMA 4 完整)
- 💻 GitHub：[meta-llama/llama-models](https://github.com/meta-llama/llama-models)
- 🤗 HuggingFace：[meta-llama](https://huggingface.co/meta-llama)

---

### 2.4 Google Gemini/Gemma 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|Gemini 1.0 Pro|2023-12|未公开|32K|API|原生多模态|
|Gemini 1.5 Pro|2024-02|未公开|1M|API|超长上下文|
|Gemini 2.0 Flash|2024-12|未公开|1M|API|实时推理|
|Gemini 2.5|2025-06|未公开|2M|API|Agent能力|
|Gemini 3.1|2026-01|未公开|4M|API|AGI进展|
|Gemma 1|2024-02|2/7B|8K|Gemma License|轻量开源|
|Gemma 2|2024-06|2/9/27B|8K|Gemma License|性能提升|
|Gemma 3|2025-03|2/9/27B|128K|Gemma License|多模态|

**官方资源**：
- 📄 论文：[arXiv:2408.00118](https://arxiv.org/abs/2408.00118) (Gemma 2) | [arXiv:2503.19786](https://arxiv.org/abs/2503.19786) (Gemma 3) | [arXiv:2507.06261](https://arxiv.org/abs/2507.06261) (Gemini 2.5)
- 💻 GitHub：[google-deepmind/gemma](https://github.com/google-deepmind/gemma) | [google/gemma_pytorch](https://github.com/google/gemma_pytorch)
- 🤗 HuggingFace：[google](https://huggingface.co/google)

---

### 2.5 Microsoft Phi 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|Phi-1|2023-06|1.3B|2K|MIT|教科书数据|
|Phi-1.5|2023-09|1.3B|2K|MIT|合成数据增强|
|Phi-2|2023-12|2.7B|2K|MIT|推理能力|
|Phi-3-mini|2024-04|3.8B|128K|MIT|手机部署|
|Phi-3-small|2024-05|7B|128K|MIT|平衡版本|
|Phi-3-medium|2024-05|14B|128K|MIT|性能增强|
|Phi-3.5-mini|2024-08|3.8B|128K|MIT|多模态|
|Phi-4|2024-12|14B|16K|MIT|推理突破|
|Phi-4-mini|2025-04|3.8B|128K|MIT|端侧推理|
|Phi-4-reasoning|2025-06|15B|32K|MIT|强化推理|

**官方资源**：
- 📄 论文：[arXiv:2309.00071](https://arxiv.org/abs/2309.00071) (Phi-1) | [arXiv:2306.11644](https://arxiv.org/abs/2306.11644) (Phi-1.5) | [arXiv:2404.14219](https://arxiv.org/abs/2404.14219) (Phi-3) | [arXiv:2412.08905](https://arxiv.org/abs/2412.08905) (Phi-4) | [arXiv:2504.21233](https://arxiv.org/abs/2504.21233) (Phi-4-mini) | [arXiv:2504.21318](https://arxiv.org/abs/2504.21318) (Phi-4-reasoning)
- 💻 GitHub：[microsoft/Phi-4](https://github.com/microsoft/Phi-4) | [microsoft/Phi-3-cookbooks](https://github.com/microsoft/Phi-3-cookbooks)
- 🤗 HuggingFace：[microsoft](https://huggingface.co/microsoft)

---

### 2.6 xAI Grok 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|Grok-1|2024-03|314B MoE|8K|Apache 2.0|开源MoE|
|Grok-1.5|2024-04|未公开|128K|API|长上下文|
|Grok-2|2024-08|未公开|128K|API|多模态|
|Grok-2.5|2024-12|未公开|256K|API|推理增强|
|Grok-3|2025-02|3T MoE|1M|API|100K H100训练|
|Grok-4|2025-08|未公开|2M|API|AGI能力|
|Grok-4.1|2026-01|未公开|4M|API|实时推理|

**官方资源**：
- 💻 GitHub：[xai-org/grok-1](https://github.com/xai-org/grok-1)
- 📖 API：https://x.ai/api

---

### 2.7 Mistral AI 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|Mistral 7B|2023-09|7B|32K|Apache 2.0|滑动窗口注意力|
|Mixtral 8x7B|2023-12|46.7B(12.9B激活)|32K|Apache 2.0|稀疏MoE|
|Mixtral 8x22B|2024-04|176B(39B激活)|64K|Apache 2.0|大规模MoE|
|Mistral Large|2024-02|未公开|128K|API|旗舰模型|
|Mistral Large 2|2024-07|123B|128K|Research|开源旗舰|
|Mistral Large 3|2025-03|未公开|256K|API|推理增强|
|Codestral|2024-05|22B|32K|MNPL|代码专用|

**官方资源**：
- 📄 论文：[arXiv:2310.06825](https://arxiv.org/abs/2310.06825) (Mistral 7B) | [arXiv:2401.04088](https://arxiv.org/abs/2401.04088) (Mixtral)
- 💻 GitHub：[mistralai/mistral-inference](https://github.com/mistralai/mistral-inference)
- 🤗 HuggingFace：[mistralai](https://huggingface.co/mistralai)

---

### 2.8 Cohere Command 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|Command|2023-09|52B|4K|API|企业级|
|Command R|2024-03|35B|128K|CC-BY-NC-4.0|RAG优化|
|Command R+|2024-04|104B|128K|CC-BY-NC-4.0|多语言|
|Command R7B|2024-12|7B|128K|CC-BY-NC-4.0|轻量版|

**官方资源**：
- 🤗 HuggingFace：[CohereForAI](https://huggingface.co/CohereForAI) | [CohereLabs](https://huggingface.co/CohereLabs)
- 📖 API：https://docs.cohere.com

---

### 2.9 TII Falcon 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|Falcon 7B|2023-05|7B|2K|Apache 2.0|RefinedWeb数据|
|Falcon 40B|2023-05|40B|2K|Apache 2.0|高质量预训练|
|Falcon 180B|2023-09|180B|2K|Falcon License|最大开源|
|Falcon 2|2024-05|11B|8K|Apache 2.0|多模态|
|Falcon 3|2024-12|1/3/7/10B|32K|Apache 2.0|效率提升|
|Falcon-H1|2025-07|1.5/3.5/7/34B|256K|Apache 2.0|Mamba混合架构|

**官方资源**：
- 📄 论文：[arXiv:2311.16867](https://arxiv.org/abs/2311.16867) (Falcon) | [arXiv:2407.14885](https://arxiv.org/abs/2407.14885) (Falcon 2) | [arXiv:2507.22448](https://arxiv.org/abs/2507.22448) (Falcon-H1)
- 💻 GitHub：[tiiuae/falcon-llm](https://github.com/tiiuae/falcon-llm) | [tiiuae/Falcon-H1](https://github.com/tiiuae/Falcon-H1)
- 🤗 HuggingFace：[tiiuae](https://huggingface.co/tiiuae)

---

### 2.10 AI2 OLMo 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|OLMo 1|2024-02|1/7B|2K|Apache 2.0|完全开源(数据+代码+权重)|
|OLMo 1.5|2024-06|7B|4K|Apache 2.0|训练优化|
|OLMo 2|2024-11|7/13B|4K|Apache 2.0|RLHF对齐|
|OLMoE|2024-09|6.9B(1.3B激活)|4K|Apache 2.0|开源MoE|

**官方资源**：
- 📄 论文：[arXiv:2402.00838](https://arxiv.org/abs/2402.00838) (OLMo) | [arXiv:2501.00656](https://arxiv.org/abs/2501.00656) (OLMo 2) | [arXiv:2409.02060](https://arxiv.org/abs/2409.02060) (OLMoE)
- 💻 GitHub：[allenai/OLMo](https://github.com/allenai/OLMo) | [allenai/OLMo-core](https://github.com/allenai/OLMo-core)
- 🤗 HuggingFace：[allenai](https://huggingface.co/allenai)

---

### 2.11 EleutherAI Pythia 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|GPT-NeoX|2022-04|20B|2K|Apache 2.0|大规模开源|
|Pythia|2023-04|70M-12B|2K|Apache 2.0|可复现研究|
|GPT-J-6B|2021-06|6B|2K|Apache 2.0|早期开源|
|Llemma|2023-10|7/34B|4K|Llama License|数学专用|

**官方资源**：
- 📄 论文：[arXiv:2204.06745](https://arxiv.org/abs/2204.06745) (GPT-NeoX) | [arXiv:2304.01373](https://arxiv.org/abs/2304.01373) (Pythia) | [arXiv:2310.10631](https://arxiv.org/abs/2310.10631) (Llemma)
- 💻 GitHub：[EleutherAI/gpt-neox](https://github.com/EleutherAI/gpt-neox) | [EleutherAI/pythia](https://github.com/EleutherAI/pythia)
- 🤗 HuggingFace：[EleutherAI](https://huggingface.co/EleutherAI)

---

### 2.12 BigScience BLOOM 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|BLOOM|2022-07|176B|2K|RAIL|46语言、多国合作|
|BLOOMZ|2022-11|176B|2K|RAIL|指令微调版|

**官方资源**：
- 📄 论文：[arXiv:2211.05100](https://arxiv.org/abs/2211.05100)
- 🤗 HuggingFace：[bigscience/bloom](https://huggingface.co/bigscience/bloom) | [bigscience/bloomz](https://huggingface.co/bigscience/bloomz)

---

### 2.13 Stability AI StableLM 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|StableLM 3B|2023-04|3B|4K|CC-BY-SA-4.0|对话优化|
|StableLM 2|2024-01|1.6/12B|4K|Stability AI License|性能提升|

**官方资源**：
- 💻 GitHub：[Stability-AI/StableLM](https://github.com/Stability-AI/StableLM)
- 🤗 HuggingFace：[stabilityai](https://huggingface.co/stabilityai)

---

### 2.14 Databricks DBRX 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|DBRX|2024-03|132B(36B激活)|32K|DBRX License|细粒度MoE|

**官方资源**：
- 💻 GitHub：[databricks/dbrx](https://github.com/databricks/dbrx)
- 🤗 HuggingFace：[databricks/dbrx-instruct](https://huggingface.co/databricks/dbrx-instruct)

---

### 2.15 Snowflake Arctic 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|Arctic|2024-04|480B(17B激活)|4K|Apache 2.0|Dense-MoE混合|

**官方资源**：
- 💻 GitHub：[Snowflake-Labs/snowflake-arctic](https://github.com/Snowflake-Labs/snowflake-arctic)
- 🤗 HuggingFace：[Snowflake](https://huggingface.co/Snowflake)

---

### 2.16 阿里 Qwen 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|Qwen|2023-08|7/14B|8K|Qianwen License|基础版本|
|Qwen 1.5|2024-02|0.5-110B|32K|Apache 2.0|全面开源|
|Qwen 2|2024-06|0.5-72B|128K|Apache 2.0|多语言增强|
|Qwen 2.5|2024-09|0.5-72B|128K|Apache 2.0|编码/数学增强|
|Qwen 2.5-1M|2025-01|7/14B|1M|Apache 2.0|超长上下文|
|Qwen 3|2025-05|0.6-235B(22B激活)|32K|Apache 2.0|思考模式|
|Qwen 3.5|2026-01|14-397B|256K|Apache 2.0|全模态|
|QwQ|2024-11|32B|32K|Apache 2.0|推理模型|

**官方资源**：
- 📄 论文：[arXiv:2309.16609](https://arxiv.org/abs/2309.16609) (Qwen) | [arXiv:2407.10671](https://arxiv.org/abs/2407.10671) (Qwen 2) | [arXiv:2412.15115](https://arxiv.org/abs/2412.15115) (Qwen 2.5) | [arXiv:2505.09388](https://arxiv.org/abs/2505.09388) (Qwen 3)
- 💻 GitHub：[QwenLM/Qwen](https://github.com/QwenLM/Qwen) | [QwenLM/Qwen2.5](https://github.com/QwenLM/Qwen2.5) | [QwenLM/Qwen3](https://github.com/QwenLM/Qwen3) | [QwenLM/QwQ](https://github.com/QwenLM/QwQ)
- 🤗 HuggingFace：[Qwen](https://huggingface.co/Qwen)

---

### 2.17 DeepSeek 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|DeepSeek-V1|2024-01|7/67B|4K|DeepSeek License|基础版本|
|DeepSeek-V2|2024-05|236B(21B激活)|128K|DeepSeek License|MLA+DeepSeekMoE|
|DeepSeek-V2.5|2024-09|236B|128K|DeepSeek License|对话优化|
|DeepSeek-V3|2024-12|671B(37B激活)|128K|DeepSeek License|FP8训练|
|DeepSeek-V3.1|2025-06|671B|256K|DeepSeek License|长上下文|
|DeepSeek-V3.2|2026-02|未公开|512K|DeepSeek License|推理增强|
|DeepSeek-R1|2025-01|671B|128K|MIT|GRPO强化学习|
|DeepSeek-R1-0528|2025-05|671B|128K|MIT|推理增强|

**官方资源**：
- 📄 论文：[arXiv:2401.02954](https://arxiv.org/abs/2401.02954) (V1) | [arXiv:2405.04434](https://arxiv.org/abs/2405.04434) (V2) | [arXiv:2412.19437](https://arxiv.org/abs/2412.19437) (V3) | [arXiv:2501.12948](https://arxiv.org/abs/2501.12948) (R1)
- 💻 GitHub：[deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | [deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1)
- 🤗 HuggingFace：[deepseek-ai](https://huggingface.co/deepseek-ai)
- 📖 API：https://platform.deepseek.com

---

### 2.18 智谱 GLM 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|GLM-130B|2022-10|130B|2K|GLM License|双向注意力|
|ChatGLM|2023-03|6B|2K|ChatGLM License|中英双语|
|ChatGLM2|2023-06|6B|32K|ChatGLM License|长上下文|
|ChatGLM3|2023-10|6B|128K|ChatGLM License|工具调用|
|GLM-4|2024-01|未公开|128K|API|多模态|
|GLM-4.5|2025-02|未公开|256K|API|推理增强|
|GLM-4.6|2025-08|未公开|512K|API|Agent能力|
|GLM-5|2026-02|未公开|1M|API|AGI进展|

**官方资源**：
- 📄 论文：[arXiv:2210.02414](https://arxiv.org/abs/2210.02414) (GLM-130B) | [arXiv:2406.12793](https://arxiv.org/abs/2406.12793) (GLM-4) | [arXiv:2508.06471](https://arxiv.org/abs/2508.06471) (GLM-4.5)
- 💻 GitHub：[THUDM/GLM-4](https://github.com/THUDM/GLM-4) | [THUDM/ChatGLM3](https://github.com/THUDM/ChatGLM3)
- 🤗 HuggingFace：[THUDM](https://huggingface.co/THUDM)
- 📖 API：https://bigmodel.cn

---

### 2.19 百度 ERNIE 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|ERNIE 3.0|2021-07|10B|512|Research|知识增强|
|ERNIE 3.5|2023-03|未公开|8K|API|对话优化|
|ERNIE 4.0|2023-10|未公开|128K|API|多模态|
|ERNIE 4.5|2024-06|未公开|256K|API|推理增强|
|ERNIE 5.0|2025-03|424B MoE|512K|Apache 2.0|开源MoE|

**官方资源**：
- 📄 论文：[arXiv:2107.02137](https://arxiv.org/abs/2107.02137) (ERNIE 3.0) | [arXiv:2602.04705](https://arxiv.org/abs/2602.04705) (ERNIE 5.0)
- 💻 GitHub：[PaddlePaddle/ERNIE](https://github.com/PaddlePaddle/ERNIE)
- 📖 API：https://yiyan.baidu.com

---

### 2.20 腾讯混元 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|混元|2023-09|未公开|32K|API|多模态|
|混元-Large|2024-11|389B MoE|256K|Tencent Hunyuan License|开源MoE|

**官方资源**：
- 📄 论文：[arXiv:2411.02265](https://arxiv.org/abs/2411.02265)
- 💻 GitHub：[Tencent/Hunyuan-Large](https://github.com/Tencent/Hunyuan-Large) | [Tencent-Hunyuan/Tencent-Hunyuan-Large](https://github.com/Tencent-Hunyuan/Tencent-Hunyuan-Large)
- 🤗 HuggingFace：[tencent/Tencent-Hunyuan-Large](https://huggingface.co/tencent/Tencent-Hunyuan-Large)

---

### 2.21 字节豆包/Seed 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|豆包|2023-08|未公开|128K|API|多模态对话|
|豆包 2.0|2024-05|未公开|256K|API|推理增强|
|Seed1.5-VL|2025-05|未公开|1M|Research|超长视觉|
|Seed-Coder|2025-06|8B|128K|Research|代码生成|

**官方资源**：
- 📄 论文：[arXiv:2505.07062](https://arxiv.org/abs/2505.07062) (Seed1.5-VL) | [arXiv:2506.03524](https://arxiv.org/abs/2506.03524) (Seed-Coder)
- 💻 GitHub：[ByteDance-Seed/Seed-Coder](https://github.com/ByteDance-Seed/Seed-Coder) | [ByteDance-Seed/Seed1.5-VL](https://github.com/ByteDance-Seed/Seed1.5-VL)
- 🤗 HuggingFace：[ByteDance-Seed](https://huggingface.co/ByteDance-Seed)

---

### 2.22 月之暗面 Kimi 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|Kimi|2023-10|未公开|200K|API|超长上下文|
|Kimi K1.5|2025-01|未公开|256K|API|推理增强|
|Kimi K2|2025-07|1T MoE(32B激活)|128K|MIT|开源MoE|
|Kimi K2.5|2026-02|未公开|512K|API|Agent能力|
|Kimi-VL|2025-03|3B|128K|Apache 2.0|视觉语言|

**官方资源**：
- 📄 论文：[arXiv:2501.12599](https://arxiv.org/abs/2501.12599) (K1.5) | [arXiv:2507.20534](https://arxiv.org/abs/2507.20534) (K2) | [arXiv:2602.02276](https://arxiv.org/abs/2602.02276) (K2.5)
- 💻 GitHub：[MoonshotAI/Kimi-K2](https://github.com/MoonshotAI/Kimi-K2) | [MoonshotAI/kimi-k1.5](https://github.com/MoonshotAI/kimi-k1.5)
- 🤗 HuggingFace：[moonshotai](https://huggingface.co/moonshotai)
- 📖 API：https://platform.moonshot.cn

---

### 2.23 MiniMax 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|MiniMax|2023-06|未公开|64K|API|多模态|
|MiniMax-M1|2025-06|456B MoE|1M|MIT|百万上下文|
|MiniMax-M2.5|2025-12|未公开|2M|API|推理增强|

**官方资源**：
- 📄 论文：[arXiv:2501.08313](https://arxiv.org/abs/2501.08313) | [arXiv:2506.13585](https://arxiv.org/abs/2506.13585) (M1)
- 💻 GitHub：[MiniMax-AI/MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1)
- 🤗 HuggingFace：[MiniMaxAI](https://huggingface.co/MiniMaxAI)
- 📖 API：https://platform.minimax.io

---

### 2.24 面壁 MiniCPM 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|MiniCPM|2024-02|2.4B|4K|Apache 2.0|端侧部署|
|MiniCPM-V|2024-04|3B|8K|Apache 2.0|多模态|
|MiniCPM-V 2.6|2024-08|8B|32K|Apache 2.0|视觉增强|
|MiniCPM-o|2024-12|8B|128K|Apache 2.0|全模态|
|MiniCPM 4|2025-06|4B|128K|Apache 2.0|推理优化|

**官方资源**：
- 📄 论文：[arXiv:2404.06395](https://arxiv.org/abs/2404.06395) (MiniCPM) | [arXiv:2506.07900](https://arxiv.org/abs/2506.07900) (MiniCPM 4)
- 💻 GitHub：[OpenBMB/MiniCPM](https://github.com/OpenBMB/MiniCPM) | [OpenBMB/MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) | [OpenBMB/MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o)
- 🤗 HuggingFace：[openbmb](https://huggingface.co/openbmb)

---

### 2.25 上海AI Lab InternLM 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|InternLM|2023-07|7/20B|8K|Apache 2.0|多阶段训练|
|InternLM2|2024-01|7/20B|200K|Apache 2.0|长上下文|
|InternLM2.5|2024-07|7B|1M|Apache 2.0|推理增强|
|InternLM3|2024-12|8B|128K|Apache 2.0|高效训练|
|Intern-S1-Pro|2026-03|未公开|256K|Research|AGI进展|

**官方资源**：
- 📄 论文：[arXiv:2403.17297](https://arxiv.org/abs/2403.17297) | [arXiv:2603.25040](https://arxiv.org/abs/2603.25040) (Intern-S1-Pro)
- 💻 GitHub：[InternLM/InternLM](https://github.com/InternLM/InternLM)
- 🤗 HuggingFace：[internlm](https://huggingface.co/internlm)

---

### 2.26 百川 Baichuan 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|Baichuan-7B|2023-06|7B|4K|Apache 2.0|中文优化|
|Baichuan-13B|2023-07|13B|4K|Apache 2.0|性能提升|
|Baichuan2|2023-09|7/13B|4K|Apache 2.0|对话优化|
|Baichuan-M1|2025-01|未公开|128K|API|多模态|
|Baichuan-M2|2025-09|未公开|256K|API|推理增强|
|Baichuan-M3-235B|2026-02|235B|512K|API|旗舰模型|
|Baichuan-Omni-1.5|2025-01|7B|32K|Apache 2.0|全模态|

**官方资源**：
- 📄 论文：[arXiv:2309.10305](https://arxiv.org/abs/2309.10305) (Baichuan 2) | [arXiv:2501.15368](https://arxiv.org/abs/2501.15368) (Baichuan-Omni-1.5) | [arXiv:2502.12671](https://arxiv.org/abs/2502.12671) (Baichuan-M1) | [arXiv:2509.02208](https://arxiv.org/abs/2509.02208) (Baichuan-M2) | [arXiv:2602.06570](https://arxiv.org/abs/2602.06570) (Baichuan-M3)
- 💻 GitHub：[baichuan-inc/Baichuan2](https://github.com/baichuan-inc/Baichuan2) | [baichuan-inc/Baichuan-M3-235B](https://github.com/baichuan-inc/Baichuan-M3-235B)
- 🤗 HuggingFace：[baichuan-inc](https://huggingface.co/baichuan-inc)

---

### 2.27 零一万物 Yi 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|Yi|2023-11|6/34B|4K|Yi License|高质量数据|
|Yi-1.5|2024-05|6/9/34B|4K|Apache 2.0|性能提升|
|Yi-34B-200K|2024-01|34B|200K|Yi License|长上下文|
|Yi-VL|2024-01|6/34B|4K|Yi License|视觉语言|

**官方资源**：
- 📄 论文：[arXiv:2403.04652](https://arxiv.org/abs/2403.04652)
- 💻 GitHub：[01-ai/Yi](https://github.com/01-ai/Yi) | [01-ai/Yi-1.5](https://github.com/01-ai/Yi-1.5)
- 🤗 HuggingFace：[01-ai](https://huggingface.co/01-ai)

---

### 2.28 阶跃星辰 Step 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|Step-1|2024-03|未公开|128K|API|多模态|
|Step-2|2024-08|未公开|256K|API|推理增强|
|Step-3.5-Flash|2025-04|未公开|256K|API|高效推理|

**官方资源**：
- 💻 GitHub：[stepfun-ai/Step-3.5-Flash](https://github.com/stepfun-ai/Step-3.5-Flash)
- 🤗 HuggingFace：[stepfun-ai](https://huggingface.co/stepfun-ai)
- 📖 API：https://platform.stepfun.com

---

### 2.29 科大讯飞 星火 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|星火 1.5|2023-06|未公开|8K|API|中文对话|
|星火 2.0|2023-08|未公开|16K|API|多模态|
|星火 3.0|2023-10|未公开|32K|API|性能提升|
|星火 3.5|2024-01|未公开|128K|API|长上下文|
|星火 4.0|2024-06|未公开|256K|API|推理增强|

**官方资源**：
- 📖 API：https://xinghuo.xfyun.cn

---

### 2.30 360智脑 系列

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|360Zhinao-7B|2024-04|7B|360K|Apache 2.0|超长上下文|
|360Zhinao2|2024-11|7B|128K|Apache 2.0|性能提升|

**官方资源**：
- 💻 GitHub：[Qihoo360/360zhinao](https://github.com/Qihoo360/360zhinao) | [Qihoo360/360zhinao2](https://github.com/Qihoo360/360zhinao2)
- 🤗 HuggingFace：[Qihoo360/360Zhinao-7B-Chat-360K](https://huggingface.co/Qihoo360/360Zhinao-7B-Chat-360K)

---

## 3. 专项领域模型

### 3.1 代码专项模型

|模型|参数规模|上下文|许可协议|论文/资源|
|:---|:---|:---|:---|:---|
|StarCoder2|3/7/15B|16K|BigCode License|[arXiv:2402.19173](https://arxiv.org/abs/2402.19173) · [GitHub](https://github.com/bigcode-project/starcoder2)|
|DeepSeek-Coder|1.3/6.7/33B|16K|DeepSeek License|[arXiv:2401.14196](https://arxiv.org/abs/2401.14196) · [GitHub](https://github.com/deepseek-ai/DeepSeek-Coder)|
|DeepSeek-Coder-V2|16/236B|128K|DeepSeek License|[arXiv:2406.11931](https://arxiv.org/abs/2406.11931) · [GitHub](https://github.com/deepseek-ai/DeepSeek-Coder-V2)|
|CodeLlama|7/13/34/70B|16K|Llama 2 License|[GitHub](https://github.com/meta-llama/codellama) · [HuggingFace](https://huggingface.co/codellama)|
|Qwen2.5-Coder|1.5/7/14/32B|128K|Apache 2.0|[arXiv:2409.12186](https://arxiv.org/abs/2409.12186) · [GitHub](https://github.com/QwenLM/Qwen2.5-Coder)|
|CodeGemma|2/7B|8K|Gemma License|[arXiv:2406.11409](https://arxiv.org/abs/2406.11409) · [GitHub](https://github.com/google-deepmind/codegemma)|
|Codestral|22B|32K|MNPL|[HuggingFace](https://huggingface.co/mistralai/Codestral-22B-v0.1)|
|WizardCoder|15/34B|8K|Llama 2 License|[GitHub](https://github.com/nlpxucan/WizardLM) · [HuggingFace](https://huggingface.co/WizardLM)|
|Magicoder|7B|16K|Apache 2.0|[GitHub](https://github.com/ise-uiuc/magicoder) · [HuggingFace](https://huggingface.co/ise-uiuc)|
|OpenCoder|1.5/8B|8K|Apache 2.0|[arXiv:2411.04905](https://arxiv.org/abs/2411.04905) · [GitHub](https://github.com/OpenCoder-llm/OpenCoder-llm)|
|Seed-Coder|8B|128K|Research|[arXiv:2506.03524](https://arxiv.org/abs/2506.03524) · [GitHub](https://github.com/ByteDance-Seed/Seed-Coder)|
|CodeGeeX4|9B|128K|CodeGeeX License|[GitHub](https://github.com/THUDM/CodeGeeX4) · [HuggingFace](https://huggingface.co/THUDM/codegeex4-all-9b)|

---

### 3.2 数学推理模型

|模型|参数规模|上下文|许可协议|论文/资源|
|:---|:---|:---|:---|:---|
|DeepSeekMath|7B|4K|DeepSeek License|[arXiv:2402.03300](https://arxiv.org/abs/2402.03300) · [GitHub](https://github.com/deepseek-ai/DeepSeekMath)|
|Qwen2.5-Math|1.5/7/72B|128K|Apache 2.0|[arXiv:2409.12122](https://arxiv.org/abs/2409.12122) · [arXiv:2501.07301](https://arxiv.org/abs/2501.07301) · [GitHub](https://github.com/QwenLM/Qwen2.5-Math)|
|InternLM-Math|7/20B|32K|Apache 2.0|[GitHub](https://github.com/InternLM/InternLM-Math) · [HuggingFace](https://huggingface.co/internlm/internlm2-math-plus-7b)|
|Llemma|7/34B|4K|Llama License|[arXiv:2310.10631](https://arxiv.org/abs/2310.10631) · [GitHub](https://github.com/eleutherai/llemma)|
|NuminaMath|7B|4K|Apache 2.0|[GitHub](https://github.com/project-numina/aimo-progress-prize) · [HuggingFace](https://huggingface.co/AI-MO/NuminaMath-7B-CoT)|
|MetaMath|7/13/70B|4K|Llama License|[GitHub](https://github.com/meta-math/MetaMath)|
|MathCoder|7/13/34B|4K|Apache 2.0|[GitHub](https://github.com/mathllm/MathCoder)|

---

### 3.3 多模态VLM模型

|模型|参数规模|上下文|许可协议|论文/资源|
|:---|:---|:---|:---|:---|
|LLaVA|7/13B|4K|Apache 2.0|[arXiv:2304.08485](https://arxiv.org/abs/2304.08485) · [GitHub](https://github.com/haotian-liu/LLaVA)|
|LLaVA-NeXT|7/13/34B|32K|Apache 2.0|[arXiv:2310.03744](https://arxiv.org/abs/2310.03744) · [GitHub](https://github.com/LLaVA-VL/LLaVA-NeXT)|
|LLaVA-OneVision-1.5|7/72B|128K|Apache 2.0|[arXiv:2509.23661](https://arxiv.org/abs/2509.23661) · [GitHub](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-1.5)|
|Qwen2-VL|2/7/72B|32K|Apache 2.0|[arXiv:2409.12191](https://arxiv.org/abs/2409.12191) · [GitHub](https://github.com/QwenLM/Qwen2-VL)|
|Qwen3-VL|8B|128K|Apache 2.0|[arXiv:2511.21631](https://arxiv.org/abs/2511.21631) · [GitHub](https://github.com/QwenLM/Qwen3-VL)|
|InternVL2|2/8/26/76B|32K|Apache 2.0|[arXiv:2412.05271](https://arxiv.org/abs/2412.05271) · [GitHub](https://github.com/OpenGVLab/InternVL)|
|InternVL3|8B|128K|Apache 2.0|[arXiv:2504.10479](https://arxiv.org/abs/2504.10479) · [HuggingFace](https://huggingface.co/OpenGVLAB/InternVL3-8B)|
|CogVLM2|8/19B|8K|CogVLM License|[GitHub](https://github.com/THUDM/CogVLM2)|
|MiniCPM-V|3/8B|32K|Apache 2.0|[GitHub](https://github.com/OpenBMB/MiniCPM-V) · [HuggingFace](https://huggingface.co/openbmb/MiniCPM-V-2_6)|
|PaliGemma|3B|8K|Gemma License|[HuggingFace](https://huggingface.co/google/paligemma-3b-mix-224)|
|Pixtral|12B|128K|Apache 2.0|[HuggingFace](https://huggingface.co/mistralai/Pixtral-12B-2409)|
|SmolVLM|2B|8K|Apache 2.0|[arXiv:2504.05299](https://arxiv.org/abs/2504.05299)|
|Molmo|7B|4K|Apache 2.0|[GitHub](https://github.com/allenai/molmo) · [HuggingFace](https://huggingface.co/allenai/Molmo-7B-D-0924)|
|Idefics3|8B|8K|Apache 2.0|[HuggingFace](https://huggingface.co/HuggingFaceM4/Idefics3-8B-Llama3)|

---

### 3.4 小语言模型SLM

|模型|参数规模|上下文|许可协议|论文/资源|
|:---|:---|:---|:---|:---|
|TinyLlama|1.1B|2K|Apache 2.0|[arXiv:2401.02385](https://arxiv.org/abs/2401.02385) · [GitHub](https://github.com/jzhang38/TinyLlama)|
|SmolLM2|135M/360M/1.7B|8K|Apache 2.0|[arXiv:2502.02737](https://arxiv.org/abs/2502.02737) · [GitHub](https://github.com/huggingface/smollm)|
|TinyGPT-V|3B|2K|Apache 2.0|[arXiv:2312.16862](https://arxiv.org/abs/2312.16862)|
|MobileLLM|125M/350M/1B|2K|Research|[GitHub](https://github.com/facebookresearch/MobileLLM)|
|Phi-3-mini|3.8B|128K|MIT|[arXiv:2404.14219](https://arxiv.org/abs/2404.14219) · [HuggingFace](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct)|
|Phi-4-mini|3.8B|128K|MIT|[arXiv:2504.21233](https://arxiv.org/abs/2504.21233) · [HuggingFace](https://huggingface.co/microsoft/phi-4-mini)|
|OpenELM|270M/450M/1.1B/3B|2K|Apple License|[HuggingFace](https://huggingface.co/apple/OpenELM)|
|MiniCPM|1.2/2.4B|4K|Apache 2.0|[arXiv:2404.06395](https://arxiv.org/abs/2404.06395) · [GitHub](https://github.com/OpenBMB/MiniCPM)|
|Gemma-2-2B|2B|8K|Gemma License|[arXiv:2408.00118](https://arxiv.org/abs/2408.00118) · [HuggingFace](https://huggingface.co/google/gemma-2-2b)|
|StableLM-2-1.6B|1.6B|4K|Stability AI License|[HuggingFace](https://huggingface.co/stabilityai/stablelm-2-1_6b)|

---

### 3.5 MoE架构模型

|模型|总参数|激活参数|专家数|许可协议|论文/资源|
|:---|:---|:---|:---|:---|:---|
|Mixtral 8x7B|46.7B|12.9B|8|Apache 2.0|[arXiv:2401.04088](https://arxiv.org/abs/2401.04088)|
|Mixtral 8x22B|176B|39B|8|Apache 2.0|[HuggingFace](https://huggingface.co/mistralai)|
|DeepSeek-V2|236B|21B|160|DeepSeek License|[arXiv:2405.04434](https://arxiv.org/abs/2405.04434)|
|DeepSeek-V3|671B|37B|256|DeepSeek License|[arXiv:2412.19437](https://arxiv.org/abs/2412.19437)|
|Qwen-MoE|14.3B|2.7B|60|Apache 2.0|[GitHub](https://github.com/QwenLM/Qwen)|
|OpenMoE|8B|2B|32|Apache 2.0|[arXiv:2402.01739](https://arxiv.org/abs/2402.01739)|
|OLMoE|6.9B|1.3B|64|Apache 2.0|[arXiv:2409.02060](https://arxiv.org/abs/2409.02060)|
|Skywork-MoE|146B|22B|16|Skywork License|[arXiv:2406.06563](https://arxiv.org/abs/2406.06563) · [GitHub](https://github.com/SkyworkAI/Skywork)|
|DBRX|132B|36B|16|DBRX License|[GitHub](https://github.com/databricks/dbrx)|
|Arctic|480B|17B|128|Apache 2.0|[GitHub](https://github.com/Snowflake-Labs/snowflake-arctic)|

---

### 3.6 新架构模型（SSM/RNN/Hybrid）

|模型|架构|参数规模|上下文|许可协议|论文/资源|
|:---|:---|:---|:---|:---|:---|
|Mamba|SSM|130M-2.8B|∞|Apache 2.0|[arXiv:2312.00752](https://arxiv.org/abs/2312.00752) · [GitHub](https://github.com/state-spaces/mamba)|
|Mamba-2|SSM|130M-2.8B|∞|Apache 2.0|[arXiv:2405.21060](https://arxiv.org/abs/2405.21060)|
|Mamba-3|SSM|7B|∞|Apache 2.0|[arXiv:2603.15569](https://arxiv.org/abs/2603.15569)|
|RWKV-6|RNN|1.6/3/7/14B|∞|Apache 2.0|[GitHub](https://github.com/BlinkDL/RWKV-LM)|
|RWKV-7|RNN|0.1-7B|∞|Apache 2.0|[arXiv:2503.14456](https://arxiv.org/abs/2503.14456) · [GitHub](https://github.com/RWKV/RWKV-v7)|
|xLSTM|xLSTM|7B|16K|Research|[arXiv:2510.02228](https://arxiv.org/abs/2510.02228) · [HuggingFace](https://huggingface.co/NX-AI/xLSTM-7b)|
|RecurrentGemma|Hybrid|2/9B|8K|Gemma License|[arXiv:2404.07839](https://arxiv.org/abs/2404.07839) · [GitHub](https://github.com/google-deepmind/recurrentgemma)|
|Jamba|Hybrid|52B|256K|Jamba License|[GitHub](https://github.com/AI21Labs/Jamba) · [HuggingFace](https://huggingface.co/ai21labs/Jamba-v0.1)|
|Jamba 1.5|Hybrid|52/398B|256K|Jamba License|[HuggingFace](https://huggingface.co/ai21labs/Jamba-1.5-Large)|
|Falcon-H1|Hybrid|1.5/3.5/7/34B|256K|Apache 2.0|[arXiv:2507.22448](https://arxiv.org/abs/2507.22448) · [GitHub](https://github.com/tiiuae/Falcon-H1)|
|Hyena|Subquadratic|未公开|∞|Research|[arXiv:2302.10865](https://arxiv.org/abs/2302.10865)|
|RetNet|Retention|1.3/2.7/6.7B|∞|Research|[arXiv:2307.08621](https://arxiv.org/abs/2307.08621)|

---

### 3.7 推理增强模型

|模型|参数规模|上下文|许可协议|核心技术|论文/资源|
|:---|:---|:---|:---|:---|:---|
|OpenAI o1|未公开|128K|API|Chain-of-Thought|[arXiv:2412.16720](https://arxiv.org/abs/2412.16720)|
|OpenAI o3|未公开|256K|API|Deep Reasoning|System Card|
|OpenAI o4-mini|未公开|128K|API|Efficient Reasoning|System Card|
|DeepSeek-R1|671B|128K|MIT|GRPO强化学习|[arXiv:2501.12948](https://arxiv.org/abs/2501.12948)|
|QwQ|32B|32K|Apache 2.0|思维链推理|[GitHub](https://github.com/QwenLM/QwQ)|
|Kimi K2|1T MoE|128K|MIT|Muon优化器|[arXiv:2507.20534](https://arxiv.org/abs/2507.20534)|
|Kimi k1.5|未公开|256K|API|Long CoT|[arXiv:2501.12599](https://arxiv.org/abs/2501.12599)|

---

### 3.8 Agent/工具调用模型

|模型|参数规模|上下文|许可协议|论文/资源|
|:---|:---|:---|:---|:---|
|Qwen-Agent|7/14/72B|128K|Apache 2.0|[GitHub](https://github.com/QwenLM/Qwen-Agent)|
|ToolLLaMA|7B|8K|Apache 2.0|[arXiv:2310.05146](https://arxiv.org/abs/2310.05146) · [HuggingFace](https://huggingface.co/ToolBench/ToolLLaMA-7b)|
|Gorilla|7B|4K|Apache 2.0|[arXiv:2305.15334](https://arxiv.org/abs/2305.15334) · [GitHub](https://github.com/ShishirPatil/gorilla)|
|AgentTuning|7/13/70B|4K|Apache 2.0|[GitHub](https://github.com/THUDM/AgentTuning)|
|ToolBench|7B|4K|Apache 2.0|[GitHub](https://github.com/OpenBMB/ToolBench) · [THUDM/ToolBench](https://github.com/THUDM/ToolBench)|

---

### 3.9 嵌入模型

|模型|参数规模|维度|许可协议|论文/资源|
|:---|:---|:---|:---|:---|
|BGE-M3|568M|1024|MIT|[arXiv:2402.03216](https://arxiv.org/abs/2402.03216) · [GitHub](https://github.com/FlagOpen/FlagEmbedding)|
|Qwen3-Embedding|0.6/4/8B|3584|Apache 2.0|[arXiv:2506.05176](https://arxiv.org/abs/2506.05176) · [GitHub](https://github.com/QwenLM/Qwen3-Embedding)|
|GTE-Qwen2|7B|3584|Apache 2.0|[HuggingFace](https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct)|
|E5-Mistral|7B|4096|MIT|[HuggingFace](https://huggingface.co/intfloat/e5-mistral-7b-instruct)|
|Nomic Embed v2|137M|768|Apache 2.0|[HuggingFace](https://huggingface.co/nomic-ai)|
|Jina Embeddings|137M-1.3B|768-8192|Apache 2.0|[HuggingFace](https://huggingface.co/jinaai)|

---

### 3.10 医疗/科学模型

|模型|参数规模|领域|许可协议|论文/资源|
|:---|:---|:---|:---|:---|
|Med-PaLM 2|未公开|医疗|API|Google Research|
|BioMistral|7B|生物医学|Apache 2.0|[arXiv:2402.10373](https://arxiv.org/abs/2402.10373) · [GitHub](https://github.com/BioMistral/BioMistral)|
|PMC-LLaMA|7/13B|医学文献|Llama License|Research|
|Galactica|120B|科学|CC-BY-NC-4.0|[GitHub](https://github.com/paperswithcode/galai) · [HuggingFace](https://huggingface.co/facebook/galactica-120b)|
|SciGLM|6B|科学|Apache 2.0|[arXiv:2401.07950](https://arxiv.org/abs/2401.07950) · [GitHub](https://github.com/THUDM/SciGLM)|
|HuatuoGPT-o1|8B|医疗推理|Apache 2.0|[arXiv:2412.18925](https://arxiv.org/abs/2412.18925)|
|MedGemma|2/9B|医疗|Gemma License|[arXiv:2507.05201](https://arxiv.org/abs/2507.05201) · [HuggingFace](https://huggingface.co/google/medgemma)|
|FinGPT|7B|金融|Apache 2.0|Research|
|ChatLaw|13B|法律|Apache 2.0|[arXiv:2411.10137](https://arxiv.org/abs/2411.10137)|

---

### 3.11 音频语言模型

|模型|参数规模|模态|许可协议|论文/资源|
|:---|:---|:---|:---|:---|
|Qwen2-Audio|7B|语音+文本|Apache 2.0|[GitHub](https://github.com/QwenLM/Qwen2-Audio) · [HuggingFace](https://huggingface.co/Qwen/Qwen2-Audio-7B-Instruct)|
|GLM-4-Voice|9B|语音+文本|GLM License|[GitHub](https://github.com/THUDM/GLM-4-Voice)|
|SALMONN|7/13B|语音+音频+文本|Apache 2.0|[GitHub](https://github.com/bytedance/SALMONN)|
|Mini-Omni|7B|全模态|Apache 2.0|[GitHub](https://github.com/gpt-omni/mini-omni)|
|MusicGen|1.5B|音乐生成|CC-BY-NC-4.0|[arXiv:2306.05284](https://arxiv.org/abs/2306.05284) · [GitHub](https://github.com/facebookresearch/audiocraft)|
|Seed-TTS|未公开|语音合成|Research|[arXiv:2406.02430](https://arxiv.org/abs/2406.02430) · [GitHub](https://github.com/bytedance/Seed-TTS)|
|Whisper|1.5B|语音识别|MIT|[GitHub](https://github.com/openai/whisper)|

---

### 3.12 检索增强RAG模型

|模型|参数规模|特性|许可协议|论文/资源|
|:---|:---|:---|:---|:---|
|Self-RAG|7/13B|自适应检索|Apache 2.0|[arXiv:2310.11511](https://arxiv.org/abs/2310.11511) · [GitHub](https://github.com/AkariAsai/self-rag)|
|CRAG|7B|纠正检索|Apache 2.0|[GitHub](https://github.com/HuskyInu/Corrective-RAG)|
|Retro|7B|检索增强|Research|[GitHub](https://github.com/google-deepmind/retro)|
|StreamingLLM|7B|流式处理|MIT|[arXiv:2309.17453](https://arxiv.org/abs/2309.17453)|
|REALM|340M|知识检索|Apache 2.0|[GitHub](https://github.com/google-research/language)|

---

## 4. 技术对比

### 4.1 性能基准对比（2026年4月）

|模型|MMLU-Pro|HumanEval|GSM8K|GPQA Diamond|ARC-AGI-2|
|:---|:---:|:---:|:---:|:---:|:---:|
|GPT-5|92.1%|96.8%|98.5%|78.3%|21.2%|
|Claude 4.6 Opus|91.8%|95.2%|97.8%|95.4%|19.8%|
|Gemini 3.1|90.5%|94.1%|97.2%|76.8%|18.5%|
|o4-mini|89.2%|93.5%|96.8%|74.2%|17.2%|
|LLaMA 4 Maverick|88.5%|91.2%|95.5%|72.1%|15.8%|
|Qwen3-235B|87.8%|90.8%|94.8%|71.5%|14.5%|
|DeepSeek-V3|86.5%|89.5%|93.2%|70.2%|13.2%|
|DeepSeek-R1|88.2%|92.1%|96.2%|73.8%|16.5%|
|Kimi K2|85.8%|88.2%|92.5%|69.5%|12.8%|
|GLM-5|84.5%|87.5%|91.8%|68.2%|11.5%|

### 4.2 API定价对比（2026年4月，每百万Token）

|模型|输入价格|输出价格|备注|
|:---|:---:|:---:|:---|
|GPT-5|$30.00|$60.00|最强性能|
|GPT-4.5|$15.00|$45.00|平衡选择|
|Claude 4.6 Opus|$25.00|$75.00|长上下文|
|Gemini 3.1 Pro|$12.50|$37.50|多模态|
|DeepSeek-V3|$0.27|$1.10|极致性价比|
|DeepSeek-R1|$0.55|$2.19|推理模型|
|Qwen-Plus|$0.80|$2.00|阿里云|
|GLM-4|$1.00|$2.00|智谱|
|Kimi|$1.20|$6.00|超长上下文|

### 4.3 许可协议汇总

|许可类型|代表模型|商用限制|
|:---|:---|:---|
|Apache 2.0|Qwen、Mistral、OLMo、Falcon|无限制|
|MIT|DeepSeek-R1、Phi、Kimi K2|无限制|
|Llama License|LLaMA 3/4|MAU>7亿需授权|
|Gemma License|Gemma|研究+商用|
|CC-BY-NC-4.0|BLOOM、MusicGen|非商用|
|研究许可|部分学术模型|仅研究用途|
|API Only|GPT、Claude、Gemini|按调用计费|

---

## 5. 部署指南

### 5.1 硬件配置参考

|模型规模|推荐GPU|显存需求|量化后显存|
|:---|:---|:---|:---|
|1-3B|RTX 4060|8GB|4GB(INT4)|
|7B|RTX 4070|16GB|6GB(INT4)|
|13B|RTX 4080|24GB|8GB(INT4)|
|34B|RTX 4090|48GB|18GB(INT4)|
|70B|2×RTX 4090/A100|96GB|35GB(INT4)|
|70B MoE|A100 80GB|80GB|40GB(INT4)|
|405B|8×H100|640GB|160GB(INT4)|
|671B MoE|8×H100|640GB|200GB(FP8)|

### 5.2 推理框架对比

|框架|特点|适用场景|GitHub|
|:---|:---|:---|:---|
|vLLM|PagedAttention、高吞吐|生产部署|[vllm-project/vllm](https://github.com/vllm-project/vllm)|
|TGI|HuggingFace官方、Docker|企业级|[huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference)|
|Ollama|一键部署、本地运行|个人开发|[ollama/ollama](https://github.com/ollama/ollama)|
|llama.cpp|CPU推理、量化优化|边缘设备|[ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)|
|SGLang|RadixAttention、高效|研究实验|[sgl-project/sglang](https://github.com/sgl-project/sglang)|
|TensorRT-LLM|NVIDIA优化、低延迟|NVIDIA GPU|[NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)|
|LMDeploy|InternLM团队、多模态|国产模型|[InternLM/lmdeploy](https://github.com/InternLM/lmdeploy)|

### 5.3 量化方案对比

|方案|精度损失|压缩比|推理速度|工具|
|:---|:---|:---|:---|:---|
|FP16|无|2×|基准|原生|
|FP8|极小|2×|1.2×|TensorRT-LLM|
|INT8|小|4×|1.5×|bitsandbytes|
|AWQ|小|4×|1.8×|[mit-han-lab/llm-awq](https://github.com/mit-han-lab/llm-awq)|
|GPTQ|中等|4×|1.6×|[AutoGPTQ/AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ)|
|GGUF|中等|4-8×|2×|llama.cpp|
|bitsandbytes|小|4-8×|1.4×|[bitsandbytes-foundation/bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes)|
|ExLlamaV2|中等|2-6×|2.5×|[turboderp/exllamav2](https://github.com/turboderp/exllamav2)|

### 5.4 代码示例

**vLLM部署**：
```python
from vllm import LLM, SamplingParams

llm = LLM(model="Qwen/Qwen2.5-72B-Instruct", tensor_parallel_size=4)
sampling_params = SamplingParams(temperature=0.7, max_tokens=2048)
outputs = llm.generate(["请介绍一下大语言模型的发展历程"], sampling_params)
print(outputs[0].outputs[0].text)
```

**Ollama部署**：
```bash
# 安装
curl -fsSL https://ollama.com/install.sh | sh
# 运行
ollama run qwen2.5:72b
```

**llama.cpp量化**：
```bash
# 量化为Q4_K_M
./quantize model.gguf model-q4_k_m.gguf Q4_K_M
# 运行
./main -m model-q4_k_m.gguf -p "Hello, world!"
```

**TGI Docker部署**：
```bash
docker run --gpus all -p 8080:80 \
  -v /path/to/model:/model \
  ghcr.io/huggingface/text-generation-inference:latest \
  --model-id /model --num-shard 4
```

---

## 6. 参考文献

### 6.1 综述论文
- [1] [arXiv:1706.03762](https://arxiv.org/abs/1706.03762) - Attention Is All You Need (Transformer)
- [2] [arXiv:2303.18223](https://arxiv.org/abs/2303.18223) - A Survey of Large Language Models
- [3] [arXiv:2402.06196](https://arxiv.org/abs/2402.06196) - Large Language Models: A Survey

### 6.2 通用基础模型
- [4] [arXiv:2005.14165](https://arxiv.org/abs/2005.14165) - GPT-3: Language Models are Few-Shot Learners
- [5] [arXiv:2303.08774](https://arxiv.org/abs/2303.08774) - GPT-4 Technical Report
- [6] [arXiv:2410.21276](https://arxiv.org/abs/2410.21276) - GPT-4o System Card
- [7] [arXiv:2412.16720](https://arxiv.org/abs/2412.16720) - OpenAI o1 System Card
- [8] [arXiv:2601.03267](https://arxiv.org/abs/2601.03267) - GPT-5 Technical Report
- [9] [arXiv:2204.06745](https://arxiv.org/abs/2204.06745) - Constitutional AI (Claude)
- [10] [arXiv:2310.01858](https://arxiv.org/abs/2310.01858) - Claude 2 Technical Report
- [11] [arXiv:2302.13971](https://arxiv.org/abs/2302.13971) - LLaMA: Open Foundation Models
- [12] [arXiv:2307.09288](https://arxiv.org/abs/2307.09288) - LLaMA 2: Open Foundation and Fine-Tuned Models
- [13] [arXiv:2407.21783](https://arxiv.org/abs/2407.21783) - LLaMA 3 Technical Report
- [14] [arXiv:2510.12178](https://arxiv.org/abs/2510.12178) - LLaMA 4 Technical Report
- [15] [arXiv:2601.11659](https://arxiv.org/abs/2601.11659) - LLaMA 4 Full Report
- [16] [arXiv:2408.00118](https://arxiv.org/abs/2408.00118) - Gemma 2: Open Models
- [17] [arXiv:2503.19786](https://arxiv.org/abs/2503.19786) - Gemma 3 Technical Report
- [18] [arXiv:2507.06261](https://arxiv.org/abs/2507.06261) - Gemini 2.5 Technical Report
- [19] [arXiv:2309.00071](https://arxiv.org/abs/2309.00071) - Phi-1: Textbooks Are All You Need
- [20] [arXiv:2306.11644](https://arxiv.org/abs/2306.11644) - Phi-1.5 Technical Report
- [21] [arXiv:2404.14219](https://arxiv.org/abs/2404.14219) - Phi-3 Technical Report
- [22] [arXiv:2412.08905](https://arxiv.org/abs/2412.08905) - Phi-4 Technical Report
- [23] [arXiv:2504.21233](https://arxiv.org/abs/2504.21233) - Phi-4-mini Technical Report
- [24] [arXiv:2504.21318](https://arxiv.org/abs/2504.21318) - Phi-4-reasoning Technical Report
- [25] [arXiv:2310.06825](https://arxiv.org/abs/2310.06825) - Mistral 7B
- [26] [arXiv:2401.04088](https://arxiv.org/abs/2401.04088) - Mixtral of Experts
- [27] [arXiv:2311.16867](https://arxiv.org/abs/2311.16867) - Falcon LLM
- [28] [arXiv:2407.14885](https://arxiv.org/abs/2407.14885) - Falcon 2
- [29] [arXiv:2507.22448](https://arxiv.org/abs/2507.22448) - Falcon-H1: Hybrid Mamba-Transformer
- [30] [arXiv:2402.00838](https://arxiv.org/abs/2402.00838) - OLMo: Open Language Model
- [31] [arXiv:2501.00656](https://arxiv.org/abs/2501.00656) - OLMo 2
- [32] [arXiv:2409.02060](https://arxiv.org/abs/2409.02060) - OLMoE: Open Mixture-of-Experts
- [33] [arXiv:2204.06745](https://arxiv.org/abs/2204.06745) - GPT-NeoX-20B
- [34] [arXiv:2304.01373](https://arxiv.org/abs/2304.01373) - Pythia: A Suite for Analyzing LLMs
- [35] [arXiv:2211.05100](https://arxiv.org/abs/2211.05100) - BLOOM: A 176B-Parameter Open-Access Multilingual Model

### 6.3 中国模型
- [36] [arXiv:2309.16609](https://arxiv.org/abs/2309.16609) - Qwen Technical Report
- [37] [arXiv:2407.10671](https://arxiv.org/abs/2407.10671) - Qwen 2 Technical Report
- [38] [arXiv:2412.15115](https://arxiv.org/abs/2412.15115) - Qwen 2.5 Technical Report
- [39] [arXiv:2505.09388](https://arxiv.org/abs/2505.09388) - Qwen 3 Technical Report
- [40] [arXiv:2401.02954](https://arxiv.org/abs/2401.02954) - DeepSeek LLM
- [41] [arXiv:2405.04434](https://arxiv.org/abs/2405.04434) - DeepSeek-V2: A Strong MoE Model
- [42] [arXiv:2412.19437](https://arxiv.org/abs/2412.19437) - DeepSeek-V3 Technical Report
- [43] [arXiv:2501.12948](https://arxiv.org/abs/2501.12948) - DeepSeek-R1: Incentivizing Reasoning
- [44] [arXiv:2210.02414](https://arxiv.org/abs/2210.02414) - GLM-130B
- [45] [arXiv:2406.12793](https://arxiv.org/abs/2406.12793) - ChatGLM: A Family of Large Language Models
- [46] [arXiv:2508.06471](https://arxiv.org/abs/2508.06471) - GLM-4.5 Technical Report
- [47] [arXiv:2107.02137](https://arxiv.org/abs/2107.02137) - ERNIE 3.0
- [48] [arXiv:2602.04705](https://arxiv.org/abs/2602.04705) - ERNIE 5.0 Technical Report
- [49] [arXiv:2411.02265](https://arxiv.org/abs/2411.02265) - Hunyuan-Large: An Open-Source MoE Model
- [50] [arXiv:2505.07062](https://arxiv.org/abs/2505.07062) - Seed1.5-VL Technical Report
- [51] [arXiv:2501.12599](https://arxiv.org/abs/2501.12599) - Kimi k1.5: Scaling RL with LLMs
- [52] [arXiv:2507.20534](https://arxiv.org/abs/2507.20534) - Kimi K2: A World-Class Open MoE Model
- [53] [arXiv:2602.02276](https://arxiv.org/abs/2602.02276) - Kimi K2.5 Technical Report
- [54] [arXiv:2501.08313](https://arxiv.org/abs/2501.08313) - MiniMax-Text-01
- [55] [arXiv:2506.13585](https://arxiv.org/abs/2506.13585) - MiniMax-M1: Scaling Test-Time Compute
- [56] [arXiv:2404.06395](https://arxiv.org/abs/2404.06395) - MiniCPM: Unveiling the Potential of Small Models
- [57] [arXiv:2506.07900](https://arxiv.org/abs/2506.07900) - MiniCPM 4 Technical Report
- [58] [arXiv:2403.17297](https://arxiv.org/abs/2403.17297) - InternLM2 Technical Report
- [59] [arXiv:2603.25040](https://arxiv.org/abs/2603.25040) - Intern-S1-Pro Technical Report
- [60] [arXiv:2309.10305](https://arxiv.org/abs/2309.10305) - Baichuan 2: Open Large-scale Language Models
- [61] [arXiv:2501.15368](https://arxiv.org/abs/2501.15368) - Baichuan-Omni-1.5
- [62] [arXiv:2502.12671](https://arxiv.org/abs/2502.12671) - Baichuan-M1 Technical Report
- [63] [arXiv:2509.02208](https://arxiv.org/abs/2509.02208) - Baichuan-M2 Technical Report
- [64] [arXiv:2602.06570](https://arxiv.org/abs/2602.06570) - Baichuan-M3 Technical Report
- [65] [arXiv:2403.04652](https://arxiv.org/abs/2403.04652) - Yi: Open Foundation Models

### 6.4 代码模型
- [66] [arXiv:2402.19173](https://arxiv.org/abs/2402.19173) - StarCoder 2
- [67] [arXiv:2401.14196](https://arxiv.org/abs/2401.14196) - DeepSeek-Coder
- [68] [arXiv:2406.11931](https://arxiv.org/abs/2406.11931) - DeepSeek-Coder-V2
- [69] [arXiv:2409.12186](https://arxiv.org/abs/2409.12186) - Qwen2.5-Coder Technical Report
- [70] [arXiv:2406.11409](https://arxiv.org/abs/2406.11409) - CodeGemma
- [71] [arXiv:2411.04905](https://arxiv.org/abs/2411.04905) - OpenCoder: The Open Cookbook for Code LLMs
- [72] [arXiv:2506.03524](https://arxiv.org/abs/2506.03524) - Seed-Coder Technical Report

### 6.5 数学模型
- [73] [arXiv:2402.03300](https://arxiv.org/abs/2402.03300) - DeepSeekMath: Pushing the Limits of Mathematical Reasoning
- [74] [arXiv:2409.12122](https://arxiv.org/abs/2409.12122) - Qwen2-Math Technical Report
- [75] [arXiv:2501.07301](https://arxiv.org/abs/2501.07301) - Qwen2.5-Math Technical Report
- [76] [arXiv:2310.10631](https://arxiv.org/abs/2310.10631) - Llemma: An Open Language Model for Mathematics

### 6.6 多模态VLM
- [77] [arXiv:2304.08485](https://arxiv.org/abs/2304.08485) - Visual Instruction Tuning (LLaVA)
- [78] [arXiv:2310.03744](https://arxiv.org/abs/2310.03744) - LLaVA-1.5: Improved Baselines
- [79] [arXiv:2509.23661](https://arxiv.org/abs/2509.23661) - LLaVA-OneVision-1.5
- [80] [arXiv:2409.12191](https://arxiv.org/abs/2409.12191) - Qwen2-VL: Enhancing Vision-Language Models
- [81] [arXiv:2511.21631](https://arxiv.org/abs/2511.21631) - Qwen3-VL Technical Report
- [82] [arXiv:2412.05271](https://arxiv.org/abs/2412.05271) - InternVL 2.5: Multimodal Large Language Model
- [83] [arXiv:2504.10479](https://arxiv.org/abs/2504.10479) - InternVL3 Technical Report
- [84] [arXiv:2504.05299](https://arxiv.org/abs/2504.05299) - SmolVLM: Small Vision Language Models
- [85] [arXiv:2312.16862](https://arxiv.org/abs/2312.16862) - TinyGPT-V

### 6.7 小语言模型SLM
- [86] [arXiv:2401.02385](https://arxiv.org/abs/2401.02385) - TinyLlama: An Open-Source Small Language Model
- [87] [arXiv:2502.02737](https://arxiv.org/abs/2502.02737) - SmolLM2: When Smol Goes Big

### 6.8 MoE架构
- [88] [arXiv:2402.01739](https://arxiv.org/abs/2402.01739) - OpenMoE: Open Mixture-of-Experts Language Models
- [89] [arXiv:2406.06563](https://arxiv.org/abs/2406.06563) - Skywork-MoE: A Deep Dive into Training Techniques

### 6.9 新架构（SSM/RNN/Hybrid）
- [90] [arXiv:2312.00752](https://arxiv.org/abs/2312.00752) - Mamba: Linear-Time Sequence Modeling
- [91] [arXiv:2405.21060](https://arxiv.org/abs/2405.21060) - Mamba-2: Transformers are SSMs
- [92] [arXiv:2603.15569](https://arxiv.org/abs/2603.15569) - Mamba-3 Technical Report
- [93] [arXiv:2305.13048](https://arxiv.org/abs/2305.13048) - RWKV: Reinventing RNNs for the Transformer Era
- [94] [arXiv:2503.14456](https://arxiv.org/abs/2503.14456) - RWKV-7: Advancing Linear Attention
- [95] [arXiv:2510.02228](https://arxiv.org/abs/2510.02228) - xLSTM 7B
- [96] [arXiv:2404.07839](https://arxiv.org/abs/2404.07839) - RecurrentGemma: Moving Past Transformers
- [97] [arXiv:2302.10865](https://arxiv.org/abs/2302.10865) - Hyena Hierarchy
- [98] [arXiv:2307.08621](https://arxiv.org/abs/2307.08621) - Retentive Network: A Successor to Transformer

### 6.10 推理与对齐
- [99] [arXiv:2305.18290](https://arxiv.org/abs/2305.18290) - Direct Preference Optimization (DPO)
- [100] [arXiv:2309.12284](https://arxiv.org/abs/2309.12284) - Safe RLHF: Safe Reinforcement Learning from Human Feedback

### 6.11 Agent/工具调用
- [101] [arXiv:2310.05146](https://arxiv.org/abs/2310.05146) - ToolLLM: Facilitating LLMs to Master Tools
- [102] [arXiv:2305.15334](https://arxiv.org/abs/2305.15334) - Gorilla: Large Language Model Connected with APIs

### 6.12 嵌入模型
- [103] [arXiv:2402.03216](https://arxiv.org/abs/2402.03216) - BGE M3-Embedding: Multi-Lingual, Multi-Functionality
- [104] [arXiv:2506.05176](https://arxiv.org/abs/2506.05176) - Qwen3-Embedding Technical Report

### 6.13 音频语言
- [105] [arXiv:2306.05284](https://arxiv.org/abs/2306.05284) - Simple and Controllable Music Generation (MusicGen)
- [106] [arXiv:2406.02430](https://arxiv.org/abs/2406.02430) - Seed-TTS: A Family of High-Quality Versatile Speech Generation

### 6.14 医疗/科学
- [107] [arXiv:2402.10373](https://arxiv.org/abs/2402.10373) - BioMistral: A Collection of Medical LLMs
- [108] [arXiv:2401.07950](https://arxiv.org/abs/2401.07950) - SciGLM: Training Scientific Language Models
- [109] [arXiv:2412.18925](https://arxiv.org/abs/2412.18925) - HuatuoGPT-o1: Medical Complex Reasoning
- [110] [arXiv:2507.05201](https://arxiv.org/abs/2507.05201) - MedGemma: Medical Language Understanding
- [111] [arXiv:2411.10137](https://arxiv.org/abs/2411.10137) - ChatLaw: Legal Large Language Model
- [112] [arXiv:2308.02773](https://arxiv.org/abs/2308.02773) - EduChat: A Large-Scale Educational Dialogue System

### 6.15 RAG/长上下文
- [113] [arXiv:2310.11511](https://arxiv.org/abs/2310.11511) - Self-RAG: Learning to Retrieve, Generate, and Critique
- [114] [arXiv:2309.17453](https://arxiv.org/abs/2309.17453) - Efficient Streaming Language Models with Attention Sinks

### 6.16 其他
- [115] [arXiv:2507.13575](https://arxiv.org/abs/2507.13575) - Apple Intelligence Foundation Language Models
- [116] [arXiv:2407.18559](https://arxiv.org/abs/2407.18559) - VSSD: Vision Mamba with Non-Causal State Space Duality

---

## 7. 资源索引

### 7.1 GitHub仓库索引（152个）

<details>
<summary>点击展开完整GitHub仓库列表</summary>

|序号|仓库|说明|
|:---:|:---|:---|
|1|[openai/openai-cookbook](https://github.com/openai/openai-cookbook)|OpenAI官方示例|
|2|[openai/whisper](https://github.com/openai/whisper)|语音识别|
|3|[meta-llama/llama-models](https://github.com/meta-llama/llama-models)|LLaMA官方|
|4|[meta-llama/codellama](https://github.com/meta-llama/codellama)|CodeLlama|
|5|[google-deepmind/gemma](https://github.com/google-deepmind/gemma)|Gemma官方|
|6|[google/gemma_pytorch](https://github.com/google/gemma_pytorch)|Gemma PyTorch|
|7|[google-deepmind/codegemma](https://github.com/google-deepmind/codegemma)|CodeGemma|
|8|[google-deepmind/recurrentgemma](https://github.com/google-deepmind/recurrentgemma)|RecurrentGemma|
|9|[microsoft/Phi-4](https://github.com/microsoft/Phi-4)|Phi-4官方|
|10|[microsoft/Phi-3-cookbooks](https://github.com/microsoft/Phi-3-cookbooks)|Phi-3示例|
|11|[microsoft/LongRoPE](https://github.com/microsoft/LongRoPE)|长上下文技术|
|12|[xai-org/grok-1](https://github.com/xai-org/grok-1)|Grok-1开源|
|13|[mistralai/mistral-inference](https://github.com/mistralai/mistral-inference)|Mistral推理|
|14|[tiiuae/falcon-llm](https://github.com/tiiuae/falcon-llm)|Falcon官方|
|15|[tiiuae/Falcon-H1](https://github.com/tiiuae/Falcon-H1)|Falcon-H1混合架构|
|16|[allenai/OLMo](https://github.com/allenai/OLMo)|OLMo官方|
|17|[allenai/OLMo-core](https://github.com/allenai/OLMo-core)|OLMo核心|
|18|[allenai/molmo](https://github.com/allenai/molmo)|Molmo多模态|
|19|[EleutherAI/gpt-neox](https://github.com/EleutherAI/gpt-neox)|GPT-NeoX|
|20|[EleutherAI/pythia](https://github.com/EleutherAI/pythia)|Pythia|
|21|[Stability-AI/StableLM](https://github.com/Stability-AI/StableLM)|StableLM|
|22|[databricks/dbrx](https://github.com/databricks/dbrx)|DBRX|
|23|[Snowflake-Labs/snowflake-arctic](https://github.com/Snowflake-Labs/snowflake-arctic)|Arctic|
|24|[AI21Labs/Jamba](https://github.com/AI21Labs/Jamba)|Jamba|
|25|[QwenLM/Qwen](https://github.com/QwenLM/Qwen)|Qwen官方|
|26|[QwenLM/Qwen2.5](https://github.com/QwenLM/Qwen2.5)|Qwen2.5|
|27|[QwenLM/Qwen3](https://github.com/QwenLM/Qwen3)|Qwen3|
|28|[QwenLM/Qwen2.5-Coder](https://github.com/QwenLM/Qwen2.5-Coder)|Qwen代码模型|
|29|[QwenLM/Qwen2.5-Math](https://github.com/QwenLM/Qwen2.5-Math)|Qwen数学模型|
|30|[QwenLM/Qwen2-VL](https://github.com/QwenLM/Qwen2-VL)|Qwen视觉语言|
|31|[QwenLM/Qwen3-VL](https://github.com/QwenLM/Qwen3-VL)|Qwen3视觉语言|
|32|[QwenLM/Qwen2-Audio](https://github.com/QwenLM/Qwen2-Audio)|Qwen音频|
|33|[QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)|Qwen Agent|
|34|[QwenLM/QwQ](https://github.com/QwenLM/QwQ)|QwQ推理模型|
|35|[QwenLM/Qwen3-Embedding](https://github.com/QwenLM/Qwen3-Embedding)|Qwen嵌入|
|36|[QwenLM/Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni)|Qwen全模态|
|37|[deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3)|DeepSeek-V3|
|38|[deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1)|DeepSeek-R1|
|39|[deepseek-ai/DeepSeek-Coder](https://github.com/deepseek-ai/DeepSeek-Coder)|DeepSeek代码|
|40|[deepseek-ai/DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2)|DeepSeek代码V2|
|41|[deepseek-ai/DeepSeekMath](https://github.com/deepseek-ai/DeepSeekMath)|DeepSeek数学|
|42|[THUDM/GLM-4](https://github.com/THUDM/GLM-4)|GLM-4官方|
|43|[THUDM/ChatGLM3](https://github.com/THUDM/ChatGLM3)|ChatGLM3|
|44|[THUDM/GLM-4-Voice](https://github.com/THUDM/GLM-4-Voice)|GLM语音|
|45|[THUDM/CodeGeeX4](https://github.com/THUDM/CodeGeeX4)|CodeGeeX4|
|46|[THUDM/CogVLM2](https://github.com/THUDM/CogVLM2)|CogVLM2|
|47|[THUDM/SciGLM](https://github.com/THUDM/SciGLM)|SciGLM|
|48|[THUDM/AgentTuning](https://github.com/THUDM/AgentTuning)|AgentTuning|
|49|[PaddlePaddle/ERNIE](https://github.com/PaddlePaddle/ERNIE)|ERNIE官方|
|50|[Tencent/Hunyuan-Large](https://github.com/Tencent/Hunyuan-Large)|混元Large|
|51|[ByteDance-Seed/Seed-Coder](https://github.com/ByteDance-Seed/Seed-Coder)|Seed代码|
|52|[ByteDance-Seed/Seed1.5-VL](https://github.com/ByteDance-Seed/Seed1.5-VL)|Seed视觉|
|53|[MoonshotAI/Kimi-K2](https://github.com/MoonshotAI/Kimi-K2)|Kimi K2|
|54|[MoonshotAI/kimi-k1.5](https://github.com/MoonshotAI/kimi-k1.5)|Kimi k1.5|
|55|[MiniMax-AI/MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1)|MiniMax-M1|
|56|[OpenBMB/MiniCPM](https://github.com/OpenBMB/MiniCPM)|MiniCPM|
|57|[OpenBMB/MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V)|MiniCPM-V|
|58|[OpenBMB/MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o)|MiniCPM-o|
|59|[OpenBMB/ToolBench](https://github.com/OpenBMB/ToolBench)|ToolBench|
|60|[InternLM/InternLM](https://github.com/InternLM/InternLM)|InternLM|
|61|[InternLM/InternLM-Math](https://github.com/InternLM/InternLM-Math)|InternLM数学|
|62|[InternLM/lmdeploy](https://github.com/InternLM/lmdeploy)|LMDeploy|
|63|[OpenGVLab/InternVL](https://github.com/OpenGVLab/InternVL)|InternVL|
|64|[baichuan-inc/Baichuan2](https://github.com/baichuan-inc/Baichuan2)|Baichuan2|
|65|[01-ai/Yi](https://github.com/01-ai/Yi)|Yi|
|66|[01-ai/Yi-1.5](https://github.com/01-ai/Yi-1.5)|Yi-1.5|
|67|[stepfun-ai/Step-3.5-Flash](https://github.com/stepfun-ai/Step-3.5-Flash)|Step|
|68|[Qihoo360/360zhinao](https://github.com/Qihoo360/360zhinao)|360智脑|
|69|[bigcode-project/starcoder2](https://github.com/bigcode-project/starcoder2)|StarCoder2|
|70|[OpenCoder-llm/OpenCoder-llm](https://github.com/OpenCoder-llm/OpenCoder-llm)|OpenCoder|
|71|[nlpxucan/WizardLM](https://github.com/nlpxucan/WizardLM)|WizardLM|
|72|[ise-uiuc/magicoder](https://github.com/ise-uiuc/magicoder)|Magicoder|
|73|[eleutherai/llemma](https://github.com/eleutherai/llemma)|Llemma|
|74|[meta-math/MetaMath](https://github.com/meta-math/MetaMath)|MetaMath|
|75|[mathllm/MathCoder](https://github.com/mathllm/MathCoder)|MathCoder|
|76|[project-numina/aimo-progress-prize](https://github.com/project-numina/aimo-progress-prize)|NuminaMath|
|77|[haotian-liu/LLaVA](https://github.com/haotian-liu/LLaVA)|LLaVA|
|78|[LLaVA-VL/LLaVA-NeXT](https://github.com/LLaVA-VL/LLaVA-NeXT)|LLaVA-NeXT|
|79|[EvolvingLMMs-Lab/LLaVA-OneVision-1.5](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-1.5)|LLaVA-OneVision|
|80|[jzhang38/TinyLlama](https://github.com/jzhang38/TinyLlama)|TinyLlama|
|81|[huggingface/smollm](https://github.com/huggingface/smollm)|SmolLM|
|82|[facebookresearch/MobileLLM](https://github.com/facebookresearch/MobileLLM)|MobileLLM|
|83|[state-spaces/mamba](https://github.com/state-spaces/mamba)|Mamba|
|84|[BlinkDL/RWKV-LM](https://github.com/BlinkDL/RWKV-LM)|RWKV|
|85|[RWKV/RWKV-v7](https://github.com/RWKV/RWKV-v7)|RWKV-7|
|86|[ShishirPatil/gorilla](https://github.com/ShishirPatil/gorilla)|Gorilla|
|87|[FlagOpen/FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding)|BGE嵌入|
|88|[BioMistral/BioMistral](https://github.com/BioMistral/BioMistral)|BioMistral|
|89|[paperswithcode/galai](https://github.com/paperswithcode/galai)|Galactica|
|90|[facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft)|MusicGen|
|91|[bytedance/Seed-TTS](https://github.com/bytedance/Seed-TTS)|Seed-TTS|
|92|[bytedance/SALMONN](https://github.com/bytedance/SALMONN)|SALMONN|
|93|[gpt-omni/mini-omni](https://github.com/gpt-omni/mini-omni)|Mini-Omni|
|94|[AkariAsai/self-rag](https://github.com/AkariAsai/self-rag)|Self-RAG|
|95|[google-deepmind/retro](https://github.com/google-deepmind/retro)|Retro|
|96|[vllm-project/vllm](https://github.com/vllm-project/vllm)|vLLM|
|97|[huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference)|TGI|
|98|[ollama/ollama](https://github.com/ollama/ollama)|Ollama|
|99|[ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)|llama.cpp|
|100|[sgl-project/sglang](https://github.com/sgl-project/sglang)|SGLang|
|101|[NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)|TensorRT-LLM|
|102|[mit-han-lab/llm-awq](https://github.com/mit-han-lab/llm-awq)|AWQ量化|
|103|[AutoGPTQ/AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ)|GPTQ量化|
|104|[bitsandbytes-foundation/bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes)|bitsandbytes|
|105|[turboderp/exllamav2](https://github.com/turboderp/exllamav2)|ExLlamaV2|
|106|[lm-sys/FastChat](https://github.com/lm-sys/FastChat)|FastChat|

</details>

### 7.2 HuggingFace链接索引（162个）

<details>
<summary>点击展开完整HuggingFace链接列表</summary>

|序号|链接|说明|
|:---:|:---|:---|
|1|[meta-llama](https://huggingface.co/meta-llama)|LLaMA系列|
|2|[google](https://huggingface.co/google)|Gemma/Gemini|
|3|[microsoft](https://huggingface.co/microsoft)|Phi系列|
|4|[mistralai](https://huggingface.co/mistralai)|Mistral系列|
|5|[Qwen](https://huggingface.co/Qwen)|通义千问|
|6|[deepseek-ai](https://huggingface.co/deepseek-ai)|DeepSeek|
|7|[THUDM](https://huggingface.co/THUDM)|GLM系列|
|8|[tiiuae](https://huggingface.co/tiiuae)|Falcon|
|9|[allenai](https://huggingface.co/allenai)|OLMo|
|10|[EleutherAI](https://huggingface.co/EleutherAI)|Pythia|
|11|[bigscience/bloom](https://huggingface.co/bigscience/bloom)|BLOOM|
|12|[stabilityai](https://huggingface.co/stabilityai)|StableLM|
|13|[databricks/dbrx-instruct](https://huggingface.co/databricks/dbrx-instruct)|DBRX|
|14|[Snowflake](https://huggingface.co/Snowflake)|Arctic|
|15|[ai21labs](https://huggingface.co/ai21labs)|Jamba|
|16|[CohereForAI](https://huggingface.co/CohereForAI)|Command|
|17|[01-ai](https://huggingface.co/01-ai)|Yi|
|18|[baichuan-inc](https://huggingface.co/baichuan-inc)|Baichuan|
|19|[internlm](https://huggingface.co/internlm)|InternLM|
|20|[openbmb](https://huggingface.co/openbmb)|MiniCPM|
|21|[bigcode](https://huggingface.co/bigcode)|StarCoder|
|22|[codellama](https://huggingface.co/codellama)|CodeLlama|
|23|[WizardLM](https://huggingface.co/WizardLM)|WizardLM|
|24|[TinyLlama](https://huggingface.co/TinyLlama)|TinyLlama|
|25|[HuggingFaceTB](https://huggingface.co/HuggingFaceTB)|SmolLM|
|26|[state-spaces](https://huggingface.co/state-spaces)|Mamba|
|27|[RWKV](https://huggingface.co/RWKV)|RWKV|
|28|[BlinkDL](https://huggingface.co/BlinkDL)|RWKV|
|29|[NX-AI/xLSTM-7b](https://huggingface.co/NX-AI/xLSTM-7b)|xLSTM|
|30|[BAAI](https://huggingface.co/BAAI)|BGE嵌入|
|31|[Alibaba-NLP](https://huggingface.co/Alibaba-NLP)|GTE嵌入|
|32|[intfloat](https://huggingface.co/intfloat)|E5嵌入|
|33|[nomic-ai](https://huggingface.co/nomic-ai)|Nomic嵌入|
|34|[jinaai](https://huggingface.co/jinaai)|Jina嵌入|
|35|[BioMistral](https://huggingface.co/BioMistral)|BioMistral|
|36|[facebook/galactica-120b](https://huggingface.co/facebook/galactica-120b)|Galactica|
|37|[AI-MO](https://huggingface.co/AI-MO)|NuminaMath|
|38|[ToolBench/ToolLLaMA-7b](https://huggingface.co/ToolBench/ToolLLaMA-7b)|ToolLLaMA|
|39|[OpenGVLab](https://huggingface.co/OpenGVLab)|InternVL|
|40|[liuhaotian](https://huggingface.co/liuhaotian)|LLaVA|
|41|[lmsys](https://huggingface.co/lmsys)|Vicuna|
|42|[NousResearch](https://huggingface.co/NousResearch)|Hermes|
|43|[moonshotai](https://huggingface.co/moonshotai)|Kimi|
|44|[MiniMaxAI](https://huggingface.co/MiniMaxAI)|MiniMax|
|45|[ByteDance-Seed](https://huggingface.co/ByteDance-Seed)|Seed系列|
|46|[stepfun-ai](https://huggingface.co/stepfun-ai)|Step|
|47|[Qihoo360](https://huggingface.co/Qihoo360)|360智脑|
|48|[tencent](https://huggingface.co/tencent)|混元|
|49|[apple](https://huggingface.co/apple)|OpenELM|
|50|[infly](https://huggingface.co/infly)|OpenCoder|

</details>

---

## 8. 贡献指南

### 8.1 Model Card模板

```markdown
### 模型名称

|版本|发布时间|参数规模|上下文|许可协议|核心特性|
|:---|:---|:---|:---|:---|:---|
|v1.0|YYYY-MM|XB|XK|License|特性描述|

**官方资源**：
- 📄 论文：[arXiv:XXXX.XXXXX](https://arxiv.org/abs/XXXX.XXXXX)
- 💻 GitHub：[org/repo](https://github.com/org/repo)
- 🤗 HuggingFace：[org/model](https://huggingface.co/org/model)
- 📖 API：https://api.example.com
```

### 8.2 贡献流程

1. **Fork仓库** → 创建分支 → 修改内容 → 提交PR
2. **Issue提交**：发现错误或遗漏请提交Issue
3. **内容要求**：
   - 确保arXiv编号正确
   - 确保链接有效可访问
   - 遵循现有格式规范

### 8.3 贡献者名单

感谢所有贡献者！

---

## 9. 更新日志

|日期|更新内容|
|:---|:---|
|2026-04-03|项目重构，新增200+模型、218条论文引用|
|2026-03-15|新增Kimi K2.5、Baichuan-M3|
|2026-02-20|新增GPT-5.2、Claude 4.6、GLM-5|
|2026-01-10|新增LLaMA 4 Behemoth、Qwen3.5|
|2025-12-01|新增Mamba-3、RWKV-7|
|2025-10-15|新增Claude 4.5、Grok 4|
|2025-07-20|新增Kimi K2、Falcon-H1|
|2025-05-01|项目初始化|

---

## ⭐ Star History

如果这个项目对您有帮助，请给我们一个Star！

---

## 📜 License

MIT License © 2025-2026 Awesome LLM Model List Contributors