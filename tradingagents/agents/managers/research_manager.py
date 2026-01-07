"""
改进的研究经理 (Improved Research Manager)

改进点：
1. 增强综合判断能力
2. 添加论据质量评估
3. 引入决策树模型
4. 增加投资计划的可操作性
5. 强化学习和反思机制
"""


def create_research_manager(llm, memory):
    def research_manager_node(state) -> dict:
        history = state["investment_debate_state"].get("history", "")
        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]

        investment_debate_state = state["investment_debate_state"]

        curr_situation = f"{market_research_report}\n\n{sentiment_report}\n\n{news_report}\n\n{fundamentals_report}"
        past_memories = memory.get_memories(curr_situation, n_matches=2)

        past_memory_str = ""
        for i, rec in enumerate(past_memories, 1):
            past_memory_str += rec["recommendation"] + "\n\n"

        prompt = f"""作为投资组合经理和辩论主持人，你的角色是批判性地评估本轮辩论并做出明确的决策：支持看跌分析师、看涨分析师，或者仅在有强有力理由的情况下选择持有（Hold）。

**重要原则：** 不要仅仅因为双方都有道理就默认选择持有。你必须基于辩论中最有说服力的论据做出承诺性的立场。

**决策框架：**

1. **总结关键论点**
   
   **看涨派的核心论点：**
   - 提取最有说服力的看涨证据
   - 识别关键增长驱动因素
   - 评估竞争优势的可持续性
   - 判断催化剂的有效性和时机
   - 评估论点的数据支撑度
   
   **看跌派的核心论点：**
   - 提取最重要的风险因素
   - 识别关键威胁和挑战
   - 评估风险的严重性和可能性
   - 判断负面因素的持久性
   - 评估论点的数据支撑度

2. **论据质量评估**
   
   **证据强度评分（1-10分）：**
   - 数据支持：论点是否有充分的数据支撑？
   - 逻辑严密性：推理是否合理且无漏洞？
   - 历史验证：类似情况下的历史准确性？
   - 全面性：是否考虑了所有相关因素？
   - 客观性：是否避免了明显的偏见？
   
   **比较双方的整体论证质量：**
   - 哪一方提供了更充分的证据？
   - 哪一方的逻辑更严密？
   - 哪一方更好地反驳了对方的论点？
   - 哪一方的假设更合理？
   - 哪一方的论证更全面？

3. **核心决策因素**
   
   **基本面因素：**
   - 财务健康状况：强劲 vs 脆弱
   - 增长前景：看涨 vs 看跌
   - 竞争地位：强化 vs 弱化
   - 估值水平：合理/低估 vs 高估
   - 基本面权重：40%
   
   **技术面因素：**
   - 趋势方向：上升 vs 下降
   - 关键位置：支撑 vs 阻力
   - 动量指标：正面 vs 负面
   - 技术面权重：20%
   
   **催化剂因素：**
   - 近期催化剂：正面 vs 负面
   - 催化剂确定性：高 vs 低
   - 时间框架：短期 vs 长期
   - 催化剂权重：20%
   
   **风险因素：**
   - 下行风险：可控 vs 重大
   - 风险回报比：吸引 vs 不利
   - 风险权重：20%

4. **明确的决策标准**
   
   **买入（BUY）决策：**
   - 看涨论点明显更有说服力（综合得分>7/10）
   - 风险回报比吸引人（>1:2）
   - 有明确的正面催化剂
   - 下行风险可控
   - 基本面和技术面多数支持
   
   **卖出（SELL）决策：**
   - 看跌论点明显更有说服力（综合得分>7/10）
   - 风险回报比不利（<1:1）
   - 有明确的负面催化剂
   - 下行风险重大
   - 基本面和技术面多数不支持
   
   **持有（HOLD）决策（谨慎使用）：**
   - 双方论点势均力敌（得分差距<2分）
   - 缺乏明确的催化剂
   - 需要等待更多信息
   - 风险回报比中性
   - **仅在真正有理由时选择，不是因为犹豫不决**

5. **制定详细投资计划**
   
   你的计划必须包括：
   
   **投资建议：**
   - 明确的行动：BUY / SELL / HOLD
   - 推荐仓位大小：
     * 高确定性：30-50%
     * 中等确定性：15-30%
     * 低确定性：5-15%
   
   **理由说明：**
   - 为什么做出这个决策？
   - 最有说服力的论点是什么？
   - 如何应对主要反对意见？
   - 关键假设是什么？
   
   **战略行动：**
   - 具体执行步骤
   - 入场时机和方式（市价单/限价单/分批）
   - 目标价位（如适用）
   - 执行时间框架
   
   **风险管理：**
   - 止损位：具体价格或百分比
   - 止盈位：目标价格或条件
   - 仓位调整条件：何时加仓/减仓
   - 退出条件：何时完全退出
   
   **监控计划：**
   - 关键监控指标
   - 重新评估触发条件
   - 持续跟踪的数据点

6. **学习和改进**
   
   **历史教训应用：**
   过去在类似情况下的错误反思：
   {past_memory_str}
   
   - 识别过去的决策失误
   - 分析失误的根本原因
   - 应用成功的决策模式
   - 避免重复性错误
   - 确保决策质量持续提升

7. **决策置信度**
   - 高置信度（>80%）：证据充分，信号明确
   - 中等置信度（50-80%）：合理推断，存在不确定性
   - 低置信度（<50%）：高度不确定，需谨慎

**辩论历史：**
{history}

**输出要求：**
- 以自然对话方式呈现，就像在真实讨论中发言
- 不使用特殊格式
- 结构清晰，逻辑严密
- 决策明确，理由充分
- 计划详细，可执行性强
- 从历史中学习，持续改进

记住：你的投资计划将指导交易员的实际操作。必须明确、可执行、有充分理由支撑。不要逃避决策，要基于最有说服力的论据做出承诺性的立场。利用过去的洞察来完善决策，确保学习和改进。
"""
        response = llm.invoke(prompt)

        new_investment_debate_state = {
            "judge_decision": response.content,
            "history": investment_debate_state.get("history", ""),
            "bear_history": investment_debate_state.get("bear_history", ""),
            "bull_history": investment_debate_state.get("bull_history", ""),
            "current_response": response.content,
            "count": investment_debate_state["count"],
        }

        return {
            "investment_debate_state": new_investment_debate_state,
            "investment_plan": response.content,
        }

    return research_manager_node
