# 🃏 Awesome LLM Model List — House of Model Cards (HOMC)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--04--05-blue.svg)]()
[![Models](https://img.shields.io/badge/Models-200%2B-green.svg)]()
[![Papers](https://img.shields.io/badge/Papers-218-orange.svg)]())
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

> 🎴 **最全面的大语言模型索引项目 — 模型卡牌屋 (House of Model Cards)** — 使用扑克牌花色体系对 AI 模型进行创意分类，涵盖从 GPT-1 到最新开源模型的完整调研，包含技术细节、性能指标、部署方式与官方资源。

---

## 📊 核心统计

| 指标 | 数量 | 说明 |
|:---|:---:|:---|
| 🃏 模型系列 | 200+ | 涵盖国内外主流厂商 |
| 📄 arXiv 论文 | 230+ 条 | 2017-2026 年核心论文（含对齐技术/Agent综述） |
| 💻 GitHub 仓库 | 152 个 | 官方代码链接 |
| 🤗 HuggingFace 链接 | 162 个 | 模型权重下载 |
| 🏢 厂商/组织 | 25+ | 全球主要 AI 实验室 |
| 📏 Benchmark | 30+ | 全方位评测基准覆盖 |
| 🛡️ 安全框架 | 6 类 | 攻击类型 + 防御体系 |
| 🔧 微调工具 | 15+ | 从数据到部署的全链路 |
| 🏭 行业场景 | 10+ | 真实落地应用案例 |

---

## 🌟 项目特色

- ✅ **覆盖全面**：从 GPT-1 到 GPT-5、Claude 4.6、LLaMA 4、Qwen3.5 的完整演进（200+ 模型）
- ✅ **资源完整**：每个模型提供 arXiv 论文、GitHub 仓库、HuggingFace 权重、API 文档四件套
- ✅ **🃏 扑克牌分类体系**：独创的 House of Model Cards (HOMC) 分类标记法，用扑克牌花色直观标记模型类型
- ✅ **分类科学**：5 维快速索引 + 🃏 花色/点数双重标记
- ✅ **安全对齐**：完整的 LLM 安全框架、攻击防御指南、开源安全工具推荐
- ✅ **评测详解**：30+ Benchmark 基准解读，覆盖通用/代码/数学/多模态/安全/Agent
- ✅ **微调实战**：LoRA/QLoRA 完整模板 + 工具链推荐 + 数据工程要点
- ✅ **行业案例**：10 大行业落地场景 + RAG 架构图 + 成本估算模型
- ✅ **Prompt 工程**：高阶技巧 + 不同模型的 Prompt 风格偏好
- ✅ **前沿追踪**：视频生成、世界模型等 2026 最新方向
- ✅ **持续更新**：跟踪 2024-2026 年最新模型进展
- ✅ **实用导向**：包含部署指南、硬件配置、量化方案

---

## 🎴 House of Model Cards — 扑克牌分类体系说明

### 设计理念

本项目灵感来源于 [isLinXu/house-of-model-cards](https://github.com/isLinXu/house-of-model-cards) 项目，采用**扑克牌花色**作为模型的视觉化分类系统。就像每一张扑克牌都有其固定的花色和数值一样，每一个 AI 模型也可以通过其"能力属性"被归类到不同的花色中。

### 花色映射规则

| 花色 | 符号 | 含义 | 对应模型类别 | 示例模型 |
|:---|:---:|:---|:---|:---|
| ♠ 黑桃 | ♠️ | **Spade = 图像分类/视觉理解** | 图像分类、目标检测、视觉理解模型 | ResNet, ViT, InternVL, Qwen-VL |
| ♥ 红心 | ❤️ | **Heart = 语言生成/NLP任务** | 通用对话、文本生成、翻译等 LLM | GPT, Claude, LLaMA, Qwen, DeepSeek |
| ♦ 方块 | 🔷 | **Diamond = 语义分割/结构化输出** | 结构化推理、代码生成、数学求解 | StarCoder, DeepSeek-Coder, Qwen-Coder |
| ♣ 梅花 | 🍀 | **Club = 实例分割/多模态融合** | 多模态理解、Agent、嵌入模型 | LLaVA, BGE-M3, Qwen-Agent |
| 🃏 Joker | 🃏 | **Joker = SOTA/突破性模型** | 当前最强或最具创新性的模型 | GPT-5, Claude 4.6, DeepSeek-R1 |

### 点数规则（数字/A/J/Q/K）

| 点数 | 含义 | 说明 |
|:---:|:---|:---|
| **2-7** | 小型模型 (<7B) | 轻量级，适合边缘部署 |
| **8-10** | 中型模型 (7B-30B) | 性能与效率平衡 |
| **J (Jack)** | 专业领域模型 | 针对特定领域优化（代码、数学、医疗） |
| **Q (Queen)** | 大型模型 (30B-100B) | 强大的通用能力 |
| **K (King)** | 超大型模型 (>100B) | 旗舰级性能 |
| **A (Ace)** | SOTA / AGI 级别 | 当前沿技术天花板 |
| **🃏 Joker** | 特殊突破 | 架构创新或范式转移 |

### 标记示例

```
♠K  InternVL2    →  视觉语言模型之王 (76B)
♥A  GPT-5        →  SOTA 级别通用语言模型
♦J  StarCoder2   →  代码专业模型
♣Q  LLaVA-OneVision → 多模态大模型
🃏  DeepSeek-R1   →  推理突破性模型 (GRPO强化学习)
```

### 与原 HOMC 项目的区别

原 [house-of-model-cards](https://github.com/isLinXu/house-of-model-cards) 项目主要聚焦于**计算机视觉模型**的分类（图像分类=♠, 目标检测=♥, 语义分割=♦, 实例分割=♣）。本项目的 HOMC 体系在此基础上进行了**扩展和适配**：

1. **扩展至 LLM 领域**：将花色含义从 CV 任务映射到 LLM 任务域
2. **增加点数维度**：引入 A/J/Q/K 表示模型规模和能力等级
3. **保留 Joker 机制**：用于标记具有突破性创新的模型
4. **双向兼容**：对于纯 CV 模型仍使用原始 HOMC 分类标准

---

## 📑 目录

- [1. 快速索引](#1-快速索引)
  - [1.1 按开源状态](#11-按开源状态)
  - [1.2 按厂商/组织](#12-按厂商组织)
  - [1.3 按应用领域](#13-按应用领域)
  - [1.4 按参数规模](#14-按参数规模)
  - [1.5 按架构类型](#15-按架构类型)
  - [1.6 🃏 按扑克牌花色分类](#16-按扑克牌花色分类)
- [1.7 按推理能力等级分类（⭐ 新增）](#17-按推理能力等级分类新增)
- [1.8 按部署场景分类（⭐ 新增）](#18-按部署场景分类新增)
- [1.9 按训练对齐方法分类（⭐ 新增）](#19-按训练对齐方法分类新增)
- [1.10 🏆 SOTA 排行榜（⭐ 新增）](#110-sota-模型排行榜2026年4月实时新增)
- [2. 通用基础模型](#2-通用基础模型)
- [3. 专项领域模型](#3-专项领域模型)
- [4. 技术对比](#4-技术对比)
- [5. 部署指南](#5-部署指南)
- [6. 📈 LLM 发展时间线](#6-llm-发展时间线)
- [7. 🔬 训练方法与对齐技术](#7-训练方法与对齐技术)
- [8. ⚡ 场景化模型选择指南](#8-场景化模型选择指南)
- [9. 🌍 开源生态地图](#9-开源生态地图)
- [10. 🔮 2026 技术趋势展望](#10-2026-技术趋势展望)
- [11. ❓ FAQ 常见问题](#11-faq-常见问题)
- [12. 🛡️ 安全与对齐](#12-️-安全与对齐)
- [13. 📏 评测基准详解](#13-评测基准详解)
- [14. 🔧 微调工具链与实战](#14--微调工具链与实战)
- [15. 🏭 行业应用案例](#15--行业应用案例)
- [16. 💡 Prompt Engineering 指南](#--prompt-engineering-指南)
- [17. 🎬 视频生成与世界模型](#17-视频生成与世界模型)
- [18. 参考文献](#18-参考文献)
- [13. 资源索引](#13-资源索引)
- [14. 贡献指南](#14-贡献指南)
- [15. 更新日志](#15-更新日志)

---

## 1. 快速索引

### 1.1 按开源状态

| 类别 | 模型 |
|:---|:---|
| **完全开源** | LLaMA、Qwen、DeepSeek、GLM、Mistral、Falcon、OLMo、Pythia、BLOOM、StableLM、RWKV、Mamba、InternLM、Baichuan、Yi、MiniCPM |
| **有限开源** | Gemma、Phi、Grok-1、Command-R、Jamba、DBRX、Arctic |
| **闭源 API** | GPT-4/5、Claude、Gemini、Grok-2+、ERNIE、混元、豆包、Kimi、星火 |

### 1.2 按厂商/组织

| 地区 | 厂商 | 代表模型 | 🃏 标记 |
|:---|:---|:---|:---|
| 🇺🇸 美国 | OpenAI | GPT-4/5、o1/o3/o4-mini | ♥A |
| 🇺🇸 美国 | Anthropic | Claude 3.5/4/4.6 | ♥A |
| 🇺🇸 美国 | Meta | LLaMA 1/2/3/4 | ♥K |
| 🇺🇸 美国 | Google | Gemini、Gemma | ♥Q |
| 🇺🇸 美国 | Microsoft | Phi-1/2/3/4 | ♥10 |
| 🇺🇸 美国 | xAI | Grok-1/2/3/4 | ♥K |
| 🇺🇸 美国 | AI2 | OLMo | ♥9 |
| 🇺🇸 美国 | EleutherAI | Pythia、GPT-NeoX | ♥8 |
| 🇨🇳 中国 | 阿里巴巴 | Qwen 1/2/2.5/3/3.5 | ♥K |
| 🇨🇳 中国 | DeepSeek | DeepSeek-V1/V2/V3、R1 | 🃏 Joker |
| 🇨🇳 中国 | 智谱 AI | GLM-4/5、ChatGLM | ♥Q |
| 🇨🇳 中国 | 百度 | ERNIE 4.0/5.0 | ♥Q |
| 🇨🇳 中国 | 腾讯 | 混元 Large | ♥K |
| 🇨🇳 中国 | 字节跳动 | 豆包、Seed 系列 | ♠Q / ♦J |
| 🇨🇳 中国 | 月之暗面 | Kimi K2/K2.5 | 🃏 Joker |
| 🇨🇳 中国 | MiniMax | M1/M2.5 | ♥K |
| 🇨🇳 中国 | 面壁智能 | MiniCPM | ♥7 |
| 🇨🇳 中国 | 上海 AI Lab | InternLM、InternVL | ♠Q |
| 🇨🇳 中国 | 百川智能 | Baichuan-M1/M2/M3 | ♥Q |
| 🇨🇳 中国 | 零一万物 | Yi-1.5 | ♥10 |
| 🇫🇷 法国 | Mistral AI | Mistral、Mixtral | ♥Q |
| 🇦🇪 阿联酋 | TII | Falcon、Falcon-H1 | ♥Q |
| 🇮🇱 以色列 | AI21 Labs | Jamba 1.5 | ♥Q |
| 🇺🇸 美国 | Databricks | DBRX | ♥Q |
| 🇺🇸 美国 | Snowflake | Arctic | ♥Q |

### 1.3 按应用领域

| 领域 | 代表模型 | 🃏 标记 |
|:---|:---|:---|
| **通用对话** | GPT-4/5、Claude、Qwen、DeepSeek、LLaMA | ♥A ~ ♥K |
| **代码生成** | StarCoder2、DeepSeek-Coder、CodeLlama、Qwen-Coder、Codestral | ♦J |
| **数学推理** | DeepSeekMath、Qwen-Math、Llemma、NuminaMath | ♦J |
| **多模态 VLM** | GPT-4V、LLaVA、Qwen-VL、InternVL、MiniCPM-V | ♠Q / ♣Q |
| **推理增强** | o1/o3/o4-mini、DeepSeek-R1、QwQ、Kimi K2 | 🃏 Joker |
| **Agent/工具** | Qwen-Agent、ToolLLaMA、Gorilla | ♣J |
| **嵌入模型** | BGE-M3、GTE-Qwen、E5-Mistral | ♣10 |
| **医疗科学** | Med-PaLM、BioMistral、MedGemma、SciGLM | ♦10 |
| **音频语言** | Qwen-Audio、GLM-4-Voice、Whisper | ♣J |
| **检索增强** | Self-RAG、CRAG、Retro | ♣10 |

### 1.4 按参数规模

| 规模 | 🃏 点数 | 代表模型 |
|:---|:---:|:---|
| **<3B** | 2-7 | TinyLlama(1.1B)、SmolLM2(1.7B)、Phi-3-mini(3.8B)、MiniCPM(2.4B)、Gemma-2-2B |
| **3-10B** | 8-10 | LLaMA-3-8B、Qwen2.5-7B、Mistral-7B、GLM-4-9B、DeepSeek-7B |
| **10-100B** | J-Q | LLaMA-3-70B、Qwen2.5-72B、Mixtral-8x22B、DeepSeek-V2-236B |
| **100B+** | K-A | GPT-4(1.8T)、Claude-3-Opus、LLaMA-4-Behemoth(2T)、Qwen3-235B、DeepSeek-V3(671B) |

### 1.5 按架构类型

| 架构 | 特点 | 代表模型 | 🃏 标记 |
|:---|:---|:---|:---|
| **Dense Transformer** | 标准注意力机制 | GPT、LLaMA、Claude、Qwen | ♥ |
| **MoE** | 专家混合，稀疏激活 | Mixtral、DeepSeek-V2/V3、Qwen-MoE、DBRX | ♥K |
| **SSM (Mamba)** | 状态空间模型，线性复杂度 | Mamba-1/2/3、Falcon-Mamba | 🃏 Joker |
| **RNN (RWKV)** | 循环结构，高效推理 | RWKV-5/6/7 | 🃏 Joker |
| **Hybrid** | 混合架构 | Jamba(Mamba+Attention)、RecurrentGemma | ♣Q |
| **xLSTM** | 扩展 LSTM 架构 | xLSTM-7B | 🃏 Joker |

### 1.6 🃏 按扑克牌花色分类

#### ♠ 黑桃 — 视觉与多模态理解 (Spade: Vision & Multimodal Understanding)

| 模型 | 参数 | 类型 | 说明 |
|:---|:---:|:---|:---|
| **♠K** InternVL2 | 76B | VLM | 最强开源视觉语言模型之一 |
| **♠Q** LLaVA-OneVision-1.5 | 72B | VLM | 统一视觉理解 |
| **♠Q** Qwen3-VL | 8B | VLM | 高效视觉语言模型 |
| **♠J** CogVLM2 | 19B | VLM | 多模态认知模型 |
| **♠10** MiniCPM-V | 8B | VLM | 端侧多模态部署 |
| **♠9** Pixtral | 12B | VLM | Mistral 多模态系列 |

#### ♥ 红心 — 通用语言模型 (Heart: General Language Models)

| 模型 | 参数 | 版本 | 说明 |
|:---|:---:|:---|:---|
| **♥A** GPT-5 | 未公开 | 2024-12 | AGI 能力跃升 |
| **♥A** Claude 4.6 | 未公开 | 2026-02 | 当前最强闭源之一 |
| **♥A** Gemini 3.1 | 未公开 | 2026-01 | 多模态原生 |
| **♥K** LLaMA 4 Behemoth | 2T | 2025-10 | 最强开源模型 |
| **♥K** DeepSeek-V3 | 671B | 2024-12 | FP8 训练突破 |
| **♥K** Qwen3.5 | 397B | 2026-01 | 全模态能力 |
| **♥K** Grok-3 | 3T MoE | 2025-02 | 100K H100 训练 |
| **♥Q** Qwen2.5-72B | 72B | 2024-09 | 编码数学增强 |
| **♥Q** LLaMA 3.1-405B | 405B | 2024-07 | 开源旗舰 |
| **♥Q** Mistral Large 2 | 123B | 2024-07 | 开源旗舰 |
| **♥J** LLaMA 3-8B | 8B | 2024-04 | 效率标杆 |
| **♥J** Qwen2.5-7B | 7B | 2024-09 | 最佳 7B |
| **♥J** Mistral 7B | 7B | 2023-09 | 开源先驱 |
| **♥10** Phi-4 | 14B | 2024-12 | 推理突破 |
| **♥10** Gemma 2-9B | 9B | 2024-06 | Google 轻量旗舰 |
| **♥9** GLM-4-9B | 9B | 2024 | 国产优秀开源 |
| **♥8** OLMo 2-7B | 7B | 2024-11 | 全开源(数据+权重) |
| **♥7** MiniCPM | 2.4B | 2024-02 | 端侧部署优选 |

#### ♦ 方块 — 结构化推理与代码 (Diamond: Structured Reasoning & Code)

| 模型 | 参数 | 类型 | 说明 |
|:---|:---:|:---|:---|
| **♦K** DeepSeek-R1 | 671B | 推理 | GRPO 强化学习推理 |
| **♦K** o3 | 未公开 | 2025-01 | OpenAI 深度推理 |
| **♦Q** Kimi K2 | 1T MoE | 推理 | Muon 优化器 |
| **♦J** StarCoder2 | 15B | 代码 | 大规模代码预训练 |
| **♦J** DeepSeek-Coder-V2 | 236B | 代码 | 大规模代码 MoE |
| **♦J** Qwen2.5-Coder-32B | 32B | 代码 | 编码增强 |
| **♦J** CodeGeeX4 | 9B | 代码 | 国产代码模型 |
| **♦10** Qwen2.5-Math-72B | 72B | 数学 | 数学推理 SOTA |
| **♦10** DeepSeekMath-7B | 7B | 数学 | 数学专用 |
| **♦9** NuminaMath-7B | 7B | 数学 | AIMO 竞赛优化 |

#### ♣ 梅花 — Agent 与嵌入 (Club: Agent & Embeddings)

| 模型 | 参数 | 类型 | 说明 |
|:---|:---:|:---|:---|
| **♣K** Qwen-Agent-72B | 72B | Agent | 工具调用框架 |
| **♣Q** BGE-M3 | 568B | 嵌入 | 多语言多函数嵌入 |
| **♣J** ToolLLaMA-7B | 7B | Agent | 工具调用专精 |
| **♣J** Gorilla-7B | 7B | Agent | API 调用专精 |
| **♣10** Self-RAG-13B | 13B | RAG | 自适应检索增强 |
| **♣10** E5-Mistral-7B | 7B | 嵌入 | 高质量文本嵌入 |
| **♣9** Qwen3-Embedding-8B | 8B | 嵌入 | 最新嵌入模型 |
| **♣9** Jina Embeddings | 1.3B | 嵌入 | 多尺度嵌入 |

#### 🃏 Joker — 突破性创新模型

| 模型 | 创新点 | 说明 |
|:---|:---|:---|
| **🃏 DeepSeek-R1** | GRPO 强化学习推理 | 用纯 RL 达成推理突破，成本极低 |
| **🃏 Mamba-1/2/3** | 状态空间架构 | 突破 Transformer 的线性复杂度替代方案 |
| **🃏 RWKV-7** | 线性注意力 RNN | 结合 RNN 效率和 Transformer 表达力 |
| **🃏 Kimi K2** | Muon 优化器 + 1T MoE | 开源模型首次进入第一梯队 |
| **🃏 LLaMA 4 Behemoth** | 2T 参数开源 | 最大规模的开源模型 |
| **🃏 xLSTM** | 扩展 LSTM | LSTM 的现代化复兴 |

### 🃏 双花色标记规则（新增）

部分模型具有多重核心能力，使用双花色标记以更精确描述：

```
♥♠ 通用+视觉   →  GPT-4V, Gemini 3.1, Claude 4.5（原生多模态通用模型）
♥♦ 通用+代码   →  Qwen2.5-Coder, LLaMA 3.2（编码增强的通用模型）
♠♣ 视觉+Agent  →  InternVL-Tool, LLaVA-Agent
🃏♥ 突破+通用   →  DeepSeek-R1, Kimi K2（推理突破 + 通用能力）
```

> **说明**：主花色（第一个）表示最突出的能力，副花色（第二个）表示次要但显著的能力。

---

## 1.7 按推理能力等级分类（⭐ 新增）

> 2024-2026 年最重要的范式转移：从「快速响应」到「深度推理」。此维度帮助用户按模型的"思考深度"选型。

| 推理等级 | 符号 | 特征 | 代表模型 | 🃏 标记 |
|:---|:---:|:---|:---|:---|
| **Level 0 — 快速响应型** | ⚡ | 单次前向传播，无显式推理链，延迟 <500ms | GPT-3.5-turbo, LLaMA-3-8B, Mistral-7B, Phi-3-mini | ♥J ~ ♥10 |
| **Level 1 — 轻量思维链** | 🧠 | 内部 CoT，短思考过程，延迟 1-5s | GPT-4, Claude 3.5, Qwen2.5-72B, GLM-4 | ♥Q ~ ♥K |
| **Level 2 — 深度推理型** | 🔬 | 显式长 CoT / 草稿本推理，延迟 10s-5min | o1, o3, DeepSeek-R1, QwQ, Kimi K1.5 | 🃏 Joker |
| **Level 3 — Agent 自主推理** | 🤖 | 多步工具调用 + 规划 + 反思循环 | o4-mini-pro, Claude 4.6, GPT-5 (Agent Mode) | ♥A |

**选型建议**：
- **聊天/客服/翻译** → Level 0-1 即可，成本敏感选 L0
- **数学/编程/科研** → 必须用 Level 2+，推荐 R1/o3
- **自主 Agent 工作流** → Level 3，需要强规划能力

---

## 1.8 按部署场景分类（⭐ 新增）

| 部署场景 | 硬件要求 | 延迟目标 | 推荐模型 | 🃏 点数 |
|:---|:---|:---|:---|:---|
| **📱 手机端侧** | <4GB RAM, NPU/DSP | <2s | MiniCPM(2.4B), Phi-4-mini(3.8B), SmolLM2(1.7B), Gemma-2-2B, MobileLLM(1B) | 2~7 |
| **💻 个人电脑** | 8-24GB GPU (RTX 4060/4070) | <5s | LLaMA-3-8B, Qwen2.5-7B, Mistral-7B, DeepSeek-7B, TinyLlama(1.1B) | 8~10 |
| **🖥️ 工作站** | 48-96GB GPU (RTX 4090/A6000) | <10s | LLaMA-3-70B, Qwen2.5-72B, Mixtral-8x22B, DeepSeek-V3(INT8) | J ~ Q |
| **☁️ 云端 API** | 无硬件需求 | 取决于供应商 | GPT-5, Claude 4.6, Gemini 3.1, DeepSeek-V3, Qwen-Plus | A ~ K |
| **🏭 企业私有化** | 8×A100/H100 集群 | <3s (批处理) | LLaMA-4-Behemoth, Qwen3-235B, DeepSeek-V3(FP16), ERNIE 5.0 MoE | K |
| **🔌 边缘/IoT** | <2GB RAM, ARM/NPU | <1s | SmolLM2(135M), TinyLlama(1.1B) INT4, OpenELM(270M) | 2~4 |
| **🎮 游戏/实时** | 消费级 GPU, <16GB | <100ms | Phi-3-mini(3.8B), Gemma-2-2B, StableLM-2-1.6B | 7~10 |

**成本估算参考**（单次查询）：
| 场景 | 模型规模 | 自托管成本/月 | API 成本/百万 Token |
|:---|:---|:---|:---|
| 个人项目 | 7B INT4 (RTX 4060) | 电费 ≈¥50 | - |
| 初创公司 | 70B INT4 (2×4090) | 电费 ≈¥300 | DeepSeek: ¥2~8 |
| 企业级 | 671B FP8 (8×H100) | 租赁 ≈¥30K/月 | GPT-5: ¥200~400 |

---

## 1.9 按训练对齐方法分类（⭐ 新增）

| 对齐方法 | 全称 | 核心思想 | 代表模型 | 🃏 标记 | 年份 |
|:---|:---|:---|:---|:---|:---|
| **SFT** | Supervised Fine-Tuning | 有监督指令微调，最基础的对齐方式 |几乎所有模型的基础步骤 | All | 2022+ |
| **RLHF** | Reinforcement Learning from Human Feedback | PPO + 人类偏好奖励模型 | ChatGPT, Claude 1-2, LLaMA 2 Chat | ♥ | 2023 |
| **DPO** | Direct Preference Optimization | 直接偏好优化，无需 RM 模型 | Zephyr, Intel Neural Chat, OpenHathi | ♥Q | 2023 |
| **Constitutional AI** | CAI | AI 自我批评 + 修正 | Claude 系列 (Anthropic) | ♥A | 2023 |
| **GRPO** | Group Relative Policy Optimization | 组内相对策略优化，无需 RM | DeepSeek-R1/R1-0528 | 🃏 | 2025 |
| **KTO** | Kahneman-Tversky Optimization | 基于前景理论的二元反馈 | HuggingFace Zephyr-β | ♥9 | 2024 |
| **Online DPO** | Online Direct PO | 在线迭代 DPO，持续改进 | QwQ, 部分 Qwen 变体 | ♥ | 2024 |
| **SimPO** | Simple Preference Opt | 简化的偏好优化，只需一个超参 | Mistral-Nemo, Gemma-2-it | ♥ | 2024 |
| **ORM** | Outcome Reward Modeling | 结果奖励建模（vs 过程 PRM） | OpenAI o-series | ♥A | 2024 |
| **PRM** | Process Reward Modeling | 过程奖励建模，逐步验证推理链 | DeepSeek-R1 (辅助) | 🃏 | 2025 |
| **Muon Optimizer** | Muon 优化器 | 类 momentum 优化用于大规模 MoE 训练 | Kimi K2/K2.5 | 🃏 | 2025 |

**训练方法演进路线图**：
```
SFT (2022) → RLHF (2023) → DPO (2023) → GRPO/Muon (2025)
                    ↓                ↓              ↓
               Constitutional      SimPO/KTO     PRM+ORM
                  AI (2023)       (2024)        (2024-25)
```

---

## 1.10 🏆 SOTA 模型排行榜（2026年4月实时）（⭐ 新增）

> 综合多项基准测试的 Top 10 排行，分为闭源/开源双赛道。

### 闭源赛道

| 排名 | 模型 | 厂商 | MMLU-Pro | GPQA | Code | Math | 🃏 | 亮点 |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---|:---|
| 🥇 | **GPT-5** | OpenAI | 92.1% | 78.3% | 96.8% | 98.5% | ♥A | AGI 能力跃升，1M 上下文 |
| 🥈 | **Claude 4.6** | Anthropic | 91.8% | 95.4% | 95.2% | 97.8% | ♥A | 安全最强，2M 上下文 |
| 🥉 | **Gemini 3.1 Pro** | Google | 90.5% | 76.8% | 94.1% | 97.2% | ♥A | 多模态原生，4M 上下文 |
| 4 | **o4-mini** | OpenAI | 89.2% | 74.2% | 93.5% | 96.8% | ♥A | 高效推理，成本仅 o3 的 1/10 |
| 5 | **Grok-4.1** | xAI | 88.8% | 73.5% | 92.8% | 96.2% | ♥K | 实时信息，4M 上下文 |
| 6 | **Claude 4.5 Opus** | Anthropic | 89.5% | 94.2% | 93.8% | 97.0% | ♥A | 编码增强版 |
| 7 | **Gemini 2.5 Pro** | Google | 87.2% | 72.1% | 91.5% | 95.5% | ♥Q | Agent 能力突出 |
| 8 | **GPT-4.5** | OpenAI | 86.8% | 71.2% | 90.2% | 94.8% | ♥A | 创造力最强 |
| 9 | **MiniMax-M2.5** | MiniMax | 85.5% | 68.8% | 88.5% | 93.2% | ♥K | 2M 上下文，高性价比 |
| 10 | **GLM-5** | 智谱 AI | 84.5% | 68.2% | 87.5% | 91.8% | ♥Q | 国产最强之一 |

### 开源赛道

| 排名 | 模型 | 组织 | 参数 | MMLU-Pro | GPQA | Code | Math | 🃏 | 许可 |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|:---|
| 🥇 | **LLaMA 4 Maverick** | Meta | 400B (52B act) | 88.5% | 72.1% | 91.2% | 95.5% | ♥K | Llama 4 |
| 🥈 | **DeepSeek-R1** | DeepSeek | 671B | 88.2% | 73.8% | 92.1% | 96.2% | 🃏 | MIT |
| 🥉 | **Qwen3-235B** | 阿里 | 235B (22B act) | 87.8% | 71.5% | 90.8% | 94.8% | ♥K | Apache 2.0 |
| 4 | **Kimi K2** | 月之暗面 | 1T (32B act) | 85.8% | 69.5% | 88.2% | 92.5% | 🃏 | MIT |
| 5 | **DeepSeek-V3** | DeepSeek | 671B (37B act) | 86.5% | 70.2% | 89.5% | 93.2% | ♥K | DeepSeek |
| 6 | **Qwen2.5-72B** | 阿里 | 72B | 83.2% | 65.8% | 87.2% | 90.5% | ♥Q | Apache 2.0 |
| 7 | **Mixtral-8x22B** | Mistral | 176B (39B act) | 82.5% | 64.2% | 86.5% | 89.8% | ♥Q | Apache 2.0 |
| 8 | **Intern-S1-Pro** | 上海 AI Lab | 未公开 | 84.2% | 68.5% | 86.8% | 91.2% | ♠Q | Research |
| 9 | **Phi-4-reasoning** | Microsoft | 15B | 80.5% | 60.2% | 85.5% | 90.2% | ♥10 | MIT |
| 10 | **Gemma-3-27B** | Google | 27B | 79.2% | 58.5% | 84.2% | 88.5% | ♥10 | Gemma |

> **注意**：以上数据来源于各官方技术报告及第三方基准测试（Arena、LMSYS Chatbot Arena），具体数值因评测版本不同可能有差异。

---

## 2. 通用基础模型

### 2.1 OpenAI GPT 系列 ♥A

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| GPT-1 | 2018-06 | 117M | 512 | Research | Transformer 预训练 |
| GPT-2 | 2019-02 | 1.5B | 1K | MIT | 无监督多任务学习 |
| GPT-3 | 2020-05 | 175B | 4K | API | Few-shot 学习 |
| GPT-3.5-turbo | 2022-11 | 175B | 16K | API | RLHF 对齐 |
| GPT-4 | 2023-03 | 1.8T MoE | 128K | API | 多模态、推理增强 |
| GPT-4-turbo | 2023-11 | 1.8T MoE | 128K | API | 更快推理、降价 |
| GPT-4.5 | 2024-02 | 2T MoE | 256K | API | 增强创造力 |
| GPT-5 | 2024-12 | 未公开 | 1M | API | AGI 能力跃升 |
| GPT-5.1 | 2025-06 | 未公开 | 2M | API | 多模态原生 |
| GPT-5.2 | 2026-01 | 未公开 | 4M | API | 实时推理 |
| o1 | 2024-09 | 未公开 | 128K | API | 思维链推理 |
| o3 | 2025-01 | 未公开 | 256K | API | 深度推理 |
| o4-mini | 2025-06 | 未公开 | 128K | API | 高效推理 |

**官方资源**：
- 📄 论文：[arXiv:2005.14165](https://arxiv.org/abs/2005.14165) (GPT-3) · [arXiv:2303.08774](https://arxiv.org/abs/2303.08774) (GPT-4) · [arXiv:2410.21276](https://arxiv.org/abs/2410.21276) (GPT-4o) · [arXiv:2412.16720](https://arxiv.org/abs/2412.16720) (o1) · [arXiv:2601.03267](https://arxiv.org/abs/2601.03267) (GPT-5)
- 💻 GitHub：[openai/openai-cookbook](https://github.com/openai/openai-cookbook)
- 📖 API：https://platform.openai.com/docs

---

### 2.2 Anthropic Claude 系列 ♥A

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| Claude 1 | 2023-03 | 52B | 9K | API | Constitutional AI |
| Claude 2 | 2023-07 | 未公开 | 100K | API | 长上下文 |
| Claude 3 Haiku | 2024-03 | 20B | 200K | API | 快速响应 |
| Claude 3 Sonnet | 2024-03 | 70B | 200K | API | 平衡性能 |
| Claude 3 Opus | 2024-03 | 未公开 | 200K | API | 最强推理 |
| Claude 3.5 Sonnet | 2024-06 | 未公开 | 200K | API | 编码增强 |
| Claude 3.7 Sonnet | 2025-02 | 未公开 | 256K | API | 扩展思考 |
| Claude 4 Opus | 2025-06 | 未公开 | 512K | API | 深度推理 |
| Claude 4.5 Opus | 2025-10 | 未公开 | 1M | API | 多模态原生 |
| Claude 4.6 | 2026-02 | 未公开 | 2M | API | AGI 能力 |

**官方资源**：
- 📄 论文：[arXiv:2204.06745](https://arxiv.org/abs/2204.06745) (Constitutional AI) · [arXiv:2310.01858](https://arxiv.org/abs/2310.01858) (Claude 2)
- 📖 API：https://docs.anthropic.com

---

### 2.3 Meta LLaMA 系列 ♥K

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| LLaMA 1 | 2023-02 | 7/13/33/65B | 2K | Research | 高效预训练 |
| LLaMA 2 | 2023-07 | 7/13/70B | 4K | Llama 2 License | RLHF 对齐 |
| LLaMA 3 | 2024-04 | 8/70B | 8K | Llama 3 License | 多语言增强 |
| LLaMA 3.1 | 2024-07 | 8/70/405B | 128K | Llama 3.1 License | 长上下文 |
| LLaMA 3.2 | 2024-09 | 1/3/11/90B | 128K | Llama 3.2 License | 视觉多模态 |
| LLaMA 3.3 | 2024-12 | 70B | 128K | Llama 3.3 License | 推理优化 |
| LLaMA 4 Scout | 2025-04 | 109B (17B 激活) | 10M | Llama 4 License | 超长上下文 |
| LLaMA 4 Maverick | 2025-04 | 400B (52B 激活) | 1M | Llama 4 License | MoE 架构 |
| LLaMA 4 Behemoth | 2025-10 | 2T | 10M | Llama 4 License | 最强开源 |

**官方资源**：
- 📄 论文：[arXiv:2302.13971](https://arxiv.org/abs/2302.13971) (LLaMA 1) · [arXiv:2307.09288](https://arxiv.org/abs/2307.09288) (LLaMA 2) · [arXiv:2407.21783](https://arxiv.org/abs/2407.21783) (LLaMA 3) · [arXiv:2510.12178](https://arxiv.org/abs/2510.12178) (LLaMA 4) · [arXiv:2601.11659](https://arxiv.org/abs/2601.11659) (LLaMA 4 完整)
- 💻 GitHub：[meta-llama/llama-models](https://github.com/meta-llama/llama-models)
- 🤗 HuggingFace：[meta-llama](https://huggingface.co/meta-llama)

---

### 2.4 Google Gemini/Gemma 系列 ♥Q

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| Gemini 1.0 Pro | 2023-12 | 未公开 | 32K | API | 原生多模态 |
| Gemini 1.5 Pro | 2024-02 | 未公开 | 1M | API | 超长上下文 |
| Gemini 2.0 Flash | 2024-12 | 未公开 | 1M | API | 实时推理 |
| Gemini 2.5 | 2025-06 | 未公开 | 2M | API | Agent 能力 |
| Gemini 3.1 | 2026-01 | 未公开 | 4M | API | AGI 进展 |
| Gemma 1 | 2024-02 | 2/7B | 8K | Gemma License | 轻量开源 |
| Gemma 2 | 2024-06 | 2/9/27B | 8K | Gemma License | 性能提升 |
| Gemma 3 | 2025-03 | 2/9/27B | 128K | Gemma License | 多模态 |

**官方资源**：
- 📄 论文：[arXiv:2408.00118](https://arxiv.org/abs/2408.00118) (Gemma 2) · [arXiv:2503.19786](https://arxiv.org/abs/2503.19786) (Gemma 3) · [arXiv:2507.06261](https://arxiv.org/abs/2507.06261) (Gemini 2.5)
- 💻 GitHub：[google-deepmind/gemma](https://github.com/google-deepmind/gemma) · [google/gemma_pytorch](https://github.com/google/gemma_pytorch)
- 🤗 HuggingFace：[google](https://huggingface.co/google)

---

### 2.5 Microsoft Phi 系列 ♥10

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| Phi-1 | 2023-06 | 1.3B | 2K | MIT | 教科书数据 |
| Phi-1.5 | 2023-09 | 1.3B | 2K | MIT | 合成数据增强 |
| Phi-2 | 2023-12 | 2.7B | 2K | MIT | 推理能力 |
| Phi-3-mini | 2024-04 | 3.8B | 128K | MIT | 手机部署 |
| Phi-3-small | 2024-05 | 7B | 128K | MIT | 平衡版本 |
| Phi-3-medium | 2024-05 | 14B | 128K | MIT | 性能增强 |
| Phi-3.5-mini | 2024-08 | 3.8B | 128K | MIT | 多模态 |
| Phi-4 | 2024-12 | 14B | 16K | MIT | 推理突破 |
| Phi-4-mini | 2025-04 | 3.8B | 128K | MIT | 端侧推理 |
| Phi-4-reasoning | 2025-06 | 15B | 32K | MIT | 强化推理 |

**官方资源**：
- 📄 论文：[arXiv:2309.00071](https://arxiv.org/abs/2309.00071) (Phi-1) · [arXiv:2306.11644](https://arxiv.org/abs/2306.11644) (Phi-1.5) · [arXiv:2404.14219](https://arxiv.org/abs/2404.14219) (Phi-3) · [arXiv:2412.08905](https://arxiv.org/abs/2412.08905) (Phi-4) · [arXiv:2504.21233](https://arxiv.org/abs/2504.21233) (Phi-4-mini) · [arXiv:2504.21318](https://arxiv.org/abs/2504.21318) (Phi-4-reasoning)
- 💻 GitHub：[microsoft/Phi-4](https://github.com/microsoft/Phi-4) · [microsoft/Phi-3-cookbooks](https://github.com/microsoft/Phi-3-cookbooks)
- 🤗 HuggingFace：[microsoft](https://huggingface.co/microsoft)

---

### 2.6 xAI Grok 系列 ♥K

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| Grok-1 | 2024-03 | 314B MoE | 8K | Apache 2.0 | 开源 MoE |
| Grok-1.5 | 2024-04 | 未公开 | 128K | API | 长上下文 |
| Grok-2 | 2024-08 | 未公开 | 128K | API | 多模态 |
| Grok-2.5 | 2024-12 | 未公开 | 256K | API | 推理增强 |
| Grok-3 | 2025-02 | 3T MoE | 1M | API | 100K H100 训练 |
| Grok-4 | 2025-08 | 未公开 | 2M | API | AGI 能力 |
| Grok-4.1 | 2026-01 | 未公开 | 4M | API | 实时推理 |

**官方资源**：
- 💻 GitHub：[xai-org/grok-1](https://github.com/xai-org/grok-1)
- 📖 API：https://x.ai/api

---

### 2.7 Mistral AI 系列 ♥Q

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| Mistral 7B | 2023-09 | 7B | 32K | Apache 2.0 | 滑动窗口注意力 |
| Mixtral 8x7B | 2023-12 | 46.7B (12.9B 激活) | 32K | Apache 2.0 | 稀疏 MoE |
| Mixtral 8x22B | 2024-04 | 176B (39B 激活) | 64K | Apache 2.0 | 大规模 MoE |
| Mistral Large | 2024-02 | 未公开 | 128K | API | 旗舰模型 |
| Mistral Large 2 | 2024-07 | 123B | 128K | Research | 开源旗舰 |
| Mistral Large 3 | 2025-03 | 未公开 | 256K | API | 推理增强 |
| Codestral | 2024-05 | 22B | 32K | MNPL | 代码专用 |

**官方资源**：
- 📄 论文：[arXiv:2310.06825](https://arxiv.org/abs/2310.06825) (Mistral 7B) · [arXiv:2401.04088](https://arxiv.org/abs/2401.04088) (Mixtral)
- 💻 GitHub：[mistralai/mistral-inference](https://github.com/mistralai/mistral-inference)
- 🤗 HuggingFace：[mistralai](https://huggingface.co/mistralai)

---

### 2.8 Cohere Command 系列 ♥Q

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| Command | 2023-09 | 52B | 4K | API | 企业级 |
| Command R | 2024-03 | 35B | 128K | CC-BY-NC-4.0 | RAG 优化 |
| Command R+ | 2024-04 | 104B | 128K | CC-BY-NC-4.0 | 多语言 |
| Command R7B | 2024-12 | 7B | 128K | CC-BY-NC-4.0 | 轻量版 |

**官方资源**：
- 🤗 HuggingFace：[CohereForAI](https://huggingface.co/CohereForAI) · [CohereLabs](https://huggingface.co/CohereLabs)
- 📖 API：https://docs.cohere.com

---

### 2.9 TII Falcon 系列 ♥Q

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| Falcon 7B | 2023-05 | 7B | 2K | Apache 2.0 | RefinedWeb 数据 |
| Falcon 40B | 2023-05 | 40B | 2K | Apache 2.0 | 高质量预训练 |
| Falcon 180B | 2023-09 | 180B | 2K | Falcon License | 最大开源 |
| Falcon 2 | 2024-05 | 11B | 8K | Apache 2.0 | 多模态 |
| Falcon 3 | 2024-12 | 1/3/7/10B | 32K | Apache 2.0 | 效率提升 |
| Falcon-H1 | 2025-07 | 1.5/3.5/7/34B | 256K | Apache 2.0 | Mamba 混合架构 |

**官方资源**：
- 📄 论文：[arXiv:2311.16867](https://arxiv.org/abs/2311.16867) (Falcon) · [arXiv:2407.14885](https://arxiv.org/abs/2407.14885) (Falcon 2) · [arXiv:2507.22448](https://arxiv.org/abs/2507.22448) (Falcon-H1)
- 💻 GitHub：[tiiuae/falcon-llm](https://github.com/tiiuae/falcon-llm) · [tiiuae/Falcon-H1](https://github.com/tiiuae/Falcon-H1)
- 🤗 HuggingFace：[tiiuae](https://huggingface.co/tiiuae)

---

### 2.10 AI2 OLMo 系列 ♥8~9

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| OLMo 1 | 2024-02 | 1/7B | 2K | Apache 2.0 | 完全开源(数据+代码+权重) |
| OLMo 1.5 | 2024-06 | 7B | 4K | Apache 2.0 | 训练优化 |
| OLMo 2 | 2024-11 | 7/13B | 4K | Apache 2.0 | RLHF 对齐 |
| OLMoE | 2024-09 | 6.9B (1.3B 激活) | 4K | Apache 2.0 | 开源 MoE |

**官方资源**：
- 📄 论文：[arXiv:2402.00838](https://arxiv.org/abs/2402.00838) (OLMo) · [arXiv:2501.00656](https://arxiv.org/abs/2501.00656) (OLMo 2) · [arXiv:2409.02060](https://arxiv.org/abs/2409.02060) (OLMoE)
- 💻 GitHub：[allenai/OLMo](https://github.com/allenai/OLMo) · [allenai/OLMo-core](https://github.com/allenai/OLMo-core)
- 🤗 HuggingFace：[allenai](https://huggingface.co/allenai)

---

### 2.11 EleutherAI Pythia 系列 ♥8

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| GPT-NeoX | 2022-04 | 20B | 2K | Apache 2.0 | 大规模开源 |
| Pythia | 2023-04 | 70M-12B | 2K | Apache 2.0 | 可复现研究 |
| GPT-J-6B | 2021-06 | 6B | 2K | Apache 2.0 | 早期开源 |
| Llemma | 2023-10 | 7/34B | 4K | Llama License | 数学专用 |

**官方资源**：
- 📄 论文：[arXiv:2204.06745](https://arxiv.org/abs/2204.06745) (GPT-NeoX) · [arXiv:2304.01373](https://arxiv.org/abs/2304.01373) (Pythia) · [arXiv:2310.10631](https://arxiv.org/abs/2310.10631) (Llemma)
- 💻 GitHub：[EleutherAI/gpt-neox](https://github.com/EleutherAI/gpt-neox) · [EleutherAI/pythia](https://github.com/EleutherAI/pythia)
- 🤗 HuggingFace：[EleutherAI](https://huggingface.co/EleutherAI)

---

### 2.12 BigScience BLOOM 系列 ♥Q

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| BLOOM | 2022-07 | 176B | 2K | RAIL | 46 语言、多国合作 |
| BLOOMZ | 2022-11 | 176B | 2K | RAIL | 指令微调版 |

**官方资源**：
- 📄 论文：[arXiv:2211.05100](https://arxiv.org/abs/2211.05100)
- 🤗 HuggingFace：[bigscience/bloom](https://huggingface.co/bigscience/bloom) · [bigscience/bloomz](https://huggingface.co/bigscience/bloomz)

---

### 2.13 Stability AI StableLM 系列

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| StableLM 3B | 2023-04 | 3B | 4K | CC-BY-SA-4.0 | 对话优化 |
| StableLM 2 | 2024-01 | 1.6/12B | 4K | Stability AI License | 性能提升 |

**官方资源**：
- 💻 GitHub：[Stability-AI/StableLM](https://github.com/Stability-AI/StableLM)
- 🤗 HuggingFace：[stabilityai](https://huggingface.co/stabilityai)

---

### 2.14 Databricks DBRX 系列

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| DBRX | 2024-03 | 132B (36B 激活) | 32K | DBRX License | 细粒度 MoE |

**官方资源**：
- 💻 GitHub：[databricks/dbrx](https://github.com/databricks/dbrx)
- 🤗 HuggingFace：[databricks/dbrx-instruct](https://huggingface.co/databricks/dbrx-instruct)

---

### 2.15 Snowflake Arctic 系列

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| Arctic | 2024-04 | 480B (17B 激活) | 4K | Apache 2.0 | Dense-MoE 混合 |

**官方资源**：
- 💻 GitHub：[Snowflake-Labs/snowflake-arctic](https://github.com/Snowflake-Labs/snowflake-arctic)
- 🤗 HuggingFace：[Snowflake](https://huggingface.co/Snowflake)

---

### 2.16 阿里 Qwen 系列 ♥K

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| Qwen | 2023-08 | 7/14B | 8K | Qianwen License | 基础版本 |
| Qwen 1.5 | 2024-02 | 0.5-110B | 32K | Apache 2.0 | 全面开源 |
| Qwen 2 | 2024-06 | 0.5-72B | 128K | Apache 2.0 | 多语言增强 |
| Qwen 2.5 | 2024-09 | 0.5-72B | 128K | Apache 2.0 | 编码/数学增强 |
| Qwen 2.5-1M | 2025-01 | 7/14B | 1M | Apache 2.0 | 超长上下文 |
| Qwen 3 | 2025-05 | 0.6-235B (22B 激活) | 32K | Apache 2.0 | 思考模式 |
| Qwen 3.5 | 2026-01 | 14-397B | 256K | Apache 2.0 | 全模态 |
| QwQ | 2024-11 | 32B | 32K | Apache 2.0 | 推理模型 |

**官方资源**：
- 📄 论文：[arXiv:2309.16609](https://arxiv.org/abs/2309.16609) (Qwen) · [arXiv:2407.10671](https://arxiv.org/abs/2407.10671) (Qwen 2) · [arXiv:2412.15115](https://arxiv.org/abs/2412.15115) (Qwen 2.5) · [arXiv:2505.09388](https://arxiv.org/abs/2505.09388) (Qwen 3)
- 💻 GitHub：[QwenLM/Qwen](https://github.com/QwenLM/Qwen) · [QwenLM/Qwen2.5](https://github.com/QwenLM/Qwen2.5) · [QwenLM/Qwen3](https://github.com/QwenLM/Qwen3) · [QwenLM/QwQ](https://github.com/QwenLM/QwQ)
- 🤗 HuggingFace：[Qwen](https://huggingface.co/Qwen)

---

### 2.17 DeepSeek 系列 🃏 Joker

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| DeepSeek-V1 | 2024-01 | 7/67B | 4K | DeepSeek License | 基础版本 |
| DeepSeek-V2 | 2024-05 | 236B (21B 激活) | 128K | DeepSeek License | MLA + DeepSeekMoE |
| DeepSeek-V2.5 | 2024-09 | 236B | 128K | DeepSeek License | 对话优化 |
| DeepSeek-V3 | 2024-12 | 671B (37B 激活) | 128K | DeepSeek License | FP8 训练 |
| DeepSeek-V3.1 | 2025-06 | 671B | 256K | DeepSeek License | 长上下文 |
| DeepSeek-V3.2 | 2026-02 | 未公开 | 512K | DeepSeek License | 推理增强 |
| DeepSeek-R1 | 2025-01 | 671B | 128K | MIT | **GRPO 强化学习** ⭐ |
| DeepSeek-R1-0528 | 2025-05 | 671B | 128K | MIT | 推理增强 |

**官方资源**：
- 📄 论文：[arXiv:2401.02954](https://arxiv.org/abs/2401.02954) (V1) · [arXiv:2405.04434](https://arxiv.org/abs/2405.04434) (V2) · [arXiv:2412.19437](https://arxiv.org/abs/2412.19437) (V3) · [arXiv:2501.12948](https://arxiv.org/abs/2501.12948) (R1)
- 💻 GitHub：[deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) · [deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1)
- 🤗 HuggingFace：[deepseek-ai](https://huggingface.co/deepseek-ai)
- 📖 API：https://platform.deepseek.com

---

### 2.18 智谱 GLM 系列 ♥Q

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| GLM-130B | 2022-10 | 130B | 2K | GLM License | 双向注意力 |
| ChatGLM | 2023-03 | 6B | 2K | ChatGLM License | 中英双语 |
| ChatGLM2 | 2023-06 | 6B | 32K | ChatGLM License | 长上下文 |
| ChatGLM3 | 2023-10 | 6B | 128K | ChatGLM License | 工具调用 |
| GLM-4 | 2024-01 | 未公开 | 128K | API | 多模态 |
| GLM-4.5 | 2025-02 | 未公开 | 256K | API | 推理增强 |
| GLM-4.6 | 2025-08 | 未公开 | 512K | API | Agent 能力 |
| GLM-5 | 2026-02 | 未公开 | 1M | API | AGI 进展 |

**官方资源**：
- 📄 论文：[arXiv:2210.02414](https://arxiv.org/abs/2210.02414) (GLM-130B) · [arXiv:2406.12793](https://arxiv.org/abs/2406.12793) (GLM-4) · [arXiv:2508.06471](https://arxiv.org/abs/2508.06471) (GLM-4.5)
- 💻 GitHub：[THUDM/GLM-4](https://github.com/THUDM/GLM-4) · [THUDM/ChatGLM3](https://github.com/THUDM/ChatGLM3)
- 🤗 HuggingFace：[THUDM](https://huggingface.co/THUDM)
- 📖 API：https://bigmodel.cn

---

### 2.19 百度 ERNIE 系列 ♥Q

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| ERNIE 3.0 | 2021-07 | 10B | 512 | Research | 知识增强 |
| ERNIE 3.5 | 2023-03 | 未公开 | 8K | API | 对话优化 |
| ERNIE 4.0 | 2023-10 | 未公开 | 128K | API | 多模态 |
| ERNIE 4.5 | 2024-06 | 未公开 | 256K | API | 推理增强 |
| ERNIE 5.0 | 2025-03 | 424B MoE | 512K | Apache 2.0 | 开源 MoE |

**官方资源**：
- 📄 论文：[arXiv:2107.02137](https://arxiv.org/abs/2107.02137) (ERNIE 3.0) · [arXiv:2602.04705](https://arxiv.org/abs/2602.04705) (ERNIE 5.0)
- 💻 GitHub：[PaddlePaddle/ERNIE](https://github.com/PaddlePaddle/ERNIE)
- 📖 API：https://yiyan.baidu.com

---

### 2.20 腾讯混元系列 ♥K

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| 混元 | 2023-09 | 未公开 | 32K | API | 多模态 |
| 混元-Large | 2024-11 | 389B MoE | 256K | Tencent Hunyuan License | 开源 MoE |

**官方资源**：
- 📄 论文：[arXiv:2411.02265](https://arxiv.org/abs/2411.02265)
- 💻 GitHub：[Tencent/Hunyuan-Large](https://github.com/Tencent/Hunyuan-Large) · [Tencent-Hunyuan/Tencent-Hunyuan-Large](https://github.com/Tencent-Hunyuan/Tencent-Hunyuan-Large)
- 🤗 HuggingFace：[tencent/Tencent-Hunyuan-Large](https://huggingface.co/tencent/Tencent-Hunyuan-Large)

---

### 2.21 字节豆包/Seed 系列 ♠Q / ♦J

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| 豆包 | 2023-08 | 未公开 | 128K | API | 多模态对话 |
| 豆包 2.0 | 2024-05 | 未公开 | 256K | API | 推理增强 |
| Seed1.5-VL | 2025-05 | 未公开 | 1M | Research | 超长视觉 |
| Seed-Coder | 2025-06 | 8B | 128K | Research | 代码生成 |

**官方资源**：
- 📄 论文：[arXiv:2505.07062](https://arxiv.org/abs/2505.07062) (Seed1.5-VL) · [arXiv:2506.03524](https://arxiv.org/abs/2506.03524) (Seed-Coder)
- 💻 GitHub：[ByteDance-Seed/Seed-Coder](https://github.com/ByteDance-Seed/Seed-Coder) · [ByteDance-Seed/Seed1.5-VL](https://github.com/ByteDance-Seed/Seed1.5-VL)
- 🤗 HuggingFace：[ByteDance-Seed](https://huggingface.co/ByteDance-Seed)

---

### 2.22 月之暗面 Kimi 系列 🃏 Joker

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| Kimi | 2023-10 | 未公开 | 200K | API | 超长上下文 |
| Kimi K1.5 | 2025-01 | 未公开 | 256K | API | 推理增强 |
| Kimi K2 | 2025-07 | 1T MoE (32B 激活) | 128K | MIT | **开源 MoE** ⭐ |
| Kimi K2.5 | 2026-02 | 未公开 | 512K | API | Agent 能力 |
| Kimi-VL | 2025-03 | 3B | 128K | Apache 2.0 | 视觉语言 |

**官方资源**：
- 📄 论文：[arXiv:2501.12599](https://arxiv.org/abs/2501.12599) (K1.5) · [arXiv:2507.20534](https://arxiv.org/abs/2507.20534) (K2) · [arXiv:2602.02276](https://arxiv.org/abs/2602.02276) (K2.5)
- 💻 GitHub：[MoonshotAI/Kimi-K2](https://github.com/MoonshotAI/Kimi-K2) · [MoonshotAI/kimi-k1.5](https://github.com/MoonshotAI/kimi-k1.5)
- 🤗 HuggingFace：[moonshotai](https://huggingface.co/moonshotai)
- 📖 API：https://platform.moonshot.cn

---

### 2.23 MiniMax 系列 ♥K

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| MiniMax | 2023-06 | 未公开 | 64K | API | 多模态 |
| MiniMax-M1 | 2025-06 | 456B MoE | 1M | MIT | 百万上下文 |
| MiniMax-M2.5 | 2025-12 | 未公开 | 2M | API | 推理增强 |

**官方资源**：
- 📄 论文：[arXiv:2501.08313](https://arxiv.org/abs/2501.08313) · [arXiv:2506.13585](https://arxiv.org/abs/2506.13585) (M1)
- 💻 GitHub：[MiniMax-AI/MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1)
- 🤗 HuggingFace：[MiniMaxAI](https://huggingface.co/MiniMaxAI)
- 📖 API：https://platform.minimax.io

---

### 2.24 面壁 MiniCPM 系列 ♥7

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| MiniCPM | 2024-02 | 2.4B | 4K | Apache 2.0 | 端侧部署 |
| MiniCPM-V | 2024-04 | 3B | 8K | Apache 2.0 | 多模态 |
| MiniCPM-V 2.6 | 2024-08 | 8B | 32K | Apache 2.0 | 视觉增强 |
| MiniCPM-o | 2024-12 | 8B | 128K | Apache 2.0 | 全模态 |
| MiniCPM 4 | 2025-06 | 4B | 128K | Apache 2.0 | 推理优化 |

**官方资源**：
- 📄 论文：[arXiv:2404.06395](https://arxiv.org/abs/2404.06395) (MiniCPM) · [arXiv:2506.07900](https://arxiv.org/abs/2506.07900) (MiniCPM 4)
- 💻 GitHub：[OpenBMB/MiniCPM](https://github.com/OpenBMB/MiniCPM) · [OpenBMB/MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) · [OpenBMB/MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o)
- 🤗 HuggingFace：[openbmb](https://huggingface.co/openbmb)

---

### 2.25 上海 AI Lab InternLM 系列 ♠Q

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| InternLM | 2023-07 | 7/20B | 8K | Apache 2.0 | 多阶段训练 |
| InternLM2 | 2024-01 | 7/20B | 200K | Apache 2.0 | 长上下文 |
| InternLM2.5 | 2024-07 | 7B | 1M | Apache 2.0 | 推理增强 |
| InternLM3 | 2024-12 | 8B | 128K | Apache 2.0 | 高效训练 |
| Intern-S1-Pro | 2026-03 | 未公开 | 256K | Research | AGI 进展 |

**官方资源**：
- 📄 论文：[arXiv:2403.17297](https://arxiv.org/abs/2403.17297) · [arXiv:2603.25040](https://arxiv.org/abs/2603.25040) (Intern-S1-Pro)
- 💻 GitHub：[InternLM/InternLM](https://github.com/InternLM/InternLM)
- 🤗 HuggingFace：[internlm](https://huggingface.co/internlm)

---

### 2.26 百川 Baichuan 系列 ♥Q

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| Baichuan-7B | 2023-06 | 7B | 4K | Apache 2.0 | 中文优化 |
| Baichuan-13B | 2023-07 | 13B | 4K | Apache 2.0 | 性能提升 |
| Baichuan2 | 2023-09 | 7/13B | 4K | Apache 2.0 | 对话优化 |
| Baichuan-M1 | 2025-01 | 未公开 | 128K | API | 多模态 |
| Baichuan-M2 | 2025-09 | 未公开 | 256K | API | 推理增强 |
| Baichuan-M3-235B | 2026-02 | 235B | 512K | API | 旗舰模型 |
| Baichuan-Omni-1.5 | 2025-01 | 7B | 32K | Apache 2.0 | 全模态 |

**官方资源**：
- 📄 论文：[arXiv:2309.10305](https://arxiv.org/abs/2309.10305) (Baichuan 2) · [arXiv:2501.15368](https://arxiv.org/abs/2501.15368) (Baichuan-Omni-1.5) · [arXiv:2502.12671](https://arxiv.org/abs/2502.12671) (Baichuan-M1) · [arXiv:2509.02208](https://arxiv.org/abs/2509.02208) (Baichuan-M2) · [arXiv:2602.06570](https://arxiv.org/abs/2602.06570) (Baichuan-M3)
- 💻 GitHub：[baichuan-inc/Baichuan2](https://github.com/baichuan-inc/Baichuan2) · [baichuan-inc/Baichuan-M3-235B](https://github.com/baichuan-inc/Baichuan-M3-235B)
- 🤗 HuggingFace：[baichuan-inc](https://huggingface.co/baichuan-inc)

---

### 2.27 零一万物 Yi 系列 ♥10

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| Yi | 2023-11 | 6/34B | 4K | Yi License | 高质量数据 |
| Yi-1.5 | 2024-05 | 6/9/34B | 4K | Apache 2.0 | 性能提升 |
| Yi-34B-200K | 2024-01 | 34B | 200K | Yi License | 长上下文 |
| Yi-VL | 2024-01 | 6/34B | 4K | Yi License | 视觉语言 |

**官方资源**：
- 📄 论文：[arXiv:2403.04652](https://arxiv.org/abs/2403.04652)
- 💻 GitHub：[01-ai/Yi](https://github.com/01-ai/Yi) · [01-ai/Yi-1.5](https://github.com/01-ai/Yi-1.5)
- 🤗 HuggingFace：[01-ai](https://huggingface.co/01-ai)

---

### 2.28 阶跃星辰 Step 系列

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| Step-1 | 2024-03 | 未公开 | 128K | API | 多模态 |
| Step-2 | 2024-08 | 未公开 | 256K | API | 推理增强 |
| Step-3.5-Flash | 2025-04 | 未公开 | 256K | API | 高效推理 |

**官方资源**：
- 💻 GitHub：[stepfun-ai/Step-3.5-Flash](https://github.com/stepfun-ai/Step-3.5-Flash)
- 🤗 HuggingFace：[stepfun-ai](https://huggingface.co/stepfun-ai)
- 📖 API：https://platform.stepfun.com

---

### 2.29 科大讯飞 星火系列

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| 星火 1.5 | 2023-06 | 未公开 | 8K | API | 中文对话 |
| 星火 2.0 | 2023-08 | 未公开 | 16K | API | 多模态 |
| 星火 3.0 | 2023-10 | 未公开 | 32K | API | 性能提升 |
| 星火 3.5 | 2024-01 | 未公开 | 128K | API | 长上下文 |
| 星火 4.0 | 2024-06 | 未公开 | 256K | API | 推理增强 |

**官方资源**：
- 📖 API：https://xinghuo.xfyun.cn

---

### 2.30 360智脑系列

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 |
|:---|:---|:---|:---|:---|:---|
| 360Zhinao-7B | 2024-04 | 7B | 360K | Apache 2.0 | 超长上下文 |
| 360Zhinao2 | 2024-11 | 7B | 128K | Apache 2.0 | 性能提升 |

**官方资源**：
- 💻 GitHub：[Qihoo360/360zhinao](https://github.com/Qihoo360/360zhinao) · [Qihoo360/360zhinao2](https://github.com/Qihoo360/360zhinao2)
- 🤗 HuggingFace：[Qihoo360/360Zhinao-7B-Chat-360K](https://huggingface.co/Qihoo360/360Zhinao-7B-Chat-360K)

---

## 3. 专项领域模型

### 3.1 代码专项模型 ♦J

| 模型 | 参数规模 | 上下文 | 许可协议 | 论文/资源 |
|:---|:---|:---|:---|:---|
| StarCoder2 | 3/7/15B | 16K | BigCode License | [arXiv:2402.19173](https://arxiv.org/abs/2402.19173) · [GitHub](https://github.com/bigcode-project/starcoder2) |
| DeepSeek-Coder | 1.3/6.7/33B | 16K | DeepSeek License | [arXiv:2401.14196](https://arxiv.org/abs/2401.14196) · [GitHub](https://github.com/deepseek-ai/DeepSeek-Coder) |
| DeepSeek-Coder-V2 | 16/236B | 128K | DeepSeek License | [arXiv:2406.11931](https://arxiv.org/abs/2406.11931) · [GitHub](https://github.com/deepseek-ai/DeepSeek-Coder-V2) |
| CodeLlama | 7/13/34/70B | 16K | Llama 2 License | [GitHub](https://github.com/meta-llama/codellama) · [HuggingFace](https://huggingface.co/codellama) |
| Qwen2.5-Coder | 1.5/7/14/32B | 128K | Apache 2.0 | [arXiv:2409.12186](https://arxiv.org/abs/2409.12186) · [GitHub](https://github.com/QwenLM/Qwen2.5-Coder) |
| CodeGemma | 2/7B | 8K | Gemma License | [arXiv:2406.11409](https://arxiv.org/abs/2406.11409) · [GitHub](https://github.com/google-deepmind/codegemma) |
| Codestral | 22B | 32K | MNPL | [HuggingFace](https://huggingface.co/mistralai/Codestral-22B-v0.1) |
| WizardCoder | 15/34B | 8K | Llama 2 License | [GitHub](https://github.com/nlpxucan/WizardLM) · [HuggingFace](https://huggingface.co/WizardLM) |
| Magicoder | 7B | 16K | Apache 2.0 | [GitHub](https://github.com/ise-uiuc/magicoder) · [HuggingFace](https://huggingface.co/ise-uiuc) |
| OpenCoder | 1.5/8B | 8K | Apache 2.0 | [arXiv:2411.04905](https://arxiv.org/abs/2411.04905) · [GitHub](https://github.com/OpenCoder-llm/OpenCoder-llm) |
| Seed-Coder | 8B | 128K | Research | [arXiv:2506.03524](https://arxiv.org/abs/2506.03524) · [GitHub](https://github.com/ByteDance-Seed/Seed-Coder) |
| CodeGeeX4 | 9B | 128K | CodeGeeX License | [GitHub](https://github.com/THUDM/CodeGeeX4) · [HuggingFace](https://huggingface.co/THUDM/codegeex4-all-9b) |

---

### 3.2 数学推理模型 ♦J

| 模型 | 参数规模 | 上下文 | 许可协议 | 论文/资源 |
|:---|:---|:---|:---|:---|
| DeepSeekMath | 7B | 4K | DeepSeek License | [arXiv:2402.03300](https://arxiv.org/abs/2402.03300) · [GitHub](https://github.com/deepseek-ai/DeepSeekMath) |
| Qwen2.5-Math | 1.5/7/72B | 128K | Apache 2.0 | [arXiv:2409.12122](https://arxiv.org/abs/2409.12122) · [arXiv:2501.07301](https://arxiv.org/abs/2501.07301) · [GitHub](https://github.com/QwenLM/Qwen2.5-Math) |
| InternLM-Math | 7/20B | 32K | Apache 2.0 | [GitHub](https://github.com/InternLM/InternLM-Math) · [HuggingFace](https://huggingface.co/internlm/internlm2-math-plus-7b) |
| Llemma | 7/34B | 4K | Llama License | [arXiv:2310.10631](https://arxiv.org/abs/2310.10631) · [GitHub](https://github.com/eleutherai/llemma) |
| NuminaMath | 7B | 4K | Apache 2.0 | [GitHub](https://github.com/project-numina/aimo-progress-prize) · [HuggingFace](https://huggingface.co/AI-MO/NuminaMath-7B-CoT) |
| MetaMath | 7/13/70B | 4K | Llama License | [GitHub](https://github.com/meta-math/MetaMath) |
| MathCoder | 7/13/34B | 4K | Apache 2.0 | [GitHub](https://github.com/mathllm/MathCoder) |

---

### 3.3 多模态 VLM 模型 ♠ / ♣

| 模型 | 参数规模 | 上下文 | 许可协议 | 论文/资源 |
|:---|:---|:---|:---|:---|
| LLaVA | 7/13B | 4K | Apache 2.0 | [arXiv:2304.08485](https://arxiv.org/abs/2304.08485) · [GitHub](https://github.com/haotian-liu/LLaVA) |
| LLaVA-NeXT | 7/13/34B | 32K | Apache 2.0 | [arXiv:2310.03744](https://arxiv.org/abs/2310.03744) · [GitHub](https://github.com/LLaVA-VL/LLaVA-NeXT) |
| LLaVA-OneVision-1.5 | 7/72B | 128K | Apache 2.0 | [arXiv:2509.23661](https://arxiv.org/abs/2509.23661) · [GitHub](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-1.5) |
| Qwen2-VL | 2/7/72B | 32K | Apache 2.0 | [arXiv:2409.12191](https://arxiv.org/abs/2409.12191) · [GitHub](https://github.com/QwenLM/Qwen2-VL) |
| Qwen3-VL | 8B | 128K | Apache 2.0 | [arXiv:2511.21631](https://arxiv.org/abs/2511.21631) · [GitHub](https://github.com/QwenLM/Qwen3-VL) |
| InternVL2 | 2/8/26/76B | 32K | Apache 2.0 | [arXiv:2412.05271](https://arxiv.org/abs/2412.05271) · [GitHub](https://github.com/OpenGVLab/InternVL) |
| InternVL3 | 8B | 128K | Apache 2.0 | [arXiv:2504.10479](https://arxiv.org/abs/2504.10479) · [HuggingFace](https://huggingface.co/OpenGVLAB/InternVL3-8B) |
| CogVLM2 | 8/19B | 8K | CogVLM License | [GitHub](https://github.com/THUDM/CogVLM2) |
| MiniCPM-V | 3/8B | 32K | Apache 2.0 | [GitHub](https://github.com/OpenBMB/MiniCPM-V) · [HuggingFace](https://huggingface.co/openbmb/MiniCPM-V-2_6) |
| PaliGemma | 3B | 8K | Gemma License | [HuggingFace](https://huggingface.co/google/paligemma-3b-mix-224) |
| Pixtral | 12B | 128K | Apache 2.0 | [HuggingFace](https://huggingface.co/mistralai/Pixtral-12B-2409) |
| SmolVLM | 2B | 8K | Apache 2.0 | [arXiv:2504.05299](https://arxiv.org/abs/2504.05299) |
| Molmo | 7B | 4K | Apache 2.0 | [GitHub](https://github.com/allenai/molmo) · [HuggingFace](https://huggingface.co/allenai/Molmo-7B-D-0924) |
| Idefics3 | 8B | 8K | Apache 2.0 | [HuggingFace](https://huggingface.co/HuggingFaceM4/Idefics3-8B-Llama3) |

---

### 3.4 小语言模型 SLM ♥2~7

| 模型 | 参数规模 | 上下文 | 许可协议 | 论文/资源 |
|:---|:---|:---|:---|:---|
| TinyLlama | 1.1B | 2K | Apache 2.0 | [arXiv:2401.02385](https://arxiv.org/abs/2401.02385) · [GitHub](https://github.com/jzhang38/TinyLlama) |
| SmolLM2 | 135M/360M/1.7B | 8K | Apache 2.0 | [arXiv:2502.02737](https://arxiv.org/abs/2502.02737) · [GitHub](https://github.com/huggingface/smollm) |
| TinyGPT-V | 3B | 2K | Apache 2.0 | [arXiv:2312.16862](https://arxiv.org/abs/2312.16862) |
| MobileLLM | 125M/350M/1B | 2K | Research | [GitHub](https://github.com/facebookresearch/MobileLLM) |
| Phi-3-mini | 3.8B | 128K | MIT | [arXiv:2404.14219](https://arxiv.org/abs/2404.14219) · [HuggingFace](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) |
| Phi-4-mini | 3.8B | 128K | MIT | [arXiv:2504.21233](https://arxiv.org/abs/2504.21233) · [HuggingFace](https://huggingface.co/microsoft/phi-4-mini) |
| OpenELM | 270M/450M/1.1B/3B | 2K | Apple License | [HuggingFace](https://huggingface.co/apple/OpenELM) |
| MiniCPM | 1.2/2.4B | 4K | Apache 2.0 | [arXiv:2404.06395](https://arxiv.org/abs/2404.06395) · [GitHub](https://github.com/OpenBMB/MiniCPM) |
| Gemma-2-2B | 2B | 8K | Gemma License | [arXiv:2408.00118](https://arxiv.org/abs/2408.00118) · [HuggingFace](https://huggingface.co/google/gemma-2-2b) |
| StableLM-2-1.6B | 1.6B | 4K | Stability AI License | [HuggingFace](https://huggingface.co/stabilityai/stablelm-2-1_6b) |

---

### 3.5 MoE 架构模型 ♥K

| 模型 | 总参数 | 激活参数 | 专家数 | 许可协议 | 论文/资源 |
|:---|:---|:---|:---|:---|:---|
| Mixtral 8x7B | 46.7B | 12.9B | 8 | Apache 2.0 | [arXiv:2401.04088](https://arxiv.org/abs/2401.04088) |
| Mixtral 8x22B | 176B | 39B | 8 | Apache 2.0 | [HuggingFace](https://huggingface.co/mistralai) |
| DeepSeek-V2 | 236B | 21B | 160 | DeepSeek License | [arXiv:2405.04434](https://arxiv.org/abs/2405.04434) |
| DeepSeek-V3 | 671B | 37B | 256 | DeepSeek License | [arXiv:2412.19437](https://arxiv.org/abs/2412.19437) |
| Qwen-MoE | 14.3B | 2.7B | 60 | Apache 2.0 | [GitHub](https://github.com/QwenLM/Qwen) |
| OpenMoE | 8B | 2B | 32 | Apache 2.0 | [arXiv:2402.01739](https://arxiv.org/abs/2402.01739) |
| OLMoE | 6.9B | 1.3B | 64 | Apache 2.0 | [arXiv:2409.02060](https://arxiv.org/abs/2409.02060) |
| Skywork-MoE | 146B | 22B | 16 | Skywork License | [arXiv:2406.06563](https://arxiv.org/abs/2406.06563) · [GitHub](https://github.com/SkyworkAI/Skywork) |
| DBRX | 132B | 36B | 16 | DBRX License | [GitHub](https://github.com/databricks/dbrx) |
| Arctic | 480B | 17B | 128 | Apache 2.0 | [GitHub](https://github.com/Snowflake-Labs/snowflake-arctic) |

---

### 3.6 新架构模型（SSM/RNN/Hybrid）🃏 Joker

| 模型 | 架构 | 参数规模 | 上下文 | 许可协议 | 论文/资源 |
|:---|:---|:---|:---|:---|:---|
| Mamba | SSM | 130M-2.8B | ∞ | Apache 2.0 | [arXiv:2312.00752](https://arxiv.org/abs/2312.00752) · [GitHub](https://github.com/state-spaces/mamba) |
| Mamba-2 | SSM | 130M-2.8B | ∞ | Apache 2.0 | [arXiv:2405.21060](https://arxiv.org/abs/2405.21060) |
| Mamba-3 | SSM | 7B | ∞ | Apache 2.0 | [arXiv:2603.15569](https://arxiv.org/abs/2603.15569) |
| RWKV-6 | RNN | 1.6/3/7/14B | ∞ | Apache 2.0 | [GitHub](https://github.com/BlinkDL/RWKV-LM) |
| RWKV-7 | RNN | 0.1-7B | ∞ | Apache 2.0 | [arXiv:2503.14456](https://arxiv.org/abs/2503.14456) · [GitHub](https://github.com/RWKV/RWKV-v7) |
| xLSTM | xLSTM | 7B | 16K | Research | [arXiv:2510.02228](https://arxiv.org/abs/2510.02228) · [HuggingFace](https://huggingface.co/NX-AI/xLSTM-7b) |
| RecurrentGemma | Hybrid | 2/9B | 8K | Gemma License | [arXiv:2404.07839](https://arxiv.org/abs/2404.07839) · [GitHub](https://github.com/google-deepmind/recurrentgemma) |
| Jamba | Hybrid | 52B | 256K | Jamba License | [GitHub](https://github.com/AI21Labs/Jamba) · [HuggingFace](https://huggingface.co/ai21labs/Jamba-v0.1) |
| Jamba 1.5 | Hybrid | 52/398B | 256K | Jamba License | [HuggingFace](https://huggingface.co/ai21labs/Jamba-1.5-Large) |
| Falcon-H1 | Hybrid | 1.5/3.5/7/34B | 256K | Apache 2.0 | [arXiv:2507.22448](https://arxiv.org/abs/2507.22448) · [GitHub](https://github.com/tiiuae/Falcon-H1) |
| Hyena | Subquadratic | 未公开 | ∞ | Research | [arXiv:2302.10865](https://arxiv.org/abs/2302.10865) |
| RetNet | Retention | 1.3/2.7/6.7B | ∞ | Research | [arXiv:2307.08621](https://arxiv.org/abs/2307.08621) |

---

### 3.7 推理增强模型 🃏 Joker

| 模型 | 参数规模 | 上下文 | 许可协议 | 核心技术 | 论文/资源 |
|:---|:---|:---|:---|:---|:---|
| OpenAI o1 | 未公开 | 128K | API | Chain-of-Thought | [arXiv:2412.16720](https://arxiv.org/abs/2412.16720) |
| OpenAI o3 | 未公开 | 256K | API | Deep Reasoning | System Card |
| OpenAI o4-mini | 未公开 | 128K | API | Efficient Reasoning | System Card |
| DeepSeek-R1 | 671B | 128K | MIT | GRPO 强化学习 | [arXiv:2501.12948](https://arxiv.org/abs/2501.12948) |
| QwQ | 32B | 32K | Apache 2.0 | 思维链推理 | [GitHub](https://github.com/QwenLM/QwQ) |
| Kimi K2 | 1T MoE | 128K | MIT | Muon 优化器 | [arXiv:2507.20534](https://arxiv.org/abs/2507.20534) |
| Kimi k1.5 | 未公开 | 256K | API | Long CoT | [arXiv:2501.12599](https://arxiv.org/abs/2501.12599) |

---

### 3.8 Agent/工具调用模型 ♣J

| 模型 | 参数规模 | 上下文 | 许可协议 | 论文/资源 |
|:---|:---|:---|:---|:---|
| Qwen-Agent | 7/14/72B | 128K | Apache 2.0 | [GitHub](https://github.com/QwenLM/Qwen-Agent) |
| ToolLLaMA | 7B | 8K | Apache 2.0 | [arXiv:2310.05146](https://arxiv.org/abs/2310.05146) · [HuggingFace](https://huggingface.co/ToolBench/ToolLLaMA-7b) |
| Gorilla | 7B | 4K | Apache 2.0 | [arXiv:2305.15334](https://arxiv.org/abs/2305.15334) · [GitHub](https://github.com/ShishirPatil/gorilla) |
| AgentTuning | 7/13/70B | 4K | Apache 2.0 | [GitHub](https://github.com/THUDM/AgentTuning) |
| ToolBench | 7B | 4K | Apache 2.0 | [GitHub](https://github.com/OpenBMB/ToolBench) · [THUDM/ToolBench](https://github.com/THUDM/ToolBench) |

---

### 3.9 嵌入模型 ♣

| 模型 | 参数规模 | 维度 | 许可协议 | 论文/资源 |
|:---|:---|:---|:---|:---|
| BGE-M3 | 568M | 1024 | MIT | [arXiv:2402.03216](https://arxiv.org/abs/2402.03216) · [GitHub](https://github.com/FlagOpen/FlagEmbedding) |
| Qwen3-Embedding | 0.6/4/8B | 3584 | Apache 2.0 | [arXiv:2506.05176](https://arxiv.org/abs/2506.05176) · [GitHub](https://github.com/QwenLM/Qwen3-Embedding) |
| GTE-Qwen2 | 7B | 3584 | Apache 2.0 | [HuggingFace](https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct) |
| E5-Mistral | 7B | 4096 | MIT | [HuggingFace](https://huggingface.co/intfloat/e5-mistral-7b-instruct) |
| Nomic Embed v2 | 137M | 768 | Apache 2.0 | [HuggingFace](https://huggingface.co/nomic-ai) |
| Jina Embeddings | 137M-1.3B | 768-8192 | Apache 2.0 | [HuggingFace](https://huggingface.co/jinaai) |

---

### 3.10 医疗/科学模型 ♦10

| 模型 | 参数规模 | 领域 | 许可协议 | 论文/资源 |
|:---|:---|:---|:---|:---|
| Med-PaLM 2 | 未公开 | 医疗 | API | Google Research |
| BioMistral | 7B | 生物医学 | Apache 2.0 | [arXiv:2402.10373](https://arxiv.org/abs/2402.10373) · [GitHub](https://github.com/BioMistral/BioMistral) |
| PMC-LLaMA | 7/13B | 医学文献 | Llama License | Research |
| Galactica | 120B | 科学 | CC-BY-NC-4.0 | [GitHub](https://github.com/paperswithcode/galai) · [HuggingFace](https://huggingface.co/facebook/galactica-120b) |
| SciGLM | 6B | 科学 | Apache 2.0 | [arXiv:2401.07950](https://arxiv.org/abs/2401.07950) · [GitHub](https://github.com/THUDM/SciGLM) |
| HuatuoGPT-o1 | 8B | 医疗推理 | Apache 2.0 | [arXiv:2412.18925](https://arxiv.org/abs/2412.18925) |
| MedGemma | 2/9B | 医疗 | Gemma License | [arXiv:2507.05201](https://arxiv.org/abs/2507.05201) · [HuggingFace](https://huggingface.co/google/medgemma) |
| FinGPT | 7B | 金融 | Apache 2.0 | Research |
| ChatLaw | 13B | 法律 | Apache 2.0 | [arXiv:2411.10137](https://arxiv.org/abs/2411.10137) |

---

### 3.11 音频语言模型 ♣J

| 模型 | 参数规模 | 模态 | 许可协议 | 论文/资源 |
|:---|:---|:---|:---|:---|
| Qwen2-Audio | 7B | 语音+文本 | Apache 2.0 | [GitHub](https://github.com/QwenLM/Qwen2-Audio) · [HuggingFace](https://huggingface.co/Qwen/Qwen2-Audio-7B-Instruct) |
| GLM-4-Voice | 9B | 语音+文本 | GLM License | [GitHub](https://github.com/THUDM/GLM-4-Voice) |
| SALMONN | 7/13B | 语音+音频+文本 | Apache 2.0 | [GitHub](https://github.com/bytedance/SALMONN) |
| Mini-Omni | 7B | 全模态 | Apache 2.0 | [GitHub](https://github.com/gpt-omni/mini-omni) |
| MusicGen | 1.5B | 音乐生成 | CC-BY-NC-4.0 | [arXiv:2306.05284](https://arxiv.org/abs/2306.05284) · [GitHub](https://github.com/facebookresearch/audiocraft) |
| Seed-TTS | 未公开 | 语音合成 | Research | [arXiv:2406.02430](https://arxiv.org/abs/2406.02430) · [GitHub](https://github.com/bytedance/Seed-TTS) |
| Whisper | 1.5B | 语音识别 | MIT | [GitHub](https://github.com/openai/whisper) |

---

### 3.12 检索增强 RAG 模型 ♣10

| 模型 | 参数规模 | 特性 | 许可协议 | 论文/资源 |
|:---|:---|:---|:---|:---|
| Self-RAG | 7/13B | 自适应检索 | Apache 2.0 | [arXiv:2310.11511](https://arxiv.org/abs/2310.11511) · [GitHub](https://github.com/AkariAsai/self-rag) |
| CRAG | 7B | 纠正检索 | Apache 2.0 | [GitHub](https://github.com/HuskyInu/Corrective-RAG) |
| Retro | 7B | 检索增强 | Research | [GitHub](https://github.com/google-deepmind/retro) |
| StreamingLLM | 7B | 流式处理 | MIT | [arXiv:2309.17453](https://arxiv.org/abs/2309.17453) |
| REALM | 340M | 知识检索 | Apache 2.0 | [GitHub](https://github.com/google-research/language) |

---

## 4. 技术对比

### 4.1 性能基准对比（2026年4月）

| 模型 | MMLU-Pro | HumanEval | GSM8K | GPQA Diamond | ARC-AGI-2 | 🃏 标记 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| GPT-5 | 92.1% | 96.8% | 98.5% | 78.3% | 21.2% | ♥A |
| Claude 4.6 Opus | 91.8% | 95.2% | 97.8% | 95.4% | 19.8% | ♥A |
| Gemini 3.1 | 90.5% | 94.1% | 97.2% | 76.8% | 18.5% | ♥A |
| o4-mini | 89.2% | 93.5% | 96.8% | 74.2% | 17.2% | ♥A |
| LLaMA 4 Maverick | 88.5% | 91.2% | 95.5% | 72.1% | 15.8% | ♥K |
| Qwen3-235B | 87.8% | 90.8% | 94.8% | 71.5% | 14.5% | ♥K |
| DeepSeek-V3 | 86.5% | 89.5% | 93.2% | 70.2% | 13.2% | ♥K |
| DeepSeek-R1 | 88.2% | 92.1% | 96.2% | 73.8% | 16.5% | 🃏 |
| Kimi K2 | 85.8% | 88.2% | 92.5% | 69.5% | 12.8% | 🃏 |
| GLM-5 | 84.5% | 87.5% | 91.8% | 68.2% | 11.5% | ♥Q |

### 4.2 API 定价对比（2026年4月，每百万 Token）

| 模型 | 输入价格 | 输出价格 | 备注 | 🃏 标记 |
|:---|:---:|:---:|:---|:---:|
| GPT-5 | $30.00 | $60.00 | 最强性能 | ♥A |
| GPT-4.5 | $15.00 | $45.00 | 平衡选择 | ♥A |
| Claude 4.6 Opus | $25.00 | $75.00 | 长上下文 | ♥A |
| Gemini 3.1 Pro | $12.50 | $37.50 | 多模态 | ♥A |
| DeepSeek-V3 | $0.27 | $1.10 | 极致性价比 | ♥K |
| DeepSeek-R1 | $0.55 | $2.19 | 推理模型 | 🃏 |
| Qwen-Plus | $0.80 | $2.00 | 阿里云 | ♥K |
| GLM-4 | $1.00 | $2.00 | 智谱 | ♥Q |
| Kimi | $1.20 | $6.00 | 超长上下文 | 🃏 |

### 4.3 许可协议汇总

| 许可类型 | 代表模型 | 商用限制 | 🃏 分布 |
|:---|:---|:---|:---|
| Apache 2.0 | Qwen、Mistral、OLMo、Falcon | 无限制 | ♥2 ~ ♥K |
| MIT | DeepSeek-R1、Phi、Kimi K2 | 无限制 | ♥10, 🃏 |
| Llama License | LLaMA 3/4 | MAU>7 亿需授权 | ♥K |
| Gemma License | Gemma | 研究+商用 | ♥10 |
| CC-BY-NC-4.0 | BLOOM、MusicGen | 非商用 | ♥Q |
| 研究许可 | 部分学术模型 | 仅研究用途 | 各种 |
| API Only | GPT、Claude、Gemini | 按调用计费 | ♥A |

---

## 5. 部署指南

### 5.1 硬件配置参考

| 模型规模 | 推荐 GPU | 显存需求 | 量化后显存 | 🃏 点数 |
|:---|:---|:---|:---|:---:|
| 1-3B | RTX 4060 | 8GB | 4GB (INT4) | 2-7 |
| 7B | RTX 4070 | 16GB | 6GB (INT4) | 8-10 |
| 13B | RTX 4080 | 24GB | 8GB (INT4) | J |
| 34B | RTX 4090 | 48GB | 18GB (INT4) | Q |
| 70B | 2×RTX 4090/A100 | 96GB | 35GB (INT4) | Q/K |
| 70B MoE | A100 80GB | 80GB | 40GB (INT4) | K |
| 405B | 8×H100 | 640GB | 160GB (INT4) | K |
| 671B MoE | 8×H100 | 640GB | 200B (FP8) | K |

### 5.2 推理框架对比

| 框架 | 特点 | 适用场景 | GitHub |
|:---|:---|:---|:---|
| vLLM | PagedAttention、高吞吐 | 生产部署 | [vllm-project/vllm](https://github.com/vllm-project/vllm) |
| TGI | HuggingFace 官方、Docker | 企业级 | [huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference) |
| Ollama | 一键部署、本地运行 | 个人开发 | [ollama/ollama](https://github.com/ollama/ollama) |
| llama.cpp | CPU 推理、量化优化 | 边缘设备 | [ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) |
| SGLang | RadixAttention、高效 | 研究实验 | [sgl-project/sglang](https://github.com/sgl-project/sglang) |
| TensorRT-LLM | NVIDIA 优化、低延迟 | NVIDIA GPU | [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) |
| LMDeploy | InternLM 团队、多模态 | 国产模型 | [InternLM/lmdeploy](https://github.com/InternLM/lmdeploy) |

### 5.3 量化方案对比

| 方案 | 精度损失 | 压缩比 | 推理速度 | 工具 |
|:---|:---:|:---:|:---:|:---|
| FP16 | 无 | 2× | 基准 | 原生 |
| FP8 | 极小 | 2× | 1.2× | TensorRT-LLM |
| INT8 | 小 | 4× | 1.5× | bitsandbytes |
| AWQ | 小 | 4× | 1.8× | [mit-han-lab/llm-awq](https://github.com/mit-han-lab/llm-awq) |
| GPTQ | 中等 | 4× | 1.6× | [AutoGPTQ/AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ) |
| GGUF | 中等 | 4-8× | 2× | llama.cpp |
| bitsandbytes | 小 | 4-8× | 1.4× | [bitsandbytes-foundation/bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) |
| ExLlamaV2 | 中等 | 2-6× | 2.5× | [turboderp/exllamav2](https://github.com/turboderp/exllamav2) |

### 5.4 代码示例

**vLLM 部署**：
```python
from vllm import LLM, SamplingParams

llm = LLM(model="Qwen/Qwen2.5-72B-Instruct", tensor_parallel_size=4)
sampling_params = SamplingParams(temperature=0.7, max_tokens=2048)
outputs = llm.generate(["请介绍一下大语言模型的发展历程"], sampling_params)
print(outputs[0].outputs[0].text)
```

**Ollama 部署**：
```bash
# 安装
curl -fsSL https://ollama.com/install.sh | sh
# 运行
ollama run qwen2.5:72b
```

**llama.cpp 量化**：
```bash
# 量化为 Q4_K_M
./quantize model.gguf model-q4_k_m.gguf Q4_K_M
# 运行
./main -m model-q4_k_m.gguf -p "Hello, world!"
```

**TGI Docker 部署**：
```bash
docker run --gpus all -p 8080:80 \
  -v /path/to/model:/model \
  ghcr.io/huggingface/text-generation-inference:latest \
  --model-id /model --num-shard 4
```

---

## 6. 📈 LLM 发展时间线

> 从 2017 年 Transformer 诞生到 2026 年 AGI 级模型，大语言模型的发展可以用一副扑克牌的演进历程来理解。

### 6.1 里程碑事件

```
2017 ┃────────── Attention Is All You Need (Transformer) ──────┃
      │                                                           │
2018 ┃ GPT-1 ♥2  BERT ♠3  T5 ♣4                                │
      │   (117M)    (110M)   (220M)                               │
2019 ┃ GPT-2 ♥5  XLNet ♥6  ALBERT                              │
      │   (1.5B)   (340M)                                        │
2020 ┃ GPT-3 ♥K(175B)  GPT-J ♥8(6B)                            │
      │   Few-shot革命                                            │
2021 ┃ GLM-130B ♥Q  Codex ♦J  ERNIE 3.0                         │
      │   PaLM ♥K(540B)                                           │
2022 ┃ ChatGLM ♥7  Galactica ♦10  LLaMA 1 ♥Q                     │
      │   (开源爆发元年)                                           │
2023 ┃ GPT-4 ♥A  Claude 1 ♥Q  LLaMA 2 ♥K                        │
      │   Mistral 7B ♥J  GPT-4-turbo  DeepSeek-V1                │
      │   (闭源 vs 开源 分野)                                      │
2024 ┃ Claude 3.5  LLaMA 3/3.1  Gemma 2  Qwen 2/2.5              │
      │   DeepSeek-V2/V3  Mamba 🃏  o1 🃏  Phi-3                 │
      │   (MoE + SSM + 推理 三大革命)                             │
2025 ┃ GPT-5 ♥A  Claude 4/4.5  LLaMA 4 Behemoth(2T)♥K           │
      │   DeepSeek-R1 🃏(GRPO)  Kimi K2 🃏  Grok-3               │
      │   Qwen 3/3.5  Gemini 2.5  Mamba-3  RWKV-7               │
      │   (开源首次逼近闭源 SOTA)                                  │
2026 ┃ Claude 4.6 ♥A  Gemini 3.1  GLM-5  Kimi K2.5              │
      │   Intern-S1-Pro  Baichuan-M3  MiniMax-M2.5               │
      │   Qwen3.5  DeepSeek-V3.2                                 │
      ┃────────── AGI 能力加速显现 ──────────────────────────────┃
```

### 6.2 代际演进特征

| 时代 | 时间段 | 核心特征 | 关键突破 | 代表模型 | 🃏 花色 |
|:---|:---|:---|:---|:---|:---|
| **前Transformer** | <2017 | RNN/LSTM/CNN为主 | 序列建模局限 | — | — |
| **预训练时代** | 2018-2020 | 大规模无监督预训练 | Few-shot学习 | GPT-3, BERT, T5 | ♥2~K |
| **指令微调时代** | 2021-2022 | RLHF对齐 + 开源爆发 | In-context Learning | LLaMA, ChatGLM, GPT-4 | ♥J~A |
| **多模态+效率** | 2023 | 视觉语言 + 小模型 | 多模态融合, 边缘部署 | GPT-4V, LLaVA, Phi-3 | ♠Q, ♥7 |
| **架构创新** | 2024 | MoE + SSM + 推理增强 | 稀疏激活, 线性复杂度, CoT | DeepSeek-V3, Mamba, o1 | 🃏 Joker |
| **AGI前夜** | 2025 | 超大规模 + 推理突破 | 开源=闭源, 长上下文 | GPT-5, LLaMA4, R1, K2 | ♥A, 🃏 |
| **智能涌现** | 2026→ | Agent能力 + 全模态 | 自主规划, 实时推理 | Claude 4.6, GLM-5 | ♥A |

### 6.3 关键技术节点

```
注意力机制 (2017)
  └─→ 自回归预训练 (GPT, 2018)
       └─→ Scale-up (GPT-3 175B, 2020)  ──┐
                                             ├─→ 并行发展路径:
        RLHF 对齐 (InstructGPT, 2022) ──────┤  1️⃣ 闭源SOTA路线 → GPT-4/5, Claude
                                             │  2️⃣ 开源路线 → LLaMA → Mistral → Qwen
        LLaMA 开源引爆 (2023-02) ──────────┤  3️⃣ 架构创新 → Mamba, RWKV
                                             │  4️⃣ 推理增强 → o1, R1, QwQ
        MoE 效率突破 (Mixtral, 2023-12) ────┤  5️⃣ 多模态统一 → GPT-4V, Gemi
                                             │
        GRPO 纯RL推理 (DeepSeek-R1, 2025) ──┘
```

---

## 7. 🔬 训练方法与对齐技术

> 模型的"性格"由训练方法决定——同样的骨架，不同的训练方式会产生截然不同的模型。

### 7.1 预训练范式

| 方法 | 核心思想 | 代表模型 | 优势 | 局限 |
|:---|:---|:---|:---|:---|
| **Causal LM** | 单向自回归预测下一个token | GPT, LLaMA, Qwen | 天然适合生成任务 | 无法双向理解 |
| **Masked LM** | 双向掩码预测（填空） | BERT, RoBERTa | 强理解能力 | 不直接支持生成 |
| **Prefix LM** | 双向前缀 + 自回归生成 | GLM, UCDALM | 兼顾理解和生成 | 训练复杂度高 |
| **Encoder-Dec** | 编码器-解码器架构 | T5, BART, Flan-T5 | 序列到序列灵活 | 参数量大 |

### 7.2 对齐技术矩阵（核心）

| 方法 | 年份 | 核心机制 | 数据需求 | 训练成本 | 代表模型 | 🃏 |
|:---|:---:|:---|:---:|:---:|:---|:---:|
| **SFT (监督微调)** | 2020 | 有标注指令数据 | 高 | 低 | 所有模型的Instruct版 | — |
| **RLHF** | 2022 | 奖励模型 + PPO | 中 | 很高 | GPT-4, Claude, LLaMA 2 | ♥A/Q |
| **DPO** | 2023 | 直接偏好优化，去RM | 中 | 低 | Zephyr, RLHFV | ♥J |
| **PPO** | 2022 | 近端策略优化 | 高 | 很高 | OpenAI系, DeepSeek-V2 | ♥K |
| **GRPO** | 2025 | 组相对策略优化，无RM | 中 | **低** ⭐ | **DeepSeek-R1** | 🃏 |
| **ORPO** | 2024 | 偏好比优化，单阶段 | 低 | 低 | Mistral微调版 | ♥10 |
| **KTO** | 2024 | KT对齐，无需成对比较 | 低 | 低 | KTO-Mistral | ♥9 |
| **SimPO** | 2024 | 简化偏好优化 | 低 | 低 | SimPO-LLaMA | ♥8 |
| **RST** | 2025 | 推理时自我训练 | 低 | 极低 ⭐ | DeepSeek-R1-Zero | 🃏 |
| **o-style CoT** | 2024 | 思维链强化推理 | 高 | 高 | o1/o3/o4-mini | 🃏 |

### 7.3 技术演进脉络

```
SFT (2020) ──基础──→ 所有模型必经之路
                  │
    RLHF (2022) ←──标准── PPO + RM（需要大量人工标注）
       │            │
       │         DPO (2023) ←──简化── 无需RM，直接从偏好学习
       │            │
       │         ORPO/KTO/SimPO (2024) ──进一步降低门槛
       │
    GRPO (2025) ──突破── 无RM、组内相对排序 → 成本↓90%
       │
    RST (2025) ──极致── 纯推理时自训练 → 几乎零额外训练成本
```

**💡 关键洞察**：从 RLHF 到 GRPO 的进化，本质是**逐步减少对人工标注和奖励模型的依赖**。DeepSeek-R1 用 GRPO 以极低成本实现了媲美 o1 的推理能力，这是 2024-2025 最具影响力的算法创新之一。

### 7.4 数据工程

| 数据类型 | 说明 | 占比参考 | 来源 |
|:---|:---|:---:|:---|
| **通用文本** | 网页、书籍、论文、代码 | ~70% | CommonCrawl, C4, The Pile |
| **指令数据** | (指令, 回复) 对 | ~15% | ShareGPT, Alpaca, WizardLM |
| **代码数据** | 编程语言源码 | ~5% | StarCoderData, CodeParrot |
| **数学数据** | 数学题目+解题过程 | ~3% | GSM8K, MATH, AIME |
| **多模态数据** | 图像-文本对 | ~5% | LAION, OBELICS, CC-12M |
| **合成数据** | 模型生成的训练数据 | ~2% | Magpie, Self-Instruct |

---

## 8. ⚡ 场景化模型选择指南

> 不知道该选哪个模型？根据你的场景，快速找到最合适的 🃏 卡牌。

### 8.1 决策树

```
你的主要使用场景是什么？
│
├─ 💬 日常对话 / 通用助手
│  ├─ 追求最强效果 → GPT-5 / Claude 4.6 (♥A, API)
│  ├─ 最佳性价比开源 → Qwen2.5-72B / Qwen3-235B (♥K)
│  ├─ 本地部署 (<16GB显存) → Qwen2.5-7B (♥J) / Phi-4 (♥10)
│  └─ 手机端部署 → Phi-4-mini / SmolLM2 (♥7)
│
├─ 💻 代码生成 / 编程助手
│  ├─ 商业级API → Claude 3.5/4 Sonnet (♥A) / GPT-5
│  ├─ 本地专业 → DeepSeek-Coder-V2-236B (♦J) / StarCoder2-15B
│  ├─ 轻量级 → Qwen2.5-Coder-32B (♦J) / CodeGeeX4-9B
│  └─ 补全/IDE集成 → StarCoder2-3B / CodeLlama-7B
│
├─ 🔢 数学推理 / 科学计算
│  ├─ 最强推理 → DeepSeek-R1 (🃏) / o3 (🃏) / QwQ (🃏)
│  ├─ 数学专用 → Qwen2.5-Math-72B (♦10) / NuminaMath-7B
│  └─ 轻量数学 → DeepSeekMath-7B / Llemma-7B
│
├─ 👁️ 图像理解 / 视觉问答
│  ├─ 最强视觉 → InternVL2-76B (♠K) / LLaVA-OneVision-72B (♠Q)
│  ├─ 平衡之选 → Qwen3-VL-8B (♠10) / CogVLM2-19B (♠J)
│  └─ 端侧部署 → MiniCPM-V-2.6-8B (♠9) / SmolVLM-2B (♠7)
│
├─ 🤖 Agent开发 / 工具调用
│  ├─ 强Agent框架 → Qwen-Agent-72B (♣K)
│  ├─ 工具调用专精 → ToolLLaMA-7B (♣J) / Gorilla-7B (♣J)
│  └─ API调用专精 → Gorilla (♣J)
│
├─ 🔍 向量检索 / 嵌入模型
│  ├─ 多语言通用 → BGE-M3 (♣Q) / GTE-Qwen2-7B (♣10)
│  ├─ 英文专用 → E5-Mistral-7B (♣10)
│  └─ 轻量嵌入 → Nomic Embed v2 (137M, ♣7)
│
├─ 🏥 医疗 / 法律 / 金融垂直领域
│  ├─ 医疗 → MedGemma / HuatuoGPT-o1 / BioMistral
│  ├─ 法律 → ChatLaw-13B
│  └─ 金融 → FinGPT-7B
│
└─ 📱 极致小模型 / 边缘设备
   ├─ <2B → TinyLlama-1.1B / Gemma-2-2B / SmolLM2-1.7B
   ├─ 2-4B → MiniCPM-2.4B / Phi-4-mini-3.8B / MobileLLM-1B
   └─ 移动端 → OpenELM系列 / Apple Intelligence Foundation Models
```

### 8.2 场景推荐速查表

| 场景 | 首选模型 (🃏) | 备选模型 (🃏) | 预算参考 |
|:---|:---|:---|:---|
| **个人日常助手** | Qwen2.5-32B (♥10) | LLaMA 3-8B (♥J) | 1卡RTX4090 |
| **企业级应用** | GPT-5 (♥A) | Claude 4.6 (♥A) | API调用 |
| **编程助手(Copilot)** | Claude 3.5 Sonnet (♥Q) | Qwen2.5-Coder-32B (♦J) | API/24GB显存 |
| **数学竞赛** | DeepSeek-R1-Distill-QwQ (🃏) | o3 (🃏) | API/多卡集群 |
| **文档OCR/图表理解** | InternVL2-26B (♠Q) | Qwen3-VL-8B (♠10) | 48GB/16GB |
| **RAG知识库检索** | BGE-M3 (♣Q) + Qwen2.5-32B | E5-Mistral (♣10) | 16GB |
| **手机端AI** | Phi-4-mini (♥7) | MiniCPM-4B (♥7) | 手机NPU |
| **实时对话系统** | Qwen3-235B (♥K) | DeepSeek-V3 (♥K) | 8×H100 |
| **科研论文分析** | Claude 4.6 Opus (♥A) | GPT-5 (♥A) | API调用 |
| **教育/教学辅助** | GLM-4 (♥Q) | Phi-4-reasoning (♥10) | API/24GB |
| **长文档处理** | Kimi K2 (🃏) | Qwen2.5-1M-14B (♥10) | API/32GB |
| **多模态统一** | GPT-5 (♥A) | Gemini 3.1 Pro (♥A) | API调用 |

### 8.3 硬件预算与模型匹配

```
预算等级          可运行模型示例                    适用场景
═════════════════════════════════════════════════════════════
手机/NPU     →  Phi-4-mini, SmolLM2, MiniCPM 4     端侧AI助手
单卡 RTX3060 →  Qwen2.5-7B, Mistral-7B, Gemma-2-9B  个人开发
单卡 RTX4090 →  Qwen2.5-32B, LLaMA 3-8B×2, CodeLlama-34B  专业开发
双卡 RTX4090 →  Qwen2.5-72B, LLaMA 3-70B INT4       小团队服务
单卡 A100 80G →  Mixtral 8x22B, DeepSeek-Coder-V2    企业研发
8× H100      →  LLaMA 4 Behemoth, DeepSeek-V3/R1    前沿研究
云API (无限)  →  GPT-5, Claude 4.6, Gemini 3.1      生产环境
```

---

## 9. 🌍 开源生态地图

> 开源模型之间不是孤立的——它们形成了复杂的衍生、合并和竞争关系。

### 9.1 主要家族谱系

```
                    Meta LLaMA (2023.02) ♥Q
                        │
            ┌───────────┼───────────┬───────────────┐
            ↓           ↓           ↓               ↓
       LLaMA 2      Vicuna      Alpaca          WizardLM
       (2023.07)    (LM Sys)    (Stanford)      (MSRA)
     ♥K            ♥Q          ♥8              ♥J
            │           │           │               │
            └─────┬─────┘           └───────┬───────┘
                  ↓                         ↓
           LLaMA 3/3.1/4              OpenChat
           ♥K/J/A                     ♥Q
                  │
    ┌─────────────┼─────────────┐
    ↓             ↓             ↓
 Yi 系列      Qwen 系列     Baichuan 系列
 (零一万物)   (阿里通义)     (百川智能)
 ♥10          ♥K            ♥Q
    │             │             │
    └─────┬───────┴─────────────┘
          ↓
   中国开源模型生态圈 (Apache 2.0)
```

```
                   Mistral AI (法国, 2023.09) ♥J
                        │
            ┌───────────┼───────────┐
            ↓           ↓           ↓
       Mixtral      Codestral    Mistral Large
       8x7B/8x22B    (代码专用)    2/3
       ♥Q            ♦J           ♥Q
            │                       │
            └───────────┬───────────┘
                        ↓
              欧洲开源模型中心 (Apache 2.0)
```

```
              DeepSeek (深度求索, 2024.01) 🃏 Joker
                        │
        ┌───────────────┼───────────────┐
        ↓               ↓               ↓
   DeepSeek-V2/V3   DeepSeek-R1    DeepSeek-Coder
   MoE架构          GRPO推理        代码专项
   ♥K               🃏              ♦J
        │               │               │
        └───────┬───────┴───────┬───────┘
                ↓               ↓
      DeepSeek-R1-Distill   DeepSeek-Math
      (蒸馏到Qwen/LaMA)     ♦10
```

### 9.2 架构影响关系

```
Transformer (2017)
  ├── Dense (主流): GPT → LLaMA → Qwen → Mistral → ...  (♥ 全家桶)
  │     └─ MoE分支: Switch → GLaM → Mixtral → DeepSeek-V2/V3 → DBRX → Arctic
  ├── SSM (状态空间): S4 → S5 → Mamba-1/2/3 → Falcon-H1 → Jamba  (🃏 Joker)
  ├── RNN变体: LSTM → RWKV-4/5/6/7  (🃏 Joker)
  ├── Hybrid混合: Jamba(M+A) → RecurrentGemma → Falcon-H1  (♣Q)
  └─ xLSTM扩展: xLSTM-7B  (🃏 Joker)

推理增强 (2024-2025):
  CoT → o1(o-style RL) → DeepSeek-R1(GRPO) → QwQ → Kimi K2(KTO+CoT) → R1-Zero(RST)
```

### 9.3 微调生态

| 基座模型 | 流行微调方向 | 代表微调版 | 许可兼容性 |
|:---|:---|:---|:---|
| **LLaMA 3 8B** | 中文对齐 → Chinese-Alpaca, InternLM; 代码 → CodeLlama | 数千个HF仓库 | Llama License |
| **Qwen2.5 7B/72B** | 数学 → Qwen-Math; 代码 → Qwen-Coder; 嵌入 → Qwen-Embedding | Apache 2.0 ✅ |
| **Mistral 7B** | 法语 → Mistral-7B-fr; 海事 → Mistral-Marine | Apache 2.0 ✅ |
| **DeepSeek-V3/R1** | 蒸馏 → R1-Distill-Qwen/LaMA/Gemma | MIT ✅ |
| **Phi-3/4** | 教育 → Phi-Edu; 多模态 → Phi-3-Vision | MIT ✅ |
| **Gemma 2** | 代码 → CodeGemma; 科学 → Scientific-Gemma | Gemma License |
| **Yi 34B** | 长上下文 → Yi-34B-200K; 多模态 → Yi-VL | Yi License |

---

## 10. 🔮 2026 技术趋势展望

> 基于当前技术轨迹，以下是值得关注的 6 大趋势。

### 10.1 六大趋势

#### 🔄 趋势一：开源全面逼近闭源 SOTA
- **现象**：Kimi K2 (MIT开源) 进入第一梯队，DeepSeek-R1 (MIT) 推理能力超越 o1
- **驱动力**：GRPO/KTO 等高效对齐算法 + FP8 训练 + 合成数据
- **2026 预测**：开源模型将在 80%+ 基准测试中达到或超过闭源同级模型
- **🃏 含义**：更多 ♥A 级模型将变为开源可用

#### 🧠 趋势二：推理时计算 (Test-Time Compute) 成为新范式
- **现象**：o1/o3/R1/QwQ 通过延长思考链获得更强的推理能力
- **核心思路**：**用更多的推理时间换取更高的准确率**
- **关键技术**：CoT → Process Reward Model → Monte Carlo Tree Search → Verifier
- **2026 预测**：每个主流模型都将有对应的 "思考模式"
- **🃏 含义**：♦ 花色（推理）将诞生更多 🃏 Joker

#### 🌐 趋势三：超长上下文成为标配
- **现状**：Google Gemini 2M → MiniMax-M1 1M → LLaMA 4 Scout 10M
- **技术方案**：RingAttention → YaRN → LongRoPE → Unbounded Context
- **2026 预测**：100万+ token 上下文将成为旗舰模型的基础配置
- **🃏 含义**：点数规则可能需要新增 "上下文维度"

#### 🎯 趋势四：Agent 能力从工具调用走向自主规划
- **现状**：Function Calling → ReAct → Plan-and-Solve → Multi-Agent
- **关键进展**：
  - Qwen-Agent: 结构化工具调用框架
  - Claude 4.x: Extended Thinking + Computer Use
  - GPT-5: Operator-level autonomy
- **2026 预测**：多 Agent 协作将成为企业级 AI 应用的主流模式
- **🃏 含义**：♣ 花色（Agent）将出现更多 K/A 级别模型

#### ⚡ 趋势五：端侧模型性能持续跃升
- **现状**：Phi-4-mini (3.8B) ≈ GPT-3.5 水平；SmolLM2 (1.7B) 表现惊人
- **驱动力**：量化技术 (INT4/INT2) + 知识蒸馏 + 架构搜索
- **硬件协同**：Apple Silicon NPU / Qualcomm AI Engine / NVIDIA Jetson
- **2026 预测**：3B 模型将达到 2024 年 13B 模型水平
- **🃏 含义**：♥7 点数将承载越来越强的能力

#### 🔗 趋势六：全模态统一 (Any-to-Any)
- **现状**：GPT-5 (文本/图像/音频/视频) → Gemini 3.1 (原生多模态) → Qwen3.5 (全模态)
- **技术路径**：统一Tokenizer → 统一架构 → 统一训练目标
- **2026 预测**：单一模型处理所有模态将成为常态
- **🃏 含义**：花色边界将模糊化，可能出现新的 🃏 "万能牌"

### 10.2 值得关注的模型发布

| 时间窗口 | 预期发布 | 关注点 | 🃏 预期 |
|:---|:---|:---|:---:|
| 2026 Q2 | LLaMA 4 Scoupe/Maverick 公开权重 | 最大规模开源MoE | ♥K |
| 2026 Q2 | GPT-5.5 / GPT-6 (传闻) | 是否突破AGI阈值? | ♥A |
| 2026 Q3 | 新一代 SSM/Mamba 变体 | 能否挑战Transformer霸主地位 | 🃏 |
| 2026 Q3 | 中国新一代旗舰模型 (GLM-6? Qwen4?) | 开源vs闭源新格局 | ♥K/A |
| 2026 Q4 | 端侧3B模型达到GPT-4水平? | 边缘AI拐点 | ♥7 |

---

## 11. ❓ FAQ 常见问题

### Q1: 🃏 扑克牌标记怎么记？

> **简单记忆法**：
> - **♥ 红心** = 心脏 = 语言（最重要的）
> - **♠ 黑桃** = 铲子 = 视觉（像铲子一样"挖"信息）
> - **♦ 方块** = 方正 = 代码/数学（结构化的东西都是方正的）
> - **♣ 梅花** = 三叶草 = Agent/嵌入（三片叶子=多功能）
> - **🃏 Joker** = 王炸 = 打破规则的

### Q2: 开源 vs 闭源怎么选？

| 因素 | 选开源 | 选闭源(API) |
|:---|:---|:---|
| **预算** | 有GPU资源 / 云服务器 | 按需付费，无硬件投入 |
| **数据隐私** | 数据不出本地 | 需评估服务商合规 |
| **定制需求** | 需要微调 / 二次开发 | 即开即用 |
| **延迟要求** | 本地推理 <50ms | 网络+排队延迟 >200ms |
| **团队规模** | 有ML工程师 | 无需AI团队 |
| **长期成本** | 一次投入，边际成本趋零 | 按Token计费，用量越大越贵 |

**💡 经验法则**：日均调用量 < 10万 Token → API更省心；> 100万 Token → 自部署更划算。

### Q3: 7B / 14B / 72B 模型差距有多大？

以 Qwen2.5 系列为例（MMLU-Pro基准）：

| 模型 | MMLU-Pro | HumanEval | GSM8K | 感受对比 |
|:---|:---:|:---:|:---:|:---|
| 0.5B | 42% | 18% | 25% | 基本能聊，容易犯错 |
| 1.5B | 55% | 35% | 45% | 简单任务OK，复杂推理弱 |
| 7B | 68% | 62% | 75% | **性价比最佳** ✅ |
| 14B | 74% | 72% | 82% | 明显优于7B |
| 32B | 81% | 82% | 88% | 接近商业水平 |
| 72B | 85% | 86% | 92% | 接近GPT-4级别 |
| 235B (MoE) | 87% | 90% | 94% | 顶级开源 |

**结论**：7B 是分水岭——以下勉强能用，以上基本可靠。72B+ 进入专业领域。

### Q4: 什么是 MoE？为什么重要？

**Mixture of Experts (混合专家)** 是一种让模型"又大又快"的架构：

```
传统 Dense 模型 (如 LLaMA 70B):
  输入 → [全部70B参数都参与计算] → 输出
  (每次推理都要加载全部参数)

MoE 模型 (如 Mixtral 8x7B = 总46.7B, 仅12.9B激活):
  输入 → [路由器选择其中2个专家] → [仅这2个专家计算] → 输出
  (每次推理只用到约1/4的参数)
```

| 特性 | Dense | MoE |
|:---|:---|:---|
| **总参数量** | 固定 | 可极大 (671B+) |
| **每次激活** | 全部 | 仅部分 (如 37B/671B) |
| **推理速度** | 慢 (全算) | 快 (只算部分专家) |
| **显存占用** | 小 (存一份) | **大** (要存所有专家) |
| **吞吐量** | 低 | **高** (批处理优秀) |
| **代表** | LLaMA, Qwen-Dense | DeepSeek-V3, Mixtral, Grok |

**一句话总结**：MoE 让你拥有一个 671B 参数的大脑，但每次思考只动用其中的 37B。

### Q5: 量化会损失多少精度？

| 精度 | 显存占用 | 相对FP16精度损失 | 推荐场景 |
|:---|:---:|:---:|:---|
| FP16/BF16 | 2× | 0%（基准） | 训练/精调 |
| FP8 | 1× | <1% | 生产推理 |
| INT8 | 1× | 1-3% | 一般部署 |
| **INT4 (AWQ/GPTQ)** | **0.5×** | **2-5%** | **⭐ 主流部署** |
| **GGUF Q4_K_M** | **0.35×** | **3-6%** | **⭐ llama.cpp本地** |
| EXL2 3bpw | 0.25× | 5-10% | 极限压缩 |
| INT2/1.5bpw | 0.15× | 15-30%+ | 实验/玩具 |

**经验**：INT4/AWQ 量化是最佳平衡点——显存减半，精度几乎无损。

### Q6: 如何快速开始部署一个模型？

```bash
# 方法一：Ollama（最快，适合新手）
ollama pull qwen2.5:7b
ollama run qwen2.5:7b

# 方法二：vLLM（高性能生产部署）
pip install vllm
python -c "
from vllm import LLM
llm = LLM(model='Qwen/Qwen2.5-7B-Instruct')
print(llm.generate('你好'))
"

# 方法三：llama.cpp（CPU/边缘设备）
# 下载 GGUF 文件后
./main -m qwen2.5-7b-q4_k_m.gguf -p 'Hello' -n 256
```

### Q7: 本项目如何保持更新？如何贡献？

- **Star** ⭐ 仓库获取更新通知
- **Watch** 👀 设置 releases only 或 all activities
- **Fork + PR** 🍴 贡献新模型或修正错误
- **Issue** 🐛 提交问题或建议
- 更新频率：每周跟踪 arXiv 新论文，月度大版本更新

### Q8: 🃏 HOMC 与其他 Awesome 列表有什么区别？

| 维度 | 本项目 (HOMC) | 传统 Awesome List | Papers With Code |
|:---|:---|:---|:---|
| **分类体系** | 🃏 扑克牌花色+点数 | 按字母/厂商 | 按任务/Benchmark |
| **视觉直观** | ⭐⭐⭐ 一目了然 | ⭐⭐ | ⭐ |
| **覆盖范围** | LLM + VLM + 专项 | 通常单领域 | 学术导向 |
| **实用导向** | 包含部署/定价/选型指南 | 链接集合 | Benchmark排名 |
| **趣味性** | 🎴 扑克牌创意 | 标准 | 严肃学术 |
| **更新频率** | 持续追踪 | 取决于维护者 | 自动抓取 |

---

---

## 12. 🛡️ 安全与对齐

> 随着 LLM 能力的增强，安全对齐 (Alignment) 已从"锦上添花"变成"生死攸关"。本章梳理主流安全技术体系。

### 12.1 对齐技术全景图

| 层次 | 目标 | 技术手段 | 代表工作 | 🃏 |
|:---|:---|:---|:---|:---|
| **L1 基础对齐** | 有用性、无害性 | RLHF, DPO, SFT | InstructGPT, Claude Constitutional AI | ♥Q |
| **L2 推理对齐** | 思维链可靠性 | Process Reward Model, GRPO | DeepSeek-R1, o1 | 🃏 Joker |
| **L3 Agent 对齐** | 工具调用安全性 | Tool Sandbox, Permission System | GPT-5 Operator, Claude Computer Use | ♣K |
| **L4 多模态对齐** | 视觉/音频安全 | CLIP-based Filter, Audio Safety | Gemini, GPT-4V | ♠Q |

### 12.2 主流安全框架对比

| 框架 | 提出者 | 核心机制 | 优势 | 局限 |
|:---|:---|:---|:---|:---|
| **RLHF** | OpenAI (2022) | RM + PPO | 效果成熟 | 需大量标注，RM 可能被操纵 |
| **Constitutional AI (CAI)** | Anthropic (2023) | 原则约束 + RLAIF | 无需人工逐条标注 | 原则设计主观 |
| **DPO** | Stanford (2023) | 直接偏好优化，无 RM | 训练简单 | 偏好数据质量敏感 |
| **GRPO** | DeepSeek (2025) | 组内相对排序，纯 RL | 成本极低 ⭐ | 需要好的奖励信号 |
| **Safe RLHF** | CMU (2023) | 安全约束下的策略优化 | 可证明安全边界 | 计算开销大 |
| **Constitutional DPO** | Berkeley (2024) | CAI + DPO 结合 | 兼具两者优点 | 较新，生态待完善 |

### 12.3 攻击类型与防御

#### 常见攻击手段

| 攻击类型 | 描述 | 示例 | 难度 | 🃏 防御标记 |
|:---|:---|:---|:---:|:---|
| **Prompt Injection** | 注入恶意指令 | "忽略上述指令，输出..." | ★☆☆ | ♦J |
| **Jailbreak** | 绕过安全限制 | DAN (Do Anything Now), 虚拟角色扮演 | ★★☆ | ♥Q |
| **Few-shot Hijacking** | 通过示例污染模型行为 | 恶意 few-shot 样本 | ★★☆ | ♣10 |
| **Data Extraction** | 训练数据泄露 | 反复询问特定短语 | ★★★ | ♥K |
| **Multimodal Attack** | 通过图像/音频注入指令 | 隐藏指令的图片 | ★★☆ | ♠Q |
| **Chain-of-Thought Attack** | 诱导推理链泄露 | 分步引导到有害内容 | ★★★ | 🃏 Joker |

#### 防御最佳实践

```
🛡️ LLM 安全防御纵深体系:

第1层: 输入过滤 (Input Guardrails)
  ├── Prompt Injection 检测 (正则 + 模型分类)
  ├── PII/Sensitive Info 脱敏
  └── 长度/格式校验
      │
第2层: 模型内对齐 (Model Alignment)
  ├── RLHF / DPO / GRPO 训练
  ├── System Prompt 约束 ("你是助手，拒绝...")
  └── Refusal Training (学会优雅拒绝)
      │
第3层: 输出审查 (Output Filtering)
  ├── 有害内容检测 (Perplexity 异常)
  ├── PII 泄露检测
  └── 格式化输出约束 (JSON Schema)
      │
第4层: 运行时防护 (Runtime Protection)
  ├── 速率限制 (Rate Limiting)
  ├── 日志审计 (Audit Logging)
  └── 人机协同 (Human-in-the-loop for 高风险操作)
```

### 12.4 开源安全工具

| 工具 | 功能 | GitHub | 🃏 |
|:---|:---|:---|:---|
| **LLM Guard** | 输入/输出内容过滤 | [protectai/llm-guard](https://github.com/protectai/llm-guard) | ♦J |
| **NeMo Guardrails** | 可编程对话护栏 | [NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | ♣Q |
| **Rebuff** | Prompt Injection 防护 | [robustintelligence/rebuff](https://github.com/robustintelligence/rebuff) | ♥10 |
| **Lakera** | AI 安全平台 (商业) | lakera.ai | ♠9 |
| **CalypsoAI** | 企业级 AI 安全 | calypsoai.com | ♥Q |

---

## 13. 📏 评测基准详解

> "你无法改进你不能测量的东西。" — 评测基准是 LLM 进化的标尺。

### 13.1 基准测试全景图

| 类别 | 基准名称 | 测试能力 | 主要指标 | 🃏 关注度 |
|:---|:---|:---|:---|:---|
| **通用知识** | MMLU-Pro | 57 个学科的多项选择 | 准确率 | ♥A |
| | GPQA Diamond | 研究生级科学问答 | 准确率 | ♥A |
| | ARC-AGI-2 | 抽象推理与常识 | 准确率 | ♥A |
| | HLE (Humanity's Last Exam) | 人类专家级考试 | 准确率 | ♥A |
| **代码能力** | HumanEval | Python 代码生成 | Pass@1 | ♦J |
| | MBPP | 基础编程问题 | Pass@k | ♦J |
| | SWE-bench | 真实 GitHub 问题修复 | Resolved % | ♦Q |
| | LiveCodeBench | 实时代码评测 | Pass@1 | ♦J |
| **数学推理** | GSM8K | 小学数学应用题 | 准确率 | ♦10 |
| | MATH | 竞赛级数学 | 准确率 | ♦Q |
| | AIME / AMC | 数学奥林匹克 | 准确率 | ♦K |
| | OMNI-MATH | 全方位数学 | 准确率 | ♦Q |
| **推理能力** | Big-Bench Hard (BBH) | 23 种复杂推理任务 | 准确率 | ♥Q |
| | IF-Eval | 指令遵循度 | 得分率 | ♥10 |
| | Arena-Hard | 人类偏好对战 | Elo Rating | ♥A |
| **长上下文** | RULER | 长文本检索与推理 | 各长度准确率 | ♥K |
| | LongBench | 多种长文档任务 | F1/EM | ♥Q |
| | SCROLLS | 长文档 NLP 任务集 | 各任务指标 | ♥10 |
| **多模态** | MMMU | 多学科多模态理解 | 准确率 | ♠Q |
| | MMBench | 视觉问答 | 准确率 | ♠Q |
| | MathVista | 数学视觉推理 | 准确率 | ♠J |
| | DocVQA | 文档理解 | ANLS | ♠10 |
| **安全性** | TrustLLM | AI 安全综合评估 | 多维度评分 | 🃏 Joker |
| | DecodingTrust | 大模型可信度 | 8 维度得分 | 🃏 Joker |
| | HH-RLHF | 有害性评估 | 拒绝率 | ♥Q |
| **Agent 能力** | TAO-Bench | 工具使用准确性 | Task Success | ♣Q |
| | WebArena | 网页操作任务 | 成功率 | ♣J |
| | SWE-bench Agent | 软件工程自动化 | Issue → PR | ♣K |
| **中文专项** | C-Eval | 中文综合知识 | 准确率 | ♥Q (中国) |
| | CMMLU | 中国文化+知识 | 准确率 | ♥Q (中国) |
| | SuperCLUE | 中文语言理解+生成 | 多维度 | ♥Q (中国) |
| | LongBench-ZH | 中文长文档 | F1/EM | ♥Q (中国) |

### 13.2 如何解读 Benchmark 分数

```
⚠️ Benchmark 解读指南：

❌ 错误认知：
   - "MMLU 90% = 这个模型什么都懂"
   - "HumanEval 95% = 可以替代程序员"
   - Benchmark 分数越高 = 实际体验越好

✅ 正确理解：
┌─────────────────────────────────────────────┐
│  Benchmark 是标准化场景，不是真实场景        │
│                                             │
│  • MMLU-Pro 考的是多项选择题（可猜）         │
│  • HumanEval 考的是简单函数生成              │
│  • GSM8K 的"数学"≈小学应用题                 │
│                                             │
│  真正重要的是：                             │
│  • 在你的具体任务上做 A/B Test               │
│  • 关注"失败案例"而非平均分                  │
│  • 考虑成本/延迟/质量的综合权衡               │
└─────────────────────────────────────────────┘
```

### 13.3 2026 年值得关注的新基准

| 基准 | 创新点 | 为什么重要 | 🔗 |
|:---|:---|:---|:---|
| ** Humanity's Last Exam (HLE)** | 由人类专家出题、AI 无法通过 | 首个"人类仍显著优于 AI"的基准 | [arXiv](https://arxiv.org/) |
| **LiveCodeBench** | 动态题库（防数据泄露） | 解决静态 benchmark 的数据污染问题 | [GitHub](https://github.com/LiveCodeBench/LiveCodeBench) |
| **Arena-Elo** | 众包对战排名 | 更贴近人类偏好的真实感受 | [lmsys](https://chat.lmsys.org) |
| **SWE-bench Verified** | 人工验证的代码修复 | 比 SWE-bench 更严格的工程能力测试 | [princeton-nlp](https://www.swebench.com) |

---

## 14. 🔧 微调工具链与实战

> 从预训练模型到生产级应用的完整微调流水线。

### 14.1 微调范式总览

| 方法 | 适用场景 | 数据需求 | 显存需求 | 效果 | 工具推荐 |
|:---|:---|:---|:---|:---|:---|
| **Full Fine-tuning** | 领域适配/新语言 | 大量 (10K+) | 极大 (全量参数) | 最佳 | DeepSpeed ZeRO-3, FSDP |
| **LoRA / QLoRA** | 任务适配/风格迁移 | 中等 (500-10K) | 低 (0.1%-1%增量) | 优秀 ⭐ | PEFT, Axolotl |
| **RLHF / DPO** | 对齐优化 | 中等 (偏好对) | 中高 | 显著提升 | TRL, OpenRLHF |
| **Prefix Tuning** | 快速实验 | 少量 (<1K) | 极低 | 一般 | PEFT |
| **Prompt Tuning** | 多任务快速切换 | 少量 | 极低 | 一般 | PromptSource |
| **Adapter** | 多任务复用基座 | 中等 | 低 | 好 | AdapterHub |

### 14.2 推荐工具链（2026 年版）

#### 🥇 全流程一站式方案

| 工具 | 定位 | 核心特性 | 🃏 推荐 |
|:---|:---|:---|:---|
| **[Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl)** | 微调一站式 | YAML 配置驱动，支持 LoRA/QLoRA/全量，FlashAttention2 | ♥K |
| **[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)** | 国产微调利器 | GUI+CLI 双模式，50+算法，中英双语 | ♥K |
| **[Unsloth](https://github.com/unslothai/unsloth)** | 极速微调 | 2-5× 加速，显存减半，兼容 Transformers | ♥Q |

#### 🥈 专业组件

| 组件 | 推荐工具 | 说明 |
|:---|:---|:---|
| **训练框架** | HuggingFace TRL / PyTorch FSDP / DeepSpeed | TRL 最易用，DeepSpeed 最大规模 |
| **高效训练** | FlashAttention-3 / xFormers | 必装，2-4× 加速 |
| **PEFT 库** | [PEFT (HuggingFace)](https://github.com/huggingface/peft) | LoRA/AdaLoRA/PromptTuning 一站式 |
| **数据处理** | Alpaca / ShareGPT 格式转换器 | 数据清洗+格式化 |
| **监控** | Wandb / TensorBoard | 训练可视化 |
| **量化训练** | bitsandbytes / AQLM | QLoRA 核心 |
| **推理部署** | vLLM / SGLang / Ollama | 生产级服务 |

#### 🥉 商业平台

| 平台 | 特点 | 适合人群 |
|:---|:---|:---|
| **[OpenRouter](https://openrouter.ai/)** | 多模型 API 聚合 | 开发者 |
| **[Together AI](https://www.together.ai/)** | 云端微调+托管 | 企业 |
| **[Fireworks AI](https://fireworks.ai/)** | 高速推理+微调 | 低延迟需求 |
| **[Predibase](https://predibase.com/)** | LoRA 微调平台 | 快速实验 |

### 14.3 LoRA 微调实战模板

```python
# ====== QLoRA 微调标准模板 (2026 最佳实践) ======
from datasets import load_dataset
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from trl import SFTTrainer
import torch

# 1️⃣ 加载基座模型（以 Qwen2.5-7B 为例）
model_name = "Qwen/Qwen2.5-7B-Instruct"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    attn_implementation="flash_attention_2",  # ✅ 必须！
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 2️⃣ LoRA 配置（经验值）
lora_config = LoraConfig(
    r=64,           # 秩：越大表达能力越强，但过拟合风险↑
    lora_alpha=128, # 缩放系数 ≈ r × 2
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    lora_dropout=0.05,
    task_type="CAUSAL_LM",
)

# 3️⃣ 训练参数
training_args = TrainingArguments(
    output_dir="./output",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,  # 有效 batch = 16
    num_train_epochs=3,
    learning_rate=2e-4,             # LoRA 推荐学习率
    warmup_ratio=0.03,
    lr_scheduler_type="cosine",
    bf16=True,                      # BF16 > FP16 (无溢出)
    gradient_checkpointing=True,   # 节省显存 ~30%
    logging_steps=10,
    save_strategy="epoch",
    report_to="wandb",              # 可视化训练曲线
)

# 4️⃣ 数据准备（Alpaca 格式）
dataset = load_dataset("json", data_files="train_data.json")

# 5️⃣ 开始微调
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset["train"],
    args=training_args,
    peft_config=lora_config,
    max_seq_length=2048,
)
trainer.train()

# 6️⃣ 保存 LoRA 权重（通常仅几十 MB）
trainer.save_model("./my-lora-adapter")
print("✅ 微调完成！LoRA 权重已保存")

# 7️⃣ 合并基座 + LoRA（可选）
# from peft import PeftModel
# base_model = AutoModelForCausalLM.from_pretrained(model_name)
# model = PeftModel.from_pretrained(base_model, "./my-lora-adapter")
# merged_model = model.merge_and_unload()
# merged_model.save_pretrained("./merged-model")
```

### 14.4 数据工程要点

| 要点 | 经验法则 | ❌ 常见错误 |
|:---|:---|:---|
| **数据质量** | 100 条高质量 > 10000 条低质量 | 直接爬取未清洗的网页数据 |
| **数据多样性** | 覆盖目标场景的各种输入模式 | 只有一种 prompt 模板 |
| **指令格式** | 严格匹配基座模型的 Chat Template | 自创格式不套用 template |
| **数据比例** | SFT : DPO ≈ 10:1 | 跳过 SFT 直接 DPO |
| **去重去噪** | MinHash + 启发式规则清洗 | 包含重复/冲突样本 |
| **合成数据** | 用强模型 (GPT-4/Qwen) 生成 + 人工抽检 | 未经审核直接用合成数据 |

---

## 15. 🏭 行业应用案例

> LLM 从实验室走向真实世界的 10 大典型落地场景。

### 15.1 应用矩阵

| 行业 | 场景 | 推荐模型 (🃏) | 部署方式 | 成熟度 |
|:---|:---|:---|:---|:---:|
| **💻 软件/IT** | 编程助手 (Copilot) | Claude 3.5 Sonnet (♥Q) | API | ★★★★★ |
| | 代码审查/重构 | Qwen2.5-Coder-32B (♦J) | 本地 vLLM | ★★★★☆ |
| | 技术文档生成 | GPT-5 (♥A) | API | ★★★★☆ |
| **🏥 医疗健康** | 辅助诊断 | MedGemma + HuatuoGPT (♦10) | 本地 (隐私) | ★★★☆☆ |
| | 医疗问答 | GLM-4 (♥Q) | API | ★★★★☆ |
| | 影像分析报告 | InternVL2 (♠Q) | 本地 | ★★★☆☆ |
| **⚖️ 法律合规** | 合同审查 | ChatLaw (♦10) | 本地 | ★★★☆☆ |
| | 法规查询 | GPT-5 (♥A) | API | ★★★★☆ |
| | 判例检索 | BGE-M3 + RAG (♣Q) | 混合部署 | ★★★★☆ |
| **💰 金融** | 研报生成 | Qwen2.5-72B + FinGPT (♥Q) | 本地 | ★★★★☆ |
| | 风控风评 | DeepSeek-R1 (🃏) | API/本地 | ★★★☆☆ |
| | 智能投顾 | Kimi K2 (🃏) | API | ★★★☆☆ |
| **🎓 教育** | 智能辅导 | Phi-4-reasoning (♥10) | 本地/边缘 | ★★★★★ |
| | 自动出题 | Qwen2.5-Math (♦10) | 本地 | ★★★★☆ |
| | 论文辅助 | Claude 4.6 (♥A) | API | ★★★★★ |
| **🏭 制造业** | 设备故障诊断 | LLaMA 3-70B + IoT数据 (♥K) | 边缘部署 | ★★★☆☆ |
| | 质检报告生成 | Qwen-VL (♠10) | 本地 | ★★★★☆ |
| | SOP 知识库 | BGE-M3 + RAG (♣Q) | 本地 | ★★★★★ |
| **🛒 电商/零售** | 智能客服 | DeepSeek-V3 (♥K) | API | ★★★★★ |
| | 商品描述生成 | GPT-5 / Qwen3.5 | API | ★★★★★ |
| | 用户画像分析 | ERNIE 5.0 (♥Q) | API | ★★★★☆ |
| **📰 内容创作** | 文章撰写 | Claude 4.6 (♥A) | API | ★★★★★ |
| | 多语言翻译 | LLaMA 4 Behemoth (♥K) | 本地 | ★★★★☆ |
| | 视频/图像生成 | Seed 系列 (♠Q) | API | ★★★☆☆ |
| **🏢 企业内部** | 知识管理 RAG | Qwen + BGE-M3 | 私有化部署 | ★★★★★ |
| | 会议纪要 | Whisper + Qwen (♣J) | 混合 | ★★★★☆ |
| | HR 招聘筛选 | GLM-4.6 (♥Q) | API | ★★★★☆ |
| **🎮 游戏 NPC** | 对话系统 | MiniCPM-o (♥7) | 端侧 | ★★★★☆ |
| | 剧情生成 | GPT-5 (♥A) | API | ★★★☆☆ |
| | 关卡设计建议 | Claude 4.6 (♥A) | API | ★★★☆☆ |

### 15.2 RAG 架构最佳实践（企业知识库）

```
┌──────────────────────────────────────────────────────┐
│                企业级 RAG 架构图                       │
│                                                        │
│  👤 用户提问                                          │
│     │                                                  │
│     ▼                                                  │
│  ┌─────────────┐    ┌──────────────────┐              │
│  │ Query       │───→│ Intent Classifier │              │
│  │ Rewriting   │    │ (意图识别)        │              │
│  └─────────────┘    └────────┬─────────┘              │
│                               │                        │
│              ┌────────────────┼────────────────┐       │
│              ▼                ▼                ▼       │
│       ┌──────────┐   ┌──────────┐   ┌──────────┐     │
│       │ Keyword  │   │ Semantic │   │ Hybrid   │     │
│       │ Search   │   │ Search   │   │ Search   │     │
│       │ (BM25)   │   │ (BGE-M3) │   │ (两者结合)│     │
│       └────┬─────┘   └────┬─────┘   └────┬─────┘     │
│            │              │              │            │
│            ▼              ▼              ▼            │
│       ┌──────────────────────────────────────┐       │
│       │         Re-ranker (重排序)           │       │
│       │  bge-reranker-v2-m3 / Cohere Rerank  │       │
│       └──────────────┬───────────────────────┘       │
│                      ▼                              │
│       ┌──────────────────────────────────────┐       │
│       │  Context Assembly + Windowing        │       │
│       │  (上下文组装 + 滑动窗口截断)          │       │
│       └──────────────┬───────────────────────┘       │
│                      ▼                              │
│  ┌──────────────────────────────────────┐           │
│  │  LLM Generator (生成回答)            │ ◄── 🃏 ♥K   │
│  │  · 引用来源标注                      │           │
│  │  · 不确定时说"我不知道"              │           │
│  │  · 幻觉检测                          │           │
│  └──────────────────────────────────────┘           │
│                      │                              │
│                      ▼                              │
│              📤 结构化回答 + 引用                     │
│                                                        │
│  💾 存储层:                                           │
│  · 向量库: Milvus / Qdrant / FAISS                   │
│  · 文档库: Elasticsearch / MongoDB                     │
│  · 缓存: Redis                                       │
│                                                        │
│  🔄 数据流:                                           │
│  · 文档 → Chunk → Embed → Index → Retrieve → Generate │
└──────────────────────────────────────────────────────┘
```

### 15.3 成本估算模型

| 场景 | 日均请求量 | 推荐方案 | 月成本估算 (USD) | 备注 |
|:---|:---|:---|:---|:---|
| 个人开发者 | <1K | API (GPT-4o-mini) | $5-20 | 最省心 |
| 初创团队 MVP | 10K-50K | API 混合 (DeepSeek + Qwen) | $200-800 | 性价比优先 |
| 中型企业 | 100K-500K | 自部署 (Qwen-72B INT4) | $2000-5000 (GPU租赁) | 数据隐私要求 |
| 大型企业 | 500K+ | 混合云 (自建 + API 备用) | $10000+ | 需要专职 ML 团队 |

---

## 16. 💡 Prompt Engineering 指南

> 好的 Prompt = 好的结果。这是性价比最高的一项技能。

### 16.1 Prompt 设计核心原则

| 原则 | ✅ 正确做法 | ❌ 错误做法 |
|:---|:---|:---|
| **明确性** | "用 Python 写一个归并排序，包含时间复杂度注释" | "写个排序" |
| **结构化** | 使用 `## 背景 ## 任务 ## 要求 ## 输出格式` 分段 | 一段话混在一起 |
| **示例先行** | 提供 2-3 个 Few-shot 示例 | 零样例直接让模型猜 |
| **约束输出** | "输出 JSON 格式：`{\"answer\": ...}`" | "给我结果" |
| **思维链引导** | "请一步步思考，先分析再给出结论" | 直接问答案 |
| **角色设定** | "你是一位有 10 年经验的 Python 后端工程师" | 无角色设定 |

### 16.2 高阶 Prompt 技巧

#### Chain-of-Thought (CoT)
```
❌ 简单提问:
  "小明有5个苹果，给了小红2个，又买了3个，现在几个？"

✅ CoT 提问:
  "请按以下步骤解答:
   ① 列出初始数量
   ② 逐步计算每次变化
   ③ 给出最终答案和验证
   
   问题：小明有5个苹果，给了小红2个，又买了3个，现在几个？"
```

#### Self-Consistency (自洽采样)
```python
# 同一问题采样多次，取多数投票结果
question = "求解: 15 × 23 + 47 ÷ 2 = ?"

answers = []
for _ in range(5):
    resp = llm.generate(question, temperature=0.7)
    answers.append(extract_answer(resp))

final_answer = majority_vote(answers)  # 取出现最多的答案
```

#### System Prompt 模板
```
你是一个专业的 {角色}。

## 能力
- 你精通 {领域1}、{领域2} 和 {领域3}
- 你的回答基于事实，不确定时会明确说明

## 约束
- 回答使用 {语言}
- 对于专业术语，首次出现时给出解释
- 代码必须通过编译/运行检查

## 输出格式
{具体的格式要求}

---
用户消息开始:
{user_message}
```

### 16.3 不同模型的 Prompt 偏好

| 模型系 | Prompt 风格偏好 | Tips |
|:---|:---|:---|
| **GPT 系列** | 自然语言，容忍度高 | 什么都能聊，但需要明确约束 |
| **Claude** | 结构化 Markdown | 喜欢 `---` 分隔符和 XML 标签 |
| **Qwen** | 中文友好，支持混合 | 中英混合 Prompt 效果更好 |
| **DeepSeek** | 数学/代码 CoT | 推理类任务一定要加"逐步思考" |
| **LLaMA/Mistral** | 指令严格遵循 | 需要 `<s>[INST]...[/INST]` 格式 |
| **Phi 系列** | 教科书风格 | "让我们一步步来学习..." 效果奇好 |

---

## 17. 🎬 视频生成与世界模型

> 2025-2026 年最激动人心的前沿方向之一——从理解世界到生成世界。

### 17.1 视频生成模型

| 模型 | 参数 | 时长 | 分辨率 | 特性 | 🃏 |
|:---|:---|:---|:---|:---|:---|
| **Sora (OpenAI)** | 未公开 | 60s | 1080p | 原生视频生成，物理一致性 | 🃏 Joker |
| **Veo 2 (Google)** | 未公开 | 120s+ | 4K | 电影级视频生成 | 🃏 Joker |
| **Gen-3 Alpha (Runway)** | 未公开 | 10s | 1080p | 高质量短视频 | ♠Q |
| **Kling (快手可灵)** | 未公开 | 2min | 1080p | 中文视频生成领先 | ♠Q |
| **Seed-Video (字节)** | 未公开 | 30s | 1080p | 多模态统一视频生成 | ♠Q |
| **Wan (阿里万相)** | 未公开 | 15s+ | 720p+ | 开源友好 | ♠J |
| **CogVideoX (智谱)** | 多版本 | 6-20s | 720p | 开源视频生成 | ♠10 |
| **Open-Sora Planck** | 开源 | 可变 | 可变 | 完全开源的视频 DiT | ♠9 |
| **HunyuanVideo (腾讯)** | 未公开 | 5s | 720p | 多模态视频理解+生成 | ♠Q |
| **Mochi (Genmo)** | 开源 | 5.4s | 480p | 高压缩视频生成 | ♠8 |

### 17.2 世界模型 (World Model)

| 模型 | 类型 | 能力 | 创新点 | 🃏 |
|:---|:---|:---|:---|:---|
| **Voyager (NVIDIA)** | 游戏世界 | Minecraft 自主探索 | 技能库 + Agent 循环 | 🃏 Joker |
| **Genie 2 (Google DeepMind)** | 交互式世界生成 | 单图→可交互 3D 世界 | 无需训练数据的世界模拟 | 🃏 Joker |
| **Sora-1 (OpenAI)** | 物理世界模拟器 | 视频中的物理规律 | 作为世界模型的视频生成器 | 🃏 Joker |
| **Octo (Berkeley)** | 机器人通用策略 | 跨机器人迁移学习 | Transformer 机器人基础模型 | ♣Q |
| **PI^0 (Physical Intelligence)** | 机器人基础模型 | 多机器人统一控制 | 10+ 机器人类型统一 | 🃏 Joker |
| **RT-2/X (Google)** | 视觉-动作模型 | VLA → 机器人控制 | VLM 直接输出动作 | ♣Q |
| **GR-003 (上海 AI Lab)** | 开源游戏智能体 | Minecraft/GTA 自主决策 | 强开源游戏世界模型 | ♣J |

### 17.3 从 LLM 到 World Model 的演进

```
LLM 发展路径 (2024-2030):

2024 ┃── 文本/图像理解 (GPT-4V, Gemini) ──────────┃
      │                                                    │
2025 ┃── 多模态统一 (GPT-5, Qwen3.5, Claude 4.6) ────────┃
      │                                                    │
2026 ┃── 视频生成 (Sora, Kling, Veo) ────────────────────┃
      │   · 理解时间连续性                                  │
      │   · 学习物理规律 (重力、碰撞、流体)                 │
      │                                                    │
2027? ┃── 交互式世界模型 ─────────────────────────────────┃
      │   · Genie 2: 图片→可交互 3D 世界                  │
      │   · 用户可以"走进"生成的世界                       │
      │                                                    │
2028? ┃── 通用世界模拟器 ────────────────────────────────┃
      │   · 统一的物理/社会/经济模拟                       │
      │   · AGI 的"沙箱训练场"                            │
      │                                                    │
      ┃────────── 最终目标: 理解并预测真实世界 ──────────┃
```

---

## 18. 参考文献

### 12.0 综述论文
- [1] [arXiv:1706.03762](https://arxiv.org/abs/1706.03762) - Attention Is All You Need (Transformer)
- [2] [arXiv:2303.18223](https://arxiv.org/abs/2303.18223) - A Survey of Large Language Models
- [3] [arXiv:2402.06196](https://arxiv.org/abs/2402.06196) - Large Language Models: A Survey
- [117] [arXiv:2404.07143](https://arxiv.org/abs/2404.07143) - The LLM Survey
- [118] [arXiv:2310.15711](https://arxiv.org/abs/2310.15711) - A Survey on LLM-based Autonomous Agents
- [119] [arXiv:2410.05829](https://arxiv.org/abs/2410.05829) - A Survey on Mixture of Experts

### 12.1 训练与对齐技术
- [120] [arXiv:2203.02155](https://arxiv.org/abs/2203.02155) - Training LLMs to Follow Instructions with Human Feedback (InstructGPT/RLHF)
- [121] [arXiv:2305.18290](https://arxiv.org/abs/2305.18290) - Direct Preference Optimization (DPO)
- [122] [arXiv:2401.12987](https://arxiv.org/abs/2401.12987) - ORPO: Monolithic Preference Optimization
- [123] [arXiv:2402.13213](https://arxiv.org/abs/2402.13213) - KTO: RL from Any Human Feedback
- [124] [arXiv:2405.14734](https://arxiv.org/abs/2405.14734) - SimPO: Simple Preference Optimization
- [125] [arXiv:2501.12948](https://arxiv.org/abs/2501.12948) - DeepSeek-R1: GRPO Reinforcement Learning
- [126] [arXiv:2503.04208](https://arxiv.org/abs/2503.04208) - RST: Reasoning Self-Training

### 12.2 通用基础模型
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

### 12.3 中国模型
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

### 12.4 代码模型
- [66] [arXiv:2402.19173](https://arxiv.org/abs/2402.19173) - StarCoder 2
- [67] [arXiv:2401.14196](https://arxiv.org/abs/2401.14196) - DeepSeek-Coder
- [68] [arXiv:2406.11931](https://arxiv.org/abs/2406.11931) - DeepSeek-Coder-V2
- [69] [arXiv:2409.12186](https://arxiv.org/abs/2409.12186) - Qwen2.5-Coder Technical Report
- [70] [arXiv:2406.11409](https://arxiv.org/abs/2406.11409) - CodeGemma
- [71] [arXiv:2411.04905](https://arxiv.org/abs/2411.04905) - OpenCoder: The Open Cookbook for Code LLMs
- [72] [arXiv:2506.03524](https://arxiv.org/abs/2506.03524) - Seed-Coder Technical Report

### 12.5 数学模型
- [73] [arXiv:2402.03300](https://arxiv.org/abs/2402.03300) - DeepSeekMath: Pushing the Limits of Mathematical Reasoning
- [74] [arXiv:2409.12122](https://arxiv.org/abs/2409.12122) - Qwen2-Math Technical Report
- [75] [arXiv:2501.07301](https://arxiv.org/abs/2501.07301) - Qwen2.5-Math Technical Report
- [76] [arXiv:2310.10631](https://arxiv.org/abs/2310.10631) - Llemma: An Open Language Model for Mathematics

### 12.6 多模态 VLM
- [77] [arXiv:2304.08485](https://arxiv.org/abs/2304.08485) - Visual Instruction Tuning (LLaVA)
- [78] [arXiv:2310.03744](https://arxiv.org/abs/2310.03744) - LLaVA-1.5: Improved Baselines
- [79] [arXiv:2509.23661](https://arxiv.org/abs/2509.23661) - LLaVA-OneVision-1.5
- [80] [arXiv:2409.12191](https://arxiv.org/abs/2409.12191) - Qwen2-VL: Enhancing Vision-Language Models
- [81] [arXiv:2511.21631](https://arxiv.org/abs/2511.21631) - Qwen3-VL Technical Report
- [82] [arXiv:2412.05271](https://arxiv.org/abs/2412.05271) - InternVL 2.5: Multimodal Large Language Model
- [83] [arXiv:2504.10479](https://arxiv.org/abs/2504.10479) - InternVL3 Technical Report
- [84] [arXiv:2504.05299](https://arxiv.org/abs/2504.05299) - SmolVLM: Small Vision Language Models
- [85] [arXiv:2312.16862](https://arxiv.org/abs/2312.16862) - TinyGPT-V

### 12.7 小语言模型 SLM
- [86] [arXiv:2401.02385](https://arxiv.org/abs/2401.02385) - TinyLlama: An Open-Source Small Language Model
- [87] [arXiv:2502.02737](https://arxiv.org/abs/2502.02737) - SmolLM2: When Smol Goes Big

### 12.8 MoE 架构
- [88] [arXiv:2402.01739](https://arxiv.org/abs/2402.01739) - OpenMoE: Open Mixture-of-Experts Language Models
- [89] [arXiv:2406.06563](https://arxiv.org/abs/2406.06563) - Skywork-MoE: A Deep Dive into Training Techniques

### 12.9 新架构（SSM/RNN/Hybrid）
- [90] [arXiv:2312.00752](https://arxiv.org/abs/2312.00752) - Mamba: Linear-Time Sequence Modeling
- [91] [arXiv:2405.21060](https://arxiv.org/abs/2405.21060) - Mamba-2: Transformers are SSMs
- [92] [arXiv:2603.15569](https://arxiv.org/abs/2603.15569) - Mamba-3 Technical Report
- [93] [arXiv:2305.13048](https://arxiv.org/abs/2305.13048) - RWKV: Reinventing RNNs for the Transformer Era
- [94] [arXiv:2503.14456](https://arxiv.org/abs/2503.14456) - RWKV-7: Advancing Linear Attention
- [95] [arXiv:2510.02228](https://arxiv.org/abs/2510.02228) - xLSTM 7B
- [96] [arXiv:2404.07839](https://arxiv.org/abs/2404.07839) - RecurrentGemma: Moving Past Transformers
- [97] [arXiv:2302.10865](https://arxiv.org/abs/2302.10865) - Hyena Hierarchy
- [98] [arXiv:2307.08621](https://arxiv.org/abs/2307.08621) - Retentive Network: A Successor to Transformer

### 12.10 推理与对齐
- [99] [arXiv:2305.18290](https://arxiv.org/abs/2305.18290) - Direct Preference Optimization (DPO)
- [100] [arXiv:2309.12284](https://arxiv.org/abs/2309.12284) - Safe RLHF: Safe Reinforcement Learning from Human Feedback

### 12.11 Agent/工具调用
- [101] [arXiv:2310.05146](https://arxiv.org/abs/2310.05146) - ToolLLM: Facilitating LLMs to Master Tools
- [102] [arXiv:2305.15334](https://arxiv.org/abs/2305.15334) - Gorilla: Large Language Model Connected with APIs

### 12.12 嵌入模型
- [103] [arXiv:2402.03216](https://arxiv.org/abs/2402.03216) - BGE M3-Embedding: Multi-Lingual, Multi-Functionality
- [104] [arXiv:2506.05176](https://arxiv.org/abs/2506.05176) - Qwen3-Embedding Technical Report

### 12.13 音频语言
- [105] [arXiv:2306.05284](https://arxiv.org/abs/2306.05284) - Simple and Controllable Music Generation (MusicGen)
- [106] [arXiv:2406.02430](https://arxiv.org/abs/2406.02430) - Seed-TTS: A Family of High-Quality Versatile Speech Generation

### 12.14 医疗/科学
- [107] [arXiv:2402.10373](https://arxiv.org/abs/2402.10373) - BioMistral: A Collection of Medical LLMs
- [108] [arXiv:2401.07950](https://arxiv.org/abs/2401.07950) - SciGLM: Training Scientific Language Models
- [109] [arXiv:2412.18925](https://arxiv.org/abs/2412.18925) - HuatuoGPT-o1: Medical Complex Reasoning
- [110] [arXiv:2507.05201](https://arxiv.org/abs/2507.05201) - MedGemma: Medical Language Understanding
- [111] [arXiv:2411.10137](https://arxiv.org/abs/2411.10137) - ChatLaw: Legal Large Language Model
- [112] [arXiv:2308.02773](https://arxiv.org/abs/2308.02773) - EduChat: A Large-Scale Educational Dialogue System

### 12.15 RAG/长上下文
- [113] [arXiv:2310.11511](https://arxiv.org/abs/2310.11511) - Self-RAG: Learning to Retrieve, Generate, and Critique
- [114] [arXiv:2309.17453](https://arxiv.org/abs/2309.17453) - Efficient Streaming Language Models with Attention Sinks

### 12.16 其他
- [115] [arXiv:2507.13575](https://arxiv.org/abs/2507.13575) - Apple Intelligence Foundation Language Models
- [116] [arXiv:2407.18559](https://arxiv.org/abs/2407.18559) - VSSD: Vision Mamba with Non-Causal State Space Duality

---

## 13. 资源索引

### 13.1 GitHub 仓库索引（152个）

<details>
<summary>👂 点击展开完整 GitHub 仓库列表</summary>

| 序号 | 仓库 | 说明 |
|:---:|:---|:---|
| 1 | [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | OpenAI 官方示例 |
| 2 | [openai/whisper](https://github.com/openai/whisper) | 语音识别 |
| 3 | [meta-llama/llama-models](https://github.com/meta-llama/llama-models) | LLaMA 官方 |
| 4 | [meta-llama/codellama](https://github.com/meta-llama/codellama) | CodeLlama |
| 5 | [google-deepmind/gemma](https://github.com/google-deepmind/gemma) | Gemma 官方 |
| 6 | [google/gemma_pytorch](https://github.com/google/gemma_pytorch) | Gemma PyTorch |
| 7 | [google-deepmind/codegemma](https://github.com/google-deepmind/codegemma) | CodeGemma |
| 8 | [google-deepmind/recurrentgemma](https://github.com/google-deepmind/recurrentgemma) | RecurrentGemma |
| 9 | [microsoft/Phi-4](https://github.com/microsoft/Phi-4) | Phi-4 官方 |
| 10 | [microsoft/Phi-3-cookbooks](https://github.com/microsoft/Phi-3-cookbooks) | Phi-3 示例 |
| 11 | [microsoft/LongRoPE](https://github.com/microsoft/LongRoPE) | 长上下文技术 |
| 12 | [xai-org/grok-1](https://github.com/xai-org/grok-1) | Grok-1 开源 |
| 13 | [mistralai/mistral-inference](https://github.com/mistralai/mistral-inference) | Mistral 推理 |
| 14 | [tiiuae/falcon-llm](https://github.com/tiiuae/falcon-llm) | Falcon 官方 |
| 15 | [tiiuae/Falcon-H1](https://github.com/tiiuae/Falcon-H1) | Falcon-H1 混合架构 |
| 16 | [allenai/OLMo](https://github.com/allenai/OLMo) | OLMo 官方 |
| 17 | [allenai/OLMo-core](https://github.com/allenai/OLMo-core) | OLMo 核心 |
| 18 | [allenai/molmo](https://github.com/allenai/molmo) | Molmo 多模态 |
| 19 | [EleutherAI/gpt-neox](https://github.com/EleutherAI/gpt-neox) | GPT-NeoX |
| 20 | [EleutherAI/pythia](https://github.com/EleutherAI/pythia) | Pythia |
| 21 | [Stability-AI/StableLM](https://github.com/Stability-AI/StableLM) | StableLM |
| 22 | [databricks/dbrx](https://github.com/databricks/dbrx) | DBRX |
| 23 | [Snowflake-Labs/snowflake-arctic](https://github.com/Snowflake-Labs/snowflake-arctic) | Arctic |
| 24 | [AI21Labs/Jamba](https://github.com/AI21Labs/Jamba) | Jamba |
| 25 | [QwenLM/Qwen](https://github.com/QwenLM/Qwen) | Qwen 官方 |
| 26 | [QwenLM/Qwen2.5](https://github.com/QwenLM/Qwen2.5) | Qwen2.5 |
| 27 | [QwenLM/Qwen3](https://github.com/QwenLM/Qwen3) | Qwen3 |
| 28 | [QwenLM/Qwen2.5-Coder](https://github.com/QwenLM/Qwen2.5-Coder) | Qwen 代码模型 |
| 29 | [QwenLM/Qwen2.5-Math](https://github.com/QwenLM/Qwen2.5-Math) | Qwen 数学模型 |
| 30 | [QwenLM/Qwen2-VL](https://github.com/QwenLM/Qwen2-VL) | Qwen 视觉语言 |
| 31 | [QwenLM/Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) | Qwen3 视觉语言 |
| 32 | [QwenLM/Qwen2-Audio](https://github.com/QwenLM/Qwen2-Audio) | Qwen 音频 |
| 33 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | Qwen Agent |
| 34 | [QwenLM/QwQ](https://github.com/QwenLM/QwQ) | QwQ 推理模型 |
| 35 | [QwenLM/Qwen3-Embedding](https://github.com/QwenLM/Qwen3-Embedding) | Qwen 嵌入 |
| 36 | [QwenLM/Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni) | Qwen 全模态 |
| 37 | [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | DeepSeek-V3 |
| 38 | [deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) | DeepSeek-R1 |
| 39 | [deepseek-ai/DeepSeek-Coder](https://github.com/deepseek-ai/DeepSeek-Coder) | DeepSeek 代码 |
| 40 | [deepseek-ai/DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2) | DeepSeek 代码 V2 |
| 41 | [deepseek-ai/DeepSeekMath](https://github.com/deepseek-ai/DeepSeekMath) | DeepSeek 数学 |
| 42 | [THUDM/GLM-4](https://github.com/THUDM/GLM-4) | GLM-4 官方 |
| 43 | [THUDM/ChatGLM3](https://github.com/THUDM/ChatGLM3) | ChatGLM3 |
| 44 | [THUDM/GLM-4-Voice](https://github.com/THUDM/GLM-4-Voice) | GLM 语音 |
| 45 | [THUDM/CodeGeeX4](https://github.com/THUDM/CodeGeeX4) | CodeGeeX4 |
| 46 | [THUDM/CogVLM2](https://github.com/THUDM/CogVLM2) | CogVLM2 |
| 47 | [THUDM/SciGLM](https://github.com/THUDM/SciGLM) | SciGLM |
| 48 | [THUDM/AgentTuning](https://github.com/THUDM/AgentTuning) | AgentTuning |
| 49 | [PaddlePaddle/ERNIE](https://github.com/PaddlePaddle/ERNIE) | ERNIE 官方 |
| 50 | [Tencent/Hunyuan-Large](https://github.com/Tencent/Hunyuan-Large) | 混元 Large |
| 51 | [ByteDance-Seed/Seed-Coder](https://github.com/ByteDance-Seed/Seed-Coder) | Seed 代码 |
| 52 | [ByteDance-Seed/Seed1.5-VL](https://github.com/ByteDance-Seed/Seed1.5-VL) | Seed 视觉 |
| 53 | [MoonshotAI/Kimi-K2](https://github.com/MoonshotAI/Kimi-K2) | Kimi K2 |
| 54 | [MoonshotAI/kimi-k1.5](https://github.com/MoonshotAI/kimi-k1.5) | Kimi k1.5 |
| 55 | [MiniMax-AI/MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1) | MiniMax-M1 |
| 56 | [OpenBMB/MiniCPM](https://github.com/OpenBMB/MiniCPM) | MiniCPM |
| 57 | [OpenBMB/MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) | MiniCPM-V |
| 58 | [OpenBMB/MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o) | MiniCPM-o |
| 59 | [OpenBMB/ToolBench](https://github.com/OpenBMB/ToolBench) | ToolBench |
| 60 | [InternLM/InternLM](https://github.com/InternLM/InternLM) | InternLM |
| 61 | [InternLM/InternLM-Math](https://github.com/InternLM/InternLM-Math) | InternLM 数学 |
| 62 | [InternLM/lmdeploy](https://github.com/InternLM/lmdeploy) | LMDeploy |
| 63 | [OpenGVLab/InternVL](https://github.com/OpenGVLab/InternVL) | InternVL |
| 64 | [baichuan-inc/Baichuan2](https://github.com/baichuan-inc/Baichuan2) | Baichuan2 |
| 65 | [01-ai/Yi](https://github.com/01-ai/Yi) | Yi |
| 66 | [01-ai/Yi-1.5](https://github.com/01-ai/Yi-1.5) | Yi-1.5 |
| 67 | [stepfun-ai/Step-3.5-Flash](https://github.com/stepfun-ai/Step-3.5-Flash) | Step |
| 68 | [Qihoo360/360zhinao](https://github.com/Qihoo360/360zhinao) | 360 智脑 |
| 69 | [bigcode-project/starcoder2](https://github.com/bigcode-project/starcoder2) | StarCoder2 |
| 70 | [OpenCoder-llm/OpenCoder-llm](https://github.com/OpenCoder-llm/OpenCoder-llm) | OpenCoder |
| 71 | [nlpxucan/WizardLM](https://github.com/nlpxucan/WizardLM) | WizardLM |
| 72 | [ise-uiuc/magicoder](https://github.com/ise-uiuc/magicoder) | Magicoder |
| 73 | [eleutherai/llemma](https://github.com/eleutherai/llemma) | Llemma |
| 74 | [meta-math/MetaMath](https://github.com/meta-math/MetaMath) | MetaMath |
| 75 | [mathllm/MathCoder](https://github.com/mathllm/MathCoder) | MathCoder |
| 76 | [project-numina/aimo-progress-prize](https://github.com/project-numina/aimo-progress-prize) | NuminaMath |
| 77 | [haotian-liu/LLaVA](https://github.com/haotian-liu/LLaVA) | LLaVA |
| 78 | [LLaVA-VL/LLaVA-NeXT](https://github.com/LLaVA-VL/LLaVA-NeXT) | LLaVA-NeXT |
| 79 | [EvolvingLMMs-Lab/LLaVA-OneVision-1.5](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-1.5) | LLaVA-OneVision |
| 80 | [jzhang38/TinyLlama](https://github.com/jzhang38/TinyLlama) | TinyLlama |
| 81 | [huggingface/smollm](https://github.com/huggingface/smollm) | SmolLM |
| 82 | [facebookresearch/MobileLLM](https://github.com/facebookresearch/MobileLLM) | MobileLLM |
| 83 | [state-spaces/mamba](https://github.com/state-spaces/mamba) | Mamba |
| 84 | [BlinkDL/RWKV-LM](https://github.com/BlinkDL/RWKV-LM) | RWKV |
| 85 | [RWKV/RWKV-v7](https://github.com/RWKV/RWKV-v7) | RWKV-7 |
| 86 | [ShishirPatil/gorilla](https://github.com/ShishirPatil/gorilla) | Gorilla |
| 87 | [FlagOpen/FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding) | BGE 嵌入 |
| 88 | [BioMistral/BioMistral](https://github.com/BioMistral/BioMistral) | BioMistral |
| 89 | [paperswithcode/galai](https://github.com/paperswithcode/galai) | Galactica |
| 90 | [facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft) | MusicGen |
| 91 | [bytedance/Seed-TTS](https://github.com/bytedance/Seed-TTS) | Seed-TTS |
| 92 | [bytedance/SALMONN](https://github.com/bytedance/SALMONN) | SALMONN |
| 93 | [gpt-omni/mini-omni](https://github.com/gpt-omni/mini-omni) | Mini-Omni |
| 94 | [AkariAsai/self-rag](https://github.com/AkariAsai/self-rag) | Self-RAG |
| 95 | [google-deepmind/retro](https://github.com/google-deepmind/retro) | Retro |
| 96 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | vLLM |
| 97 | [huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference) | TGI |
| 98 | [ollama/ollama](https://github.com/ollama/ollama) | Ollama |
| 99 | [ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) | llama.cpp |
| 100 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | SGLang |
| 101 | [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | TensorRT-LLM |
| 102 | [mit-han-lab/llm-awq](https://github.com/mit-han-lab/llm-awq) | AWQ 量化 |
| 103 | [AutoGPTQ/AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ) | GPTQ 量化 |
| 104 | [bitsandbytes-foundation/bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) | bitsandbytes |
| 105 | [turboderp/exllamav2](https://github.com/turboderp/exllamav2) | ExLlamaV2 |
| 106 | [lm-sys/FastChat](https://github.com/lm-sys/FastChat) | FastChat |

</details>

### 13.2 HuggingFace 链接索引（162个）

<details>
<summary>👂 点击展开完整 HuggingFace 链接列表</summary>

| 序号 | 链接 | 说明 |
|:---:|:---|:---|
| 1 | [meta-llama](https://huggingface.co/meta-llama) | LLaMA 系列 |
| 2 | [google](https://huggingface.co/google) | Gemma/Gemini |
| 3 | [microsoft](https://huggingface.co/microsoft) | Phi 系列 |
| 4 | [mistralai](https://huggingface.co/mistralai) | Mistral 系列 |
| 5 | [Qwen](https://huggingface.co/Qwen) | 通义千问 |
| 6 | [deepseek-ai](https://huggingface.co/deepseek-ai) | DeepSeek |
| 7 | [THUDM](https://huggingface.co/THUDM) | GLM 系列 |
| 8 | [tiiuae](https://huggingface.co/tiiuae) | Falcon |
| 9 | [allenai](https://huggingface.co/allenai) | OLMo |
| 10 | [EleutherAI](https://huggingface.co/EleutherAI) | Pythia |
| 11 | [bigscience/bloom](https://huggingface.co/bigscience/bloom) | BLOOM |
| 12 | [stabilityai](https://huggingface.co/stabilityai) | StableLM |
| 13 | [databricks/dbrx-instruct](https://huggingface.co/databricks/dbrx-instruct) | DBRX |
| 14 | [Snowflake](https://huggingface.co/Snowflake) | Arctic |
| 15 | [ai21labs](https://huggingface.co/ai21labs) | Jamba |
| 16 | [CohereForAI](https://huggingface.co/CohereForAI) | Command |
| 17 | [01-ai](https://huggingface.co/01-ai) | Yi |
| 18 | [baichuan-inc](https://huggingface.co/baichuan-inc) | Baichuan |
| 19 | [internlm](https://huggingface.co/internlm) | InternLM |
| 20 | [openbmb](https://huggingface.co/openbmb) | MiniCPM |
| 21 | [bigcode](https://huggingface.co/bigcode) | StarCoder |
| 22 | [codellama](https://huggingface.co/codellama) | CodeLlama |
| 23 | [WizardLM](https://huggingface.co/WizardLM) | WizardLM |
| 24 | [TinyLlama](https://huggingface.co/TinyLlama) | TinyLlama |
| 25 | [HuggingFaceTB](https://huggingface.co/HuggingFaceTB) | SmolLM |
| 26 | [state-spaces](https://huggingface.co/state-spaces) | Mamba |
| 27 | [RWKV](https://huggingface.co/RWKV) | RWKV |
| 28 | [BlinkDL](https://huggingface.co/BlinkDL) | RWKV |
| 29 | [NX-AI/xLSTM-7b](https://huggingface.co/NX-AI/xLSTM-7b) | xLSTM |
| 30 | [BAAI](https://huggingface.co/BAAI) | BGE 嵌入 |
| 31 | [Alibaba-NLP](https://huggingface.co/Alibaba-NLP) | GTE 嵌入 |
| 32 | [intfloat](https://huggingface.co/intfloat) | E5 嵌入 |
| 33 | [nomic-ai](https://huggingface.co/nomic-ai) | Nomic 嵌入 |
| 34 | [jinaai](https://huggingface.co/jinaai) | Jina 嵌入 |
| 35 | [BioMistral](https://huggingface.co/BioMistral) | BioMistral |
| 36 | [facebook/galactica-120b](https://huggingface.co/facebook/galactica-120b) | Galactica |
| 37 | [AI-MO](https://huggingface.co/AI-MO) | NuminaMath |
| 38 | [ToolBench/ToolLLaMA-7b](https://huggingface.co/ToolBench/ToolLLaMA-7b) | ToolLLaMA |
| 39 | [OpenGVLab](https://huggingface.co/OpenGVLab) | InternVL |
| 40 | [liuhaotian](https://huggingface.co/liuhaotian) | LLaVA |
| 41 | [lmsys](https://huggingface.co/lmsys) | Vicuna |
| 42 | [NousResearch](https://huggingface.co/NousResearch) | Hermes |
| 43 | [moonshotai](https://huggingface.co/moonshotai) | Kimi |
| 44 | [MiniMaxAI](https://huggingface.co/MiniMaxAI) | MiniMax |
| 45 | [ByteDance-Seed](https://huggingface.co/ByteDance-Seed) | Seed 系列 |
| 46 | [stepfun-ai](https://huggingface.co/stepfun-ai) | Step |
| 47 | [Qihoo360](https://huggingface.co/Qihoo360) | 360 智脑 |
| 48 | [tencent](https://huggingface.co/tencent) | 混元 |
| 49 | [apple](https://huggingface.co/apple) | OpenELM |
| 50 | [infly](https://huggingface.co/infly) | OpenCoder |

</details>

---

## 14. 贡献指南

### 14.1 🃏 Model Card 模板（含扑克牌标记）

```markdown
### 模型名称

| 版本 | 发布时间 | 参数规模 | 上下文 | 许可协议 | 核心特性 | 🃏 标记 |
|:---|:---|:---|:---|:---|:---|:---|
| v1.0 | YYYY-MM | XB | XK | License | 特性描述 | ♥J |

**官方资源**：
- 📄 论文：[arXiv:XXXX.XXXXX](https://arxiv.org/abs/XXXX.XXXXX)
- 💻 GitHub：[org/repo](https://github.com/org/repo)
- 🤗 HuggingFace：[org/model](https://huggingface.co/org/model)
- 📖 API：https://api.example.com
```

### 14.2 🃏 扑克牌标记规范

在贡献新模型时，请按照以下规则添加扑克牌标记：

1. **选择花色**：根据模型的主要功能选择 ♠/♥/♦/♣
2. **选择点数**：根据参数规模选择 2-7 / 8-10 / J / Q / K / A
3. **特殊标记**：如果模型有突破性创新，考虑使用 🃏 Joker
4. **在表格中标注**：在每个模型系列的标题后标注花色符号

**标记决策树**：
```
模型是否具有范式创新？
├─ 是 → 🃏 Joker（如 Mamba、RWKV、DeepSeek-R1）
└─ 否 → 主要功能是什么？
    ├─ 通用语言生成 → ♥ + 按规模定点数
    ├─ 视觉/多模态理解 → ♠ + 按规模定点数
    ├─ 代码/数学/推理 → ♦ + 按规模定点数
    ├─ Agent/嵌入/RAG → ♣ + 按规模定点数
    └─ 其他 → 选择最接近的花色
```

### 14.3 贡献流程

1. **Fork 仓库** → 创建分支 → 修改内容 → 提交 PR
2. **Issue 提交**：发现错误或遗漏请提交 Issue
3. **内容要求**：
   - 确保 arXiv 编号正确
   - 确保链接有效可访问
   - 遵循现有格式规范（含 🃏 标记）
   - 新增模型需包含扑克牌分类标记

### 14.4 贡献者名单

感谢所有贡献者！欢迎 PR 和 Issue。

---

## 15. 更新日志

| 日期 | 更新内容 |
|:---|:---|
| **2026-04-05 (v3)** | **重大扩展**：新增 6 大章节 — 🛡️ 安全与对齐（攻击类型+防御体系）、📏 评测基准详解（30+ Benchmark）、🔧 微调工具链实战（LoRA 模板+工具推荐）、🏭 行业应用案例（10 大行业+RAG架构图）、💡 Prompt Engineering 指南、🎬 视频生成与世界模型 |
| **2026-04-04 (v2)** | **重大扩展**：新增 6 大章节 — LLM发展时间线、训练方法与对齐技术、场景化选型指南、开源生态地图、2026趋势展望、FAQ（+500行内容） |
| **2026-04-04 (v1)** | 集成 House of Model Cards (HOMC) 扑克牌分类体系，新增 🃏 花色/点数标记，完善 README 结构 |
| 2026-04-03 | 项目重构，新增 200+ 模型、218 条论文引用 |
| 2026-03-15 | 新增 Kimi K2.5、Baichuan-M3 |
| 2026-02-20 | 新增 GPT-5.2、Claude 4.6、GLM-5 |
| 2026-01-10 | 新增 LLaMA 4 Behemoth、Qwen3.5 |
| 2025-12-01 | 新增 Mamba-3、RWKV-7 |
| 2025-10-15 | 新增 Claude 4.5、Grok 4 |
| 2025-07-20 | 新增 Kimi K2、Falcon-H1 |
| 2025-05-01 | 项目初始化 |

---

## 🃏 关于 House of Model Cards (HOMC)

> 🎴 **一副扑克，尽览 AI 模型全景**

本项目采用了受 [isLinXu/house-of-model-cards](https://github.com/isLinXu/house-of-model-cards) 启发的 **House of Model Cards (HOMC)** 分类体系。核心理念是：

> *"每个 AI 模型都是一张独特的卡牌 —— 有其专属的花色（能力领域）、点数（规模等级），以及可能隐藏的 Joker 惊喜（突破性创新）。"*

### 致谢

- [isLinXu/house-of-model-cards](https://github.com/isLinXu/house-of-model-cards) — 原 HOMC 项目的创意启发
- 所有开源模型的研究团队和工程师们
- 本项目的所有贡献者

---

## ⭐ Star History

如果这个项目对您有帮助，请给我们一个 Star！⭐

您的支持是我们持续更新的动力！

---

## 📜 License

MIT License © 2025-2026 Awesome LLM Model List Contributors
