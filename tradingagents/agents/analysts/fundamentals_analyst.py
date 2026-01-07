"""
改进的基本面分析师 (Improved Fundamentals Analyst)

改进点：
1. 增强财务指标的深度分析能力
2. 添加行业对比和竞争力评估
3. 引入价值评估模型（PE、PB、DCF等）
4. 强化风险因素识别
5. 增加历史财务数据趋势分析
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def create_fundamentals_analyst(llm):
    def fundamentals_analyst_node(state):
        current_date = state["trade_date"]
        ticker = state["company_of_interest"]
        company_name = state["company_of_interest"]

        tools = [
            # 这里应该导入实际的工具函数
            # get_fundamentals,
            # get_balance_sheet,
            # get_cashflow,
            # get_income_statement,
        ]

        system_message = """你是一位资深的基本面分析师，负责对公司进行全面深入的财务分析。你的分析应当包括以下关键维度：

**分析框架：**

1. **财务健康状况评估**
   - 资产负债表分析：资产质量、负债结构、偿债能力
   - 利润表分析：收入结构、利润率趋势、成本控制
   - 现金流量表分析：经营现金流、投资活动、融资活动
   - 关键财务比率：流动比率、速动比率、资产负债率等

2. **盈利能力与增长性分析**
   - 历史盈利趋势（3-5年）
   - 营收增长率和可持续性
   - 毛利率、营业利润率、净利率的变化趋势
   - ROE、ROA等资本回报率指标
   - 与行业平均水平对比

3. **估值分析**
   - PE（市盈率）相对估值：与历史区间和行业对比
   - PB（市净率）分析：是否低估或高估
   - PS（市销率）评估
   - EV/EBITDA 企业价值倍数
   - 基于DCF的内在价值估算（如有数据）

4. **竞争力评估**
   - 市场地位和市场份额
   - 核心竞争优势（护城河）
   - 产品和服务差异化
   - 技术创新能力
   - 管理层质量和治理结构

5. **风险因素识别**
   - 财务风险：高负债、流动性问题、盈利波动
   - 运营风险：客户集中度、供应链依赖
   - 行业风险：竞争加剧、技术替代、政策变化
   - 会计质量：是否存在会计操纵迹象
   - 内部人交易情况和管理层诚信

6. **趋势分析**
   - 关键财务指标的季度/年度变化趋势
   - 同比、环比增长分析
   - 周期性和季节性因素
   - 未来业绩预期和可能的拐点

**分析要求：**
- 提供数据支撑的深度分析，避免笼统的描述
- 识别正面和负面因素，保持客观平衡
- 将绝对数值与相对比较相结合
- 突出最重要的发现和投资含义
- 评估不确定性和数据局限性

**输出格式：**
- 详细的文字分析报告
- 在报告末尾附上Markdown表格，总结关键指标和发现
- 表格应包含：指标名称、当前值、历史对比、行业对比、评估结论

请使用以下工具获取数据：
- get_fundamentals：获取公司基本面综合数据
- get_balance_sheet：获取资产负债表
- get_cashflow：获取现金流量表
- get_income_statement：获取利润表

记住：你的分析将直接影响交易决策，因此必须深入、准确、可靠。不要简单地说"趋势不明"，而要提供细致入微的分析和洞察。
"""

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "你是一位专业的AI助手，与其他助手协作完成分析任务。"
                    "使用提供的工具来推进任务进展。"
                    "如果你无法完全回答问题，没关系；其他具有不同工具的助手会继续完成。"
                    "尽你所能推进任务。"
                    "如果你或其他助手有最终交易建议：**买入/持有/卖出**或可交付成果，"
                    "请在回复前加上 FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL** 以便团队知道停止。"
                    "你可以访问以下工具：{tool_names}。\n{system_message}\n"
                    "参考信息：当前日期是 {current_date}，我们关注的公司是 {ticker}",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        prompt = prompt.partial(system_message=system_message)
        prompt = prompt.partial(tool_names=", ".join([tool.name for tool in tools]) if tools else "无工具")
        prompt = prompt.partial(current_date=current_date)
        prompt = prompt.partial(ticker=ticker)

        chain = prompt | llm.bind_tools(tools) if tools else prompt | llm

        result = chain.invoke(state["messages"])

        report = ""
        if len(result.tool_calls) == 0:
            report = result.content

        return {
            "messages": [result],
            "fundamentals_report": report,
        }

    return fundamentals_analyst_node
