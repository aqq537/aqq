# TradingAgents 改进版 - 多智能体金融交易框架

## 项目简介

本项目基于 [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) 进行改进，对各个专家智能体的提示词进行了系统性优化，以提升交易决策的准确性、深度和可执行性。

TradingAgents 是一个多智能体交易框架，模仿真实交易公司的动态运作。通过部署专业化的 LLM 驱动的智能体：从基本面分析师、情绪专家、技术分析师，到交易员、风险管理团队，该平台协同评估市场状况并指导交易决策。

## 核心改进

### 改进原则

1. **结构化思维** - 所有提示词都采用更结构化的分析框架
2. **数据驱动** - 强调基于数据和证据的分析，减少主观臆断
3. **风险意识** - 全面增强风险识别和管理能力
4. **可执行性** - 提供更具体、可操作的建议和决策
5. **学习机制** - 强化从历史决策中学习和改进的能力
6. **协作性** - 优化各智能体之间的协作和辩论质量

### 改进内容

详细的改进方向、预期效果和技术实现请参考 [IMPROVEMENTS.md](./IMPROVEMENTS.md)

## 智能体架构

### 1. 分析师团队 (Analyst Team)

#### 基本面分析师 (Fundamentals Analyst)
- **文件位置**: `tradingagents/agents/analysts/fundamentals_analyst.py`
- **核心功能**: 评估公司财务和业绩指标，识别内在价值和潜在风险
- **改进重点**:
  - 增强财务指标深度分析
  - 添加行业对比和竞争力评估
  - 引入价值评估模型（PE、PB、DCF等）
  - 强化风险因素识别

#### 新闻分析师 (News Analyst)
- **文件位置**: `tradingagents/agents/analysts/news_analyst.py`
- **核心功能**: 监控全球新闻和宏观经济指标，解读事件对市场的影响
- **改进重点**:
  - 增强新闻事件影响评估框架
  - 添加新闻真实性和可信度评估
  - 引入时效性分析（短期vs长期影响）
  - 增加地缘政治和宏观经济关联分析

#### 技术/市场分析师 (Market/Technical Analyst)
- **文件位置**: `tradingagents/agents/analysts/market_analyst.py`
- **核心功能**: 利用技术指标（如 MACD 和 RSI）检测交易模式和预测价格走势
- **改进重点**:
  - 优化技术指标选择策略
  - 增加多时间框架分析
  - 引入价格形态识别
  - 添加支撑位和阻力位分析

#### 社交媒体/情绪分析师 (Social Media/Sentiment Analyst)
- **文件位置**: `tradingagents/agents/analysts/social_media_analyst.py`
- **核心功能**: 分析社交媒体和公众情绪，评估短期市场情绪
- **改进重点**:
  - 增强情绪量化分析能力
  - 添加异常情绪波动检测
  - 引入情绪领先指标识别
  - 强化谣言和虚假信息过滤

### 2. 研究员团队 (Researcher Team)

#### 看涨研究员 (Bull Researcher)
- **文件位置**: `tradingagents/agents/researchers/bull_researcher.py`
- **核心功能**: 批判性评估分析师团队提供的见解，通过结构化辩论平衡潜在收益与固有风险
- **改进重点**:
  - 增强论证逻辑的严密性
  - 添加数据驱动的支撑论据
  - 引入风险对冲思维
  - 增加对熊市论点的系统性反驳

#### 看跌研究员 (Bear Researcher)
- **文件位置**: `tradingagents/agents/researchers/bear_researcher.py`
- **核心功能**: 从看跌角度批判性评估，识别风险和挑战
- **改进重点**:
  - 增强风险识别的全面性
  - 添加极端情况分析
  - 引入下行风险量化
  - 增加对牛市论点的系统性质疑

### 3. 交易员 (Trader Agent)

- **文件位置**: `tradingagents/agents/trader/trader.py`
- **核心功能**: 综合分析师和研究员的报告，做出明智的交易决策
- **改进重点**:
  - 增强决策框架的系统性
  - 添加仓位管理建议
  - 引入止损和止盈策略
  - 增加执行时机的精确性

### 4. 风险管理团队 (Risk Management Team)

#### 激进风险分析师 (Aggressive/Risky Debator)
- **文件位置**: `tradingagents/agents/risk_mgmt/aggresive_debator.py`
- **核心功能**: 倡导高回报、高风险策略
- **改进重点**:
  - 增强机会成本分析
  - 添加高收益场景的概率评估
  - 引入竞争优势分析

#### 保守风险分析师 (Conservative/Safe Debator)
- **文件位置**: `tradingagents/agents/risk_mgmt/conservative_debator.py`
- **核心功能**: 优先考虑资本保全和风险最小化
- **改进重点**:
  - 增强下行风险评估
  - 添加压力测试场景
  - 引入流动性风险分析

#### 中性风险分析师 (Neutral Debator)
- **文件位置**: `tradingagents/agents/risk_mgmt/neutral_debator.py`
- **核心功能**: 提供平衡的风险视角
- **改进重点**:
  - 增强平衡视角
  - 添加多因素综合评估
  - 引入情景分析

