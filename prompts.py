import Get

folder_path = "articles"
S_name = Get.getName()
S_article = Get.getArticle()


prompt1 = f"""
请基于雅思四项评分细则逐一对以下文章进行评分,请注意，我需要中英文对照版：
{S_article}

以下是输出样例，请注意，你只能学习以下样例中的排版布局和格式且要严格遵守该格式，不能学习其中的内容：
### 任务回应情况（Task Response）: 6
- **Analysis**: The essay addresses the topic, discussing the advantages of younger leaders. The writer's opinion is clear, but the arguments are not fully developed or supported with detailed examples. 
- **中文分析**: 这篇文章讨论了年轻领导者的优势，回应了题目。作者的观点清晰，但论点未完全发展，也未用详细例子支持。

### 连贯与衔接（Coherence and Cohesion）: 5
- **Analysis**: The essay's structure is basic, and ideas are somewhat organized. However, transitions between ideas are weak, and the overall coherence could be
improved with better paragraphing. 
- **中文分析**: 文章结构基本，观点有一定组织，但观点间过渡弱，通过更好的段落划分可以提高整体连贯性。

### 词汇丰富程度（Lexical Resource）: 6
- **Analysis**: The writer uses a range of vocabulary, but with some inaccuracies and repetition. Word choice could be more varied to enhance expression. 
- **中文分析**: 作者使用了一定范围的词汇，但有些不准确和重复。词汇选择可以更多样化以增强表达。

### 语法多样性及准确性（Grammatical Range and Accuracy）: 5
- **Analysis**: The essay shows some grammatical range, but there are notable errors in sentence structure and verb tense. These errors occasionally hinder clarity.
- **中文分析**: 文章显示了一些语法范围，但在句子结构和动词时态上有显著
错误。这些错误偶尔会影响清晰度。

### 总体评分 (Overall): 5.5
- **Analysis**: While the essay addresses the topic and presents a clear position, it needs more development in terms of argument support, coherence, lexical variety, and grammatical accuracy. 
- **中文分析**: 虽然文章回应了题目并提出了明确立场，但在论点支持、连贯性、词汇多样性和语法准确性方面需要进一步发展。


如果总体评分(Overall)为类似“6.25”这样的数字，根据雅思评分标准，实际分数应为“6”分，请不要在评分中出现任何类似“6.25”这样的数字
如果总体评分(Overall)为类似“6.75”这样的数字，根据雅思评分标准，实际分数应为“6.5”分，请不要在评分中出现任何类似“6.75”这样的数字

"""

prompt2 = f"""
请基于雅思四项评分细则与以下文章，给出四个部分的评改建议
{S_article}

以下是输出样例，请注意，你只能学习以下样例中的排版布局和格式且要严格遵守该格式，不能学习其中的内容：

### 任务回应情况（Task Response）:
- **English**: Enhance your arguments by providing more specific examples and detailed explanations to support your points. This will strengthen the persuasiveness of your stance on the role of younger leaders. 
- **中文**: 通过提供更具体的例子和详细的解释来加强你的论点。这将增强你对年轻领导者作用的立场的说服力。

### 连贯与衔接（Coherence and Cohesion）:
- **English**: Improve the structure and flow of your essay. Utilize clear and effective transitional phrases to connect ideas smoothly and ensure each paragraph contributes to your overall argument. 
- **中文**: 改善文章的结构和流畅性。使用清晰有效的过渡短语顺利连接观点，并确保每个段落都有助于你的整体论点。

### 词汇丰富程度（Lexical Resource）:
- **English**: Broaden your vocabulary to express ideas more precisely. Avoid repetition and strive for a variety of expressions to articulate your points more effectively. 
- **中文**: 扩展你的词汇以更准确地表达观点。避免重复，努力寻找多种表达方式来更有效地表达你的观点。

### 语法多样性及准确性（Grammatical Range and Accuracy）:
- **English**: Focus on improving grammatical accuracy. Pay attention to sentence structure and verb tense consistency to enhance the clarity and professionalism of your writing. 
- **中文**: 专注于提高语法准确性。注意句子结构和动词时态的一致性，以提高你的写作清晰度和专业性
"""

