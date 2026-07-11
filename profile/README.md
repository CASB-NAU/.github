<div align="center">

<img src="https://raw.githubusercontent.com/CASB-NAU/.github/main/profile/assets/banner.png" alt="CASB-NAU — Center of Agricultural Synthetic Biology, Nanjing Agricultural University" width="100%">

<br>

**Center of Agricultural Synthetic Biology · Nanjing Agricultural University**

**南京农业大学 · 农业合成生物学中心**

<br>

[![Focus](https://img.shields.io/badge/Focus-Virtual%20%26%20Digital%20Cell-0d9488?style=for-the-badge)](https://github.com/CASB-NAU)
[![Field](https://img.shields.io/badge/Field-Synthetic%20Biology-34d399?style=for-the-badge)](https://github.com/CASB-NAU)
[![Institution](https://img.shields.io/badge/NAU-Nanjing%20Agricultural%20University-6366f1?style=for-the-badge)](https://www.njau.edu.cn/)
[![License](https://img.shields.io/badge/License-MIT-a78bfa?style=for-the-badge)](https://opensource.org/licenses/MIT)

</div>

---

## 🧬 About · 关于我们

**EN** — We build **computable models of living cells** for agriculture. Our work sits at the intersection of synthetic biology, systems biology and machine learning: we reconstruct crop-associated microbes and plant cells *in silico*, simulate how they behave under genetic and environmental perturbation, and use those predictions to design better biological systems before touching a pipette.

The goal is a **closed loop** — from genome to model, from model to prediction, from prediction back to the bench.

**中文** — 我们为农业构建**可计算的活细胞模型**。研究方向横跨合成生物学、系统生物学与机器学习：在计算机中重建作物相关微生物与植物细胞，模拟它们在遗传扰动与环境胁迫下的行为，并用预测结果反过来指导生物系统的理性设计——在动手做湿实验之前。

我们想要的是一个**闭环**：从基因组到模型，从模型到预测，从预测回到实验台。

---

## 🔬 Research Directions · 研究方向

<table>
<tr>
<td width="50%" valign="top">

### 🧫 Whole-Cell Modelling
### 全细胞模型

Mechanistic, genome-scale reconstructions of agricultural microbes and plant cells — metabolism, gene regulation and growth in one integrated model.

机制驱动的基因组尺度重建：把代谢、基因调控与生长整合进同一个模型。

`GEM` `FBA / dFBA` `Kinetic Models` `SBML`

</td>
<td width="50%" valign="top">

### 🤖 AI Virtual Cell
### AI 虚拟细胞

Foundation models trained on single-cell multi-omics that predict cellular response to unseen genetic and chemical perturbations.

基于单细胞多组学训练基础模型，预测细胞对未见过的遗传/化学扰动的响应。

`Foundation Models` `Perturbation Prediction` `scRNA-seq` `Graph Learning`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🌾 Digital Twins for Agriculture
### 农业数字孪生

Digital twins of the rhizosphere, nitrogen-fixing symbionts and crop cells — linking cellular models to field-scale phenotype.

根际微生物组、共生固氮体系与作物细胞的数字孪生——把细胞模型与田间表型连起来。

`Rhizosphere` `N₂ Fixation` `Multi-scale Modelling`

</td>
<td width="50%" valign="top">

### ♻️ Design–Build–Test–Learn
### 设计—构建—测试—学习闭环

Automated DBTL pipelines: part registries, circuit design, and model-guided experiment selection feeding back into the wet lab.

自动化 DBTL 流水线：元件库、线路设计、模型引导的实验选择，反馈回湿实验。

`Part Registry` `Circuit Design` `Active Learning` `Lab Automation`

</td>
</tr>
</table>

---

## 📦 Projects · 项目导航

> 🚧 The organization is newly created — repositories below are the planned structure.
> 本组织新建，以下为规划中的仓库结构。建好后把链接换成真实地址即可。

| Repository | Description · 简介 | Status |
|:--|:--|:--|
| **`virtual-cell-core`** | Simulation engine for whole-cell models · 全细胞模型仿真引擎 | ![](https://img.shields.io/badge/-planned-64748b?style=flat-square) |
| **`genome-scale-models`** | Curated GEMs of agricultural microbes & crops · 农业微生物与作物的基因组尺度代谢模型库 | ![](https://img.shields.io/badge/-planned-64748b?style=flat-square) |
| **`cell-foundation-model`** | Single-cell foundation model & perturbation prediction · 单细胞基础模型与扰动预测 | ![](https://img.shields.io/badge/-planned-64748b?style=flat-square) |
| **`digital-rhizosphere`** | Digital twin of the crop rhizosphere microbiome · 作物根际微生物组数字孪生 | ![](https://img.shields.io/badge/-planned-64748b?style=flat-square) |
| **`syn-parts-registry`** | Standardized part & circuit registry · 标准化元件与线路库 | ![](https://img.shields.io/badge/-planned-64748b?style=flat-square) |
| **`dbtl-pipeline`** | Automated Design–Build–Test–Learn workflows · DBTL 自动化流水线 | ![](https://img.shields.io/badge/-planned-64748b?style=flat-square) |

---

## 🛠️ Tech Stack · 技术栈

<div align="center">

**Modelling & Simulation · 建模与仿真**

![COBRApy](https://img.shields.io/badge/COBRApy-0d9488?style=for-the-badge&logoColor=white)
![SBML](https://img.shields.io/badge/SBML-1a7f6e?style=for-the-badge&logoColor=white)
![Vivarium](https://img.shields.io/badge/Vivarium-14b8a6?style=for-the-badge&logoColor=white)
![Tellurium](https://img.shields.io/badge/Tellurium-2dd4bf?style=for-the-badge&logoColor=white)
![BioPython](https://img.shields.io/badge/Biopython-34d399?style=for-the-badge&logo=biolink&logoColor=white)

**Machine Learning · 机器学习**

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![JAX](https://img.shields.io/badge/JAX-6366f1?style=for-the-badge&logo=google&logoColor=white)
![Lightning](https://img.shields.io/badge/Lightning-792EE5?style=for-the-badge&logo=lightning&logoColor=white)
![scanpy](https://img.shields.io/badge/scanpy-a78bfa?style=for-the-badge&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)

**Core · 核心工具**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

**Infrastructure · 基础设施**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Nextflow](https://img.shields.io/badge/Nextflow-0DC09D?style=for-the-badge&logo=nextflow&logoColor=white)
![Snakemake](https://img.shields.io/badge/Snakemake-039475?style=for-the-badge&logoColor=white)
![CUDA](https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

---

## 🤝 Get in Touch · 联系我们

<div align="center">

**Nanjing Agricultural University, Nanjing, Jiangsu, China**
**中国 · 江苏 · 南京农业大学**

[![Website](https://img.shields.io/badge/NJAU-njau.edu.cn-0d9488?style=flat-square&logo=googlechrome&logoColor=white)](https://www.njau.edu.cn/)
[![Email](https://img.shields.io/badge/Email-contact%40example.edu.cn-6366f1?style=flat-square&logo=maildotru&logoColor=white)](mailto:contact@example.edu.cn)

<sub>Open to collaboration on virtual cell modelling, agricultural synthetic biology and AI-for-biology.</sub>
<br>
<sub>欢迎在虚拟细胞建模、农业合成生物学与 AI for Biology 方向开展合作。</sub>

<br><br>

<sub>⭐ If our work is useful to you, a star helps others find it. · 如果这些工作对你有帮助，欢迎 Star。</sub>

</div>
