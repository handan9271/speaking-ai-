
import Processing
import prompts


article = prompts.S_article()

prompt1 = Processing.getScore()

prompt2 = Processing.getSuggestion()

prompt3 = Processing.getTR()

prompt4 = Processing.getLR()

prompt6 = Processing.getN_article()

prompt5 = Processing.getDeftctive()

prompt7 = Processing.getSummery()

Details = f"""Original：原文
Issue：问题
Comment：建议
Enhanced：细节升级
"""
Mian = f"""本评分报告是基于您提供的样本通过 AI 生成。请注意，由于真实考场环境和评分标准可能与 AI 的分析和评分方法存在差异，因此本报告中的分数仅供参考，不能完全反映您在实际雅思考试中的表现。

雅思考试评分包含一定程度的主观性，不同考官可能会有不同的评分标准和偏好。因此，本报告的评分结果不能保证与实际雅思考官的评分完全一致。

建议您将本报告作为一种学习和练习的工具，用于辅助您的雅思备考，而非作为最终成绩的预测或保证。真实的考试成绩取决于多种因素，包括但不限于考试当天的表现、考官的评分标准以及考试环境等。
"""