prompt3 = f"""
以下文章在TR、CC层面分别在哪里扣了分？请注意，每个评分标准请分别举出3个例子说明。
{S_article}

以下是输出样例，请注意，你只能学习以下样例中的排版布局和格式且要严格遵守该格式，不能学习其中的内容：
### 任务回应情况（Task Response, TR）

1. **缺乏具体支持细节**
   - 原文: "I Agree younger should have chance to work as leader due to these two reasons."
   - 问题: 缺乏具体论点支持。
   - 优化: "I agree that younger individuals should lead, as they bring fresh perspectives and innovative strategies, crucial in today's rapidly evolving business landscape."
   - 解释: 提供了具体的理由支持为何年轻人应该担任领导角色。
   - 中文: "我同意年轻人应该担任领导角色，因为他们带来了新鲜的视角和创新策略，在当今快速发展的商业环境中至关重要。"

2. **论点发展不足**
   - 原文: "young directord can apply the latest technology and theory into practice..."
   - 问题: 论点表述过于笼统。
   - 优化: "Young leaders are adept at applying the latest technological advancements and theoretical models, enhancing organizational efficiency and adaptability."
   - 解释: 论点通过具体化描述，更为清晰。
   - 中文: "年轻领导者擅长应用最新的技术进步和理论模型，提高组织的效率和适应性。"

3. **结论部分简化**
   - 原文: "Overall the older leaders can give big pictures for the things However the young leaders are creative..."
   - 问题: 结论部分缺乏深度和清晰的比较。
   - 优化: "In conclusion, while older leaders offer valuable experience and a broad perspective, young leaders bring creativity and a strong grasp of contemporary trends, which are indispensable in modern business."
   - 解释: 结论更全面地比较了年轻和年长领导者的优势。
   - 中文: "总之，虽然年长领导者提供宝贵的经验和广阔的视角，但年轻领导者带来创造力和对当代趋势的深刻理解，在现代商业中不可或缺。"


### 连贯与衔接（Coherence and Cohesion, CC）

1. **缺乏有效过渡**
   - 原文: "Firstly, Compared with the senior leaders,young directord can apply..."
   - 问题: 缺乏有效的过渡和连接。
   - 优化: "Firstly, unlike senior leaders who may rely on traditional methods, young directors can effortlessly integrate..."
   - 解释: 提供了一个清晰的比较过渡，使文章更连贯。
   - 中文: "首先，与可能依赖传统方法的资深领导者不同，年轻的主管可以轻松地融合..."

2. **段落结构混乱**
   - 原文: "Secondly, in the current scenario, younger leaders are bustling with creative ideas..."
   - 问题: 段落主题不明确。
   - 优化: "Secondly, in today's dynamic business environment, younger leaders stand out with their creative ideas and readiness to embrace new challenges."
   - 解释: 明确了段落的主题和内容。
   - 中文: "其次，在当今充满活力的商业环境中，年轻领导者凭借他们的创意思维和面对新挑战的准备突显出来。"

3. **结论部分过于简单**
   - 原文: "Overall the older leaders can give big pictures for the things However the young leaders are creative..."
   - 问题: 结论部分过于简单，未有效总结文章主题。
   - 优化: "In conclusion, the comparison between older and younger leaders reveals that while experience is invaluable, the innovation and adaptability young leaders bring are critical in today's world."
   - 解释: 提供了一个全面的结论，有效地总结了文章的主题。
   - 中文: "总结来说，对比年长和年轻领导者显示，虽然经验宝贵，但年轻领导者带来的创新和适应性在当今世界至关重要。"
"""

prompt4 = f"""
以下文章在LR、GRA层面分别在哪里扣了分？请注意，每个评分标准请分别举出3个例子说明。
{S_article}

以下是输出样例，请注意，你只能学习以下样例中的排版布局和格式且要严格遵守该格式，不能学习其中的内容：
### 词汇丰富程度（Lexical Resource, LR）

1. **词汇重复和使用不当**
   - 原文: "young directord can apply the latest technology and theory into practice..."
   - 问题: "apply" 和 "technology and theory" 重复和用词不当。
   - 优化: "Young leaders are adept at harnessing contemporary technologies and innovative theories to enhance business practices."
   - 解释: 使用了更丰富和准确的词汇来表达相同的意思。
   - 中文: "年轻领导者擅长利用当代技术和创新理论来提升商业实践。"

2. **过度简化的词汇**
   - 原文: "they are not hesitant to implement them in their businesses."
   - 问题: 表达过于简化，缺乏精确性。
   - 优化: "they display a proactive approach in integrating these concepts into their strategic planning."
   - 解释: 使用更专业和精确的词汇来提升表达的质量。
   - 中文: "他们在将这些概念融入其战略规划中表现出积极主动的态度。"

3. **词汇选择不恰当**
   - 原文: "Exemplify, Bill Gates started his companies Microsoft at a young age..."
   - 问题: "Exemplify" 用词不恰当。
   - 优化: "For example, Bill Gates founded Microsoft at a young age..."
   - 解释: 更准确地使用例证。
   - 中文: "例如，比尔·盖茨在年轻时创立了微软公司..."

### 语法多样性及准确性（Grammatical Range and Accuracy, GRA）

1. **时态和语法结构错误**
   - 原文: "I Agree younger shouldhave chance to work as leader..."
   - 问题: 时态和语法结构错误。
   - 优化: "I agree that younger individuals should have the opportunity to serve as leaders..."
   - 解释: 修正了时态和语法错误，使句子更加准确。
   - 中文: "我同意年轻人应该有机会担任领导角色..."

2. **句式结构单调**
   - 原文: "young directord can apply the latest technology and theory into practice..."
   - 问题: 句式结构单调，缺乏多样性。
   - 优化: "Young leaders are capable of innovatively applying cutting-edge technology and theoretical insights in practical scenarios."
   - 解释: 使用了更复杂和多样化的句式结构。
   - 中文: "年轻领导者能够在实际场景中创新地应用尖端技术和理论见解。"

3. **语法错误和不清晰**
   - 原文: "but young leaders have signifcantly a plethora of advantages including fresh perspectives,innovelative ideas, and a close connection to the latest trends and technologies."
   - 问题: 语法错误和表达不清晰。
   - 优化: "However, young leaders possess a significant array of advantages, including fresh perspectives, innovative ideas, and a strong connection to the latest trends and technologies."
   - 解释: 纠正了语法错误并清晰地表达了意思。
   - 中文: "然而，年轻领导者拥有大量优势，包括新鲜视角、创新思想以及与最新趋势和技术的紧密联系。"    

"""