#### 风险管理判官 (Risk Manager)
- **文件位置**: `tradingagents/agents/managers/risk_manager.py`
- **核心功能**: 评估风险辩论并做出最终交易决策
- **改进重点**:
  - 增强决策综合能力
  - 添加风险评分系统
  - 引入投资组合优化视角

### 5. 研究经理 (Research Manager)

- **文件位置**: `tradingagents/agents/managers/research_manager.py`
- **核心功能**: 评估看涨/看跌研究员的辩论并制定投资计划
- **改进重点**:
  - 增强综合判断能力
  - 添加论据质量评估
  - 增加投资计划的可操作性

## 项目结构

```
aqq/
├── README.md                          # 本文件
├── IMPROVEMENTS.md                    # 详细改进说明文档
└── tradingagents/
    └── agents/
        ├── analysts/                  # 分析师团队
        │   ├── fundamentals_analyst.py
        │   ├── news_analyst.py
        │   ├── market_analyst.py
        │   └── social_media_analyst.py
        ├── researchers/               # 研究员团队
        │   ├── bull_researcher.py
        │   └── bear_researcher.py
        ├── trader/                    # 交易员
        │   └── trader.py
        ├── risk_mgmt/                 # 风险管理团队
        │   ├── aggresive_debator.py
        │   ├── conservative_debator.py
        │   └── neutral_debator.py
        └── managers/                  # 管理团队
            ├── risk_manager.py
            └── research_manager.py
```

## 使用方法

### 前提条件

本项目提供改进后的智能体提示词和架构设计。要运行完整系统，需要：

1. Python 3.13+
2. LangChain 框架
3. OpenAI API 密钥
4. Alpha Vantage API 密钥（用于金融数据）

### 集成说明

这些改进的智能体可以直接集成到原始 TradingAgents 框架中，替换对应的智能体文件。

每个智能体都遵循相同的接口模式：
- 接受 `state` 参数（包含市场数据、历史记录等）
- 返回更新后的状态和报告/决策

### 示例使用

```python
from tradingagents.agents.analysts.fundamentals_analyst import create_fundamentals_analyst
from langchain_openai import ChatOpenAI

# 初始化 LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# 创建基本面分析师
fundamentals_analyst = create_fundamentals_analyst(llm)

# 使用分析师
state = {
    "trade_date": "2024-05-10",
    "company_of_interest": "NVDA",
    "messages": []
}

result = fundamentals_analyst(state)
print(result["fundamentals_report"])
```

## 核心改进对比

| 智能体 | 原版特点 | 改进版特点 |
|--------|----------|------------|
| 基本面分析师 | 基础财务分析 | 增加估值模型、竞争力评估、风险识别 |
| 新闻分析师 | 新闻汇总 | 增加可信度评估、时效性分析、影响评估框架 |
| 技术分析师 | 基础技术指标 | 增加形态识别、多时间框架、支撑阻力分析 |
| 情绪分析师 | 情绪汇总 | 增加情绪量化、异常检测、领先指标识别 |
| 看涨研究员 | 论点列举 | 增加数据驱动论证、系统性反驳、风险对冲 |
| 看跌研究员 | 风险列举 | 增加极端情况分析、下行风险量化 |
| 交易员 | 基础决策 | 增加仓位管理、止损止盈、执行计划 |
| 风险分析师 | 简单辩论 | 增加概率评估、情景分析、期望值计算 |
| 判官/经理 | 基础综合 | 增加评分系统、决策树、置信度评估 |

## 预期效果

通过这些系统性改进，预期达到以下效果：

1. **决策准确性提升 15-25%** - 通过更深入的分析和更全面的视角
2. **风险控制改善 20-30%** - 通过增强的风险管理机制
3. **收益优化 10-20%** - 通过更好地把握机会和控制风险
4. **系统稳定性提高** - 通过结构化的决策流程
5. **持续改进能力** - 通过学习机制不断优化

## 技术实现

- **框架**: LangChain + LangGraph
- **模型**: 支持 OpenAI GPT-4o、o1-preview 等
- **数据源**: Alpha Vantage、yfinance
- **记忆系统**: 向量数据库进行历史决策存储和检索

## 注意事项

⚠️ **重要声明**: 

本框架仅用于研究目的。交易表现可能因多种因素而异，包括：
- 选择的骨干语言模型
- 模型温度设置
- 交易周期
- 数据质量
- 其他非确定性因素

**本项目不构成财务、投资或交易建议。**

## 贡献

欢迎提交问题报告和改进建议！

## 许可证

本项目基于 TauricResearch/TradingAgents 项目进行改进，遵循原项目的开源许可证。

## 致谢

- 感谢 [TauricResearch](https://github.com/TauricResearch) 开发的原始 TradingAgents 框架
- 感谢 Alpha Vantage 提供的金融数据 API 支持
- 感谢 OpenAI 提供的先进语言模型

## 联系方式

如有问题或建议，欢迎通过 GitHub Issues 联系。

---

**最后更新**: 2026年1月

**版本**: 1.0 - 改进版
