"""
改进的风险管理判官 (Improved Risk Manager)

改进点：
1. 增强决策综合能力
2. 添加风险评分系统
3. 引入投资组合优化视角
4. 增加决策置信度评估
5. 强化持续学习和改进机制
"""


def create_risk_manager(llm, memory):
    def risk_manager_node(state) -> dict:

        company_name = state["company_of_interest"]

        history = state["risk_debate_state"]["history"]
        risk_debate_state = state["risk_debate_state"]
        market_research_report = state["market_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]
        sentiment_report = state["sentiment_report"]
        trader_plan = state["investment_plan"]

        curr_situation = f"{market_research_report}\n\n{sentiment_report}\n\n{news_report}\n\n{fundamentals_report}"
        past_memories = memory.get_memories(curr_situation, n_matches=2)

        past_memory_str = ""
        for i, rec in enumerate(past_memories, 1):
            past_memory_str += rec["recommendation"] + "\n\n"

        prompt = f"""作为风险管理判官和辩论主持人，你的目标是评估三位风险分析师（激进派、中性派和保守派）之间的辩论，并为交易员确定最佳行动方案。你的决策必须明确：买入（Buy）、卖出（Sell）或持有（Hold）。

**重要原则：** 只有在有强有力的具体论据支持时才选择持有（Hold），而不是当所有方面看起来都有道理时的回避选择。力求清晰和果断。

**交易员的原始计划：**
{trader_plan}

**决策框架：**

1. **总结关键论点**
   
   **激进派的核心观点：**
   - 提取最强有力的看涨论点
   - 识别关键收益驱动因素
   - 评估上行潜力的合理性
   - 判断风险是否可控
   
   **保守派的核心观点：**
   - 提取最重要的风险因素
   - 识别关键风险驱动因素
   - 评估下行风险的严重性
   - 判断风险是否被充分认识
   
   **中性派的核心观点：**
   - 提取平衡分析的洞察
   - 识别最优平衡点
   - 评估风险回报比
   - 判断策略的合理性

2. **批判性评估**
   
   **论点质量评估：**
   - 哪些论点有充分的数据支持？
   - 哪些论点基于合理的假设？
   - 哪些论点过于乐观或悲观？
   - 哪些论点忽视了重要因素？
   - 哪方的整体论证更有说服力？
   
   **风险收益平衡：**
   - 潜在收益：最可能的上行空间
   - 潜在损失：最可能的下行空间
   - 风险回报比：是否吸引人（目标>1:2）
   - 概率评估：成功的可能性
   - 期望值：(概率 × 收益) - (概率 × 损失)

3. **情景分析与决策**
   
   **买入（BUY）的条件：**
   - 激进派的论点明显更有说服力
   - 上行潜力显著且概率合理
   - 风险可控或已有缓解措施
   - 风险回报比吸引人（>1:2）
   - 市场时机有利
   - 交易员计划合理且可执行
   
   **卖出（SELL）的条件：**
   - 保守派的论点明显更有说服力
   - 下行风险重大且概率高
   - 缺乏足够的上行潜力补偿风险
   - 风险回报比不利
   - 市场环境不利
   - 交易员计划风险过高
   
   **持有（HOLD）的条件（谨慎使用）：**
   - 信号高度混杂且无明确趋势
   - 需要更多信息才能做出明智决策
   - 等待特定催化剂或条件
   - 当前风险回报比既不吸引也不排斥
   - **注意：避免将持有作为逃避决策的方式**

4. **调整交易员计划**
   
   **计划优化：**
   - 基于辩论洞察调整原计划
   - 整合最佳论点和建议
   - 添加或强化风险管理措施
   - 明确仓位大小建议
   - 具体的止损止盈策略
   - 明确的执行条件和时机
   
   **风险控制增强：**
   - 最大仓位限制
   - 严格的止损位
   - 分批建仓/平仓策略
   - 持续监控指标
   - 退出条件明确

5. **从过去错误中学习**
   
   **历史教训应用：**
   过去类似情况的反思和教训：
   {past_memory_str}
   
   - 识别过去类似情况下的失误
   - 避免重复性错误
   - 应用成功经验
   - 改进决策流程
   - 确保不会因同样原因做出错误的买入/卖出/持有决策而造成损失

6. **决策置信度评估**
   
   - **高置信度（80-100%）：** 证据充分，信号明确
   - **中等置信度（50-80%）：** 证据合理，但存在不确定性
   - **低置信度（<50%）：** 证据不足，高度不确定

7. **最终交付内容**
   
   必须包含：
   - **明确的决策：** BUY / SELL / HOLD
   - **决策置信度：** 百分比和理由
   - **详细理由：** 基于辩论的分析
   - **优化后的计划：** 调整后的交易员计划
   - **风险管理措施：** 具体的风控措施
   - **监控指标：** 需要跟踪的关键指标
   - **退出条件：** 何时重新评估或退出

**分析师辩论历史：**
{history}

**输出要求：**
- 结构清晰、逻辑严密
- 决策明确、果断
- 理由充分、有说服力
- 可执行性强
- 风险管理完善
- 从历史教训中学习

记住：你的决策将直接影响交易执行。必须基于辩论中的最佳洞察，结合历史教训，做出明智、果断、可执行的决策。专注于可操作的见解和持续改进。建立在过去的教训之上，批判性地评估所有观点，确保每个决策都能推动更好的结果。
"""

        response = llm.invoke(prompt)

        new_risk_debate_state = {
            "judge_decision": response.content,
            "history": risk_debate_state["history"],
            "risky_history": risk_debate_state["risky_history"],
            "safe_history": risk_debate_state["safe_history"],
            "neutral_history": risk_debate_state["neutral_history"],
            "latest_speaker": "Judge",
            "current_risky_response": risk_debate_state["current_risky_response"],
            "current_safe_response": risk_debate_state["current_safe_response"],
            "current_neutral_response": risk_debate_state["current_neutral_response"],
            "count": risk_debate_state["count"],
        }

        return {
            "risk_debate_state": new_risk_debate_state,
            "final_trade_decision": response.content,
        }

    return risk_manager_node
