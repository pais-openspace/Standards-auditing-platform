import yaml

class SAP_config:


    def __init__(self, config_path: str):

        print(config_path)

        with open(config_path, 'r', encoding='utf8') as config_file:
            config = yaml.safe_load(config_file)
            print(config)





if __name__ == '__main__':
    SAP_config('../../templates/config-sample.yaml')