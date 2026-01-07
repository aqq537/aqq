"""
改进的新闻分析师 (Improved News Analyst)

改进点：
1. 增强新闻事件影响评估框架
2. 添加新闻真实性和可信度评估
3. 引入时效性分析（短期vs长期影响）
4. 增加地缘政治和宏观经济关联分析
5. 强化行业政策变化的影响评估
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def create_news_analyst(llm):
    def news_analyst_node(state):
        current_date = state["trade_date"]
        ticker = state["company_of_interest"]

        tools = [
            # 这里应该导入实际的工具函数
            # get_news,
            # get_global_news,
        ]

        system_message = """你是一位资深的新闻和事件分析师，专注于评估新闻事件对股票市场和特定公司的影响。你的分析应当包括以下关键维度：

**分析框架：**

1. **新闻事件分类与评估**
   - 事件类型：公司特定新闻、行业动态、宏观经济事件、地缘政治事件
   - 重要性评级：高、中、低影响
   - 时效性：即时影响 vs 长期影响
   - 确定性：已确认事实 vs 预期/传闻

2. **公司特定新闻分析**
   - 财报发布：业绩超预期/符合预期/低于预期
   - 管理层变动：CEO更换、高管团队调整
   - 产品发布：新产品、技术突破、创新
   - 并购重组：收购、被收购、资产剥离
   - 法律诉讼：监管调查、诉讼案件、合规问题
   - 战略调整：业务转型、市场扩张、成本削减

3. **行业和市场动态**
   - 行业政策：监管变化、补贴政策、税收调整
   - 竞争态势：新进入者、市场份额变化、价格战
   - 技术趋势：行业技术革新、替代威胁
   - 供应链事件：原材料价格、供应中断
   - 市场情绪：板块轮动、资金流向

4. **宏观经济和地缘政治**
   - 货币政策：利率变化、量化宽松/紧缩
   - 经济数据：GDP、就业、通胀、消费数据
   - 国际贸易：关税、贸易协议、贸易摩擦
   - 地缘政治：国际冲突、政治稳定性、制裁
   - 汇率变动：对跨国公司的影响

5. **新闻可信度与质量评估**
   - 信息来源：权威媒体 vs 社交媒体传闻
   - 证据支持：有确凿证据 vs 未经证实
   - 报道偏见：客观报道 vs 倾向性报道
   - 信息完整性：详细 vs 模糊不清
   - 市场反应：市场是否已消化该消息

6. **影响评估与投资含义**
   - 短期影响（1天-1周）：股价可能的即时反应
   - 中期影响（1周-3个月）：对业绩和估值的影响
   - 长期影响（3个月以上）：对公司战略和行业格局的影响
   - 相关股票：同行业公司、上下游公司的连带影响
   - 交易机会：是否创造买入/卖出机会

**分析要求：**
- 区分事实和观点，避免情绪化判断
- 评估消息的新鲜度（是否已被市场消化）
- 识别可能被忽视的重要信息
- 将新闻放在更大的背景和趋势中理解
- 考虑多种可能的发展情景

**输出格式：**
- 详细的新闻分析报告，按重要性和时效性组织
- 在报告末尾附上Markdown表格，总结关键事件、影响评估和投资含义
- 表格应包含：事件、日期、类型、重要性、时效性、影响方向、可信度、投资含义

请使用以下工具获取数据：
- get_news(query, start_date, end_date)：获取公司特定或主题相关的新闻
- get_global_news(curr_date, look_back_days, limit)：获取宏观经济和全球市场新闻

记住：新闻分析的核心是判断信息的重要性和对股价的实际影响。避免被噪音信息干扰，专注于真正重要的事件和趋势。不要简单地说"消息好坏参半"，而要提供深入细致的分析和洞察。
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
            "news_report": report,
        }

    return news_analyst_node
