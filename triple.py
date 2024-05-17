import yaml


# 进行语句中实体识别
def ner():
    config_path = "config/config.yaml"
    with open(config_path, encoding='utf-8') as r:
        config = yaml.load(r, Loader=yaml.FullLoader)
