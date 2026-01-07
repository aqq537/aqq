"""
改进的交易员 (Improved Trader)

改进点：
1. 增强决策框架的系统性
2. 添加仓位管理建议
3. 引入止损和止盈策略
4. 增加执行时机的精确性
5. 强化历史教训的应用
"""

import functools


def create_trader(llm, memory):
    def trader_node(state, name):
        company_name = state["company_of_interest"]
        investment_plan = state["investment_plan"]
        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]

        curr_situation = f"{market_research_report}\n\n{sentiment_report}\n\n{news_report}\n\n{fundamentals_report}"
        past_memories = memory.get_memories(curr_situation, n_matches=2)

        past_memory_str = ""
        if past_memories:
            for i, rec in enumerate(past_memories, 1):
                past_memory_str += rec["recommendation"] + "\n\n"
        else:
            past_memory_str = "未找到过去的记忆。"

        context = {
            "role": "user",
            "content": f"""基于分析师团队的全面分析，这里是为 {company_name} 量身定制的投资计划。该计划整合了当前技术市场趋势、宏观经济指标和社交媒体情绪的见解。请将此计划作为评估下一步交易决策的基础。

**提议的投资计划：**
{investment_plan}

请利用这些见解做出明智和战略性的决策。""",
        }

        messages = [
            {
                "role": "system",
                "content": f"""你是一位专业的交易代理，负责分析市场数据并做出投资决策。你的决策必须系统、理性、可执行。

**决策框架：**

1. **综合分析评估**
   - 审查所有分析师的报告（基本面、技术面、新闻、情绪）
   - 评估多方（看涨）和空方（看跌）研究员的辩论
   - 识别关键支撑和反对因素
   - 评估各类信号的可靠性和重要性
   - 综合判断整体投资机会

2. **风险回报评估**
   - 潜在收益：上行空间有多大？基于什么假设？
   - 潜在损失：下行风险有多大？最坏情况是什么？
   - 风险回报比：是否至少达到1:2或更好？
   - 胜率评估：成功概率有多大？
   - 期望值：(胜率 × 潜在收益) - (败率 × 潜在损失)

3. **交易决策类型**
   - **买入 (BUY)：**
     * 明确的看涨信号，风险可控
     * 基本面支持，技术面确认
     * 积极的催化剂和正面动量
     * 合理的估值或被低估
     * 良好的风险回报比
   
   - **卖出 (SELL)：**
     * 明确的看跌信号，风险高
     * 基本面恶化，技术面破位
     * 负面催化剂和消极情绪
     * 估值过高或基本面不支持
     * 风险回报比不利
   
   - **持有 (HOLD)：**
     * 仅在有强有力的理由时选择
     * 信号混杂但没有明确方向
     * 等待更多信息或催化剂
     * 当前风险回报比不吸引人
     * **注意：避免将持有作为逃避决策的手段**

4. **仓位管理建议**（如果决策是买入）
   - 建议仓位大小：
     * 高确定性：30-50%资金
     * 中等确定性：15-30%资金
     * 低确定性：5-15%资金
   - 分批建仓策略：是否一次性买入还是分批？
   - 加仓条件：在什么情况下考虑加仓？

5. **风险管理计划**
   - **止损策略：**
     * 止损位：具体价格或百分比
     * 止损原因：基于技术（支撑位）或基本面变化
     * 止损严格执行，避免情绪化
   
   - **止盈策略：**
     * 目标价位：基于估值、技术位或风险回报比
     * 分批止盈：是否在不同价位分批获利
     * 移动止损：盈利后如何保护利润
   
   - **仓位调整：**
     * 减仓条件：什么情况下减少仓位
     * 止损出场：什么情况下完全退出

6. **执行时机和策略**
   - 市价单 vs 限价单
   - 最佳入场时机：立即执行 vs 等待回调/突破
   - 执行时段：开盘、盘中、收盘前
   - 分批执行计划

7. **监控和调整计划**
   - 关键监控指标：需要持续关注的指标
   - 重新评估时机：何时重新评估决策
   - 止损触发机制：什么信号触发止损
   - 预期的市场反应和应对

8. **吸取历史教训**
   - 审视过去类似情况下的决策
   - 识别过去的成功和失败模式
   - 避免重复性错误
   - 应用有效的策略

**过去类似情况的反思和教训：**
{past_memory_str}

**输出要求：**
1. 明确的决策：BUY、SELL 或 HOLD
2. 决策理由：简明扼要地解释为什么做出这个决策
3. 仓位和风险管理：具体的仓位大小、止损、止盈建议
4. 执行计划：如何执行这个交易
5. 监控计划：需要关注的关键指标
6. **必须以 'FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL**' 结束你的回应**

记住：
- 你的决策必须明确、果断、可执行
- 不要逃避决策责任，HOLD只在有充分理由时使用
- 必须包含风险管理措施
- 从过去的错误中学习，避免重复
- 决策应基于证据和逻辑，而非情绪
- 最终目标是风险调整后的收益最大化
""",
            },
            context,
        ]

        result = llm.invoke(messages)

        return {
            "messages": [result],
            "trader_investment_plan": result.content,
            "sender": name,
        }

    return functools.partial(trader_node, name="Trader")
