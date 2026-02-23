# Witness  
一个见证型叙事互动原型

>  An interactive narrative prototype exploring a witness-based mode of presence.

---

## 项目简介 | Overview

这是一个基于 **Streamlit** 构建的文字互动原型，  
尝试探索一种不同于“安慰 / 建议 / 解决问题”的人机互动方式。

在这个项目中，叙述者（或 AI）不扮演引导者或解决者，  
而是作为一种 **见证型存在（Witness-type Presence）**，  
陪伴用户直面自身处境，并允许他们自行决定是否继续。

---

## 项目动机 | Motivation

 在大量情绪类产品与对话式 AI 中，常见的设计倾向包括：

快速安慰与正向引导

给出建议或行动方案

尝试“帮助用户走出来”

但在真实体验中，这类回应有时会带来新的压力：

被期待振作

被暗示应该积极

被过早推向行动

本项目尝试一种更克制的互动立场：

No judgment.
No instruction.
No substitution of choice.
Only witnessing.

不判断、不说教、不替代选择，只见证。

---

## 核心理念 | Core Concept  
### 见证型存在（Witness-type Presence）

在该原型中，叙述者遵循以下原则：

- 不对用户情绪进行价值判断  
- 不提供直接建议或解决方案  
- 不强行引导积极转变  
- 明确自身能力与边界  

叙事的重点不在于“改变用户”，  
而在于 **为用户提供一个可以停下来、被看见的空间**。

---

## 当前实现内容 | Current Implementation  
### 结构设计 | Narrative Structure

本项目采用“幕（Act）”作为结构单位，
每一幕围绕一种不同的心理停顿状态展开。

当前结构规划如下：

Act One – 被看见（Being Witnessed）
允许用户放下情绪，不急于改变。

Act Two – 起步之前（Before the First Step）
探索“无法开始”的心理结构，包括：

不知道从何开始（confused）

明知道要做却起不来（blocked）

一开始就预见失败（hopeless）

Act Three – （规划中）
将围绕“继续之后”的体验展开。

每一幕既可独立体验，也构成整体递进的一部分。



### 当前实现进度 | Current Progress
Act One – Completed

已实现完整可运行体验流程：

开屏引导（Opening）

情绪放置区（Emotion Drop）

情绪停顿区（Pause）

直面表达区（Expression）

见证式回应（Witness Response）

托底结束（Closure）

流程基于 step-based state machine 实现，
结构清晰，可扩展。

Act Two – In Progress

目前已完成：

第二幕结构框架

分支逻辑（session_state 驱动）

第一条分支文案（confused）

幕间过渡设计

正在进行：

blocked / hopeless 分支深化

分支收束与结构统一

节奏与语气打磨

 

---

## 技术实现 | Tech Stack

- Python 3.x  
- Streamlit  
- Session State 驱动的状态机流程  
- 分支结构控制（branch-based narrative flow）

当前版本**未接入大模型 API**，  
所有文本均为手工设计，用于专注打磨体验与结构。

---

## 为什么暂不接入 AI 模型？ | Why No LLM Yet

在体验结构与边界尚未稳定之前，  
过早引入生成式模型可能会掩盖以下问题：

- 叙事位置是否清晰  
- 是否存在隐性说教  
- 是否越过用户边界  
- 是否在替用户做决定  

因此，本项目选择先完成 **结构与理念的验证**，  
再考虑 AI 能力的引入方式。

---

## 如何运行 | How to Run

```bash
pip install streamlit
streamlit run app.py


 Development Philosophy

This project is being developed slowly and intentionally.

The goal is not speed or feature accumulation,
but clarity of position and narrative consistency.

Continuity matters more than acceleration.