prompt6 = f"""
Here's my article
{S_article}
How would you write this article？

以下是输出样例，请注意，你只能学习以下样例中的排版布局和格式且要严格遵守该格式，不能学习其中的内容：
**Title: The Quintessential Objective of Science: Elevating Human Existence**

In the realm of human intellectual endeavor, the discourse frequently orbits around the pivotal role of science. Predominantly, it's posited that the zenith of scientific pursuit should be the betterment of human life. I wholeheartedly subscribe to this notion, contending that the essence of scientific advancement inherently intertwines with elevating the human condition.

**Paragraph 1: Communication Revolution through Scientific Innovation**
Initially, the transformative impact of science on human communication merits consideration. The evolution from rudimentary to advanced telecommunication exemplifies this paradigm shift. Consider the ubiquitous smartphone - a marvel of scientific ingenuity - transforming not just the efficiency of communication but also transcending geographical boundaries. This quantum leap from the protracted processes of yore to instantaneous connectivity epitomizes the core of scientific advancement: making the once-impossible, a tangible reality.

**Paragraph 2: Prolonging Life - The Apex of Scientific Achievement**
Furthermore, the prolongation of human lifespan stands as a testament to science's profound impact. The realm of life sciences, relentlessly focused on longevity, showcases remarkable strides in this aspect. For instance, consider the evolution of cancer treatment. Once deemed incurable and a harbinger of mortality, it now succumbs to a myriad of therapeutic strategies. This revolution in medical science, turning the tide against erstwhile fatal diseases, underscores the pivotal role of scientific progress in augmenting the human life span.

**Conclusion: The Indispensable Role of Science in Enhancing Life**
In conclusion, the role of science in ameliorating human life is both irreplaceable and multidimensional. It has revolutionized our means of communication and has significantly extended our lifespan. Asserting that the ultimate aim of science is to enhance the quality and longevity of human life is not just an observation but a recognition of its profound and diverse impacts on our existence.

"""

prompt5 = f"""
Here's my article
{S_article}
find out 10 defective sentences in my article, tell me the issue, make key comments and give enhanced answer, I need a bilingual version in both Chinese and English.

以下是输出样例，请注意，你只能学习以下样例中的排版布局和格式且要严格遵守该格式，不能学习其中的内容，且不能输出任何多余的话：
1. Original: "Science is the core element for the advancing of human civilization."
- Issue: Grammatical awkwardness and redundancy.
- Enhanced: "Science is the core element in advancing human civilization."
- 中文: "科学是推进人类文明的核心要素。"
- 考官点评: "for the advancing of"这个短语很鸡肋，可以更精简的表达。

"""

prompt7 = f"""
Here's my article
{S_article}
基于我的文章给我5条提升建议。

以下是输出样例，请注意，你只能学习以下样例中的排版布局和格式且要严格遵守该格式，不能学习其中的内容：

1. **精炼并明确表达（Refine and Clarify Expression）**:
   - **English**: Aim for concise and clear statements. Avoid wordiness and ensure that each sentence directly contributes to your argument.
   - **中文**: 力求简洁明了的表达。避免冗长，并确保每个句子直接支持您的论点。

"""
