## 👏 项目介绍

基于GLM-4构建的知识图谱工具。 

相关模块包括：
- 爬虫工厂：自动定时爬取相关来源新闻
- NER(命名实体识别)：识别文本中的实体对象
- RE(关系抽取)：对于实体之间相关关系进行抽取
- EE(事件抽取)：对于事件内容主体、客体、时间、结果进行抽取
- 知识问答：基于openapi以及网络来源知识的问答。
- 新闻可信度分析：基于本地数据库相关知识以及web_search知识的可信度分析模块。

## 🚀 Get Start

### config

修改`config/config.yaml`中的配置，填写你的api-key，模型默认为glm-4。

```yaml
glm:
  # input your api_key here
  api_key: xxxxxxxxxxxxxxxxxx
  # select model used
  model: glm-4
```