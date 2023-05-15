from dataclasses import dataclass
import yaml
import jinja2

from src.standarts_auditing_platform.sap_question import SAP_question


@dataclass
class A_field:
    name: str
    required: bool
    value = None
    @property
    def answer(self):
        return self.value

    @answer.setter
    def answer(self, value):
        self.value = value


class SAP_audit:
    name: str
    standard: str
    definition: str
    author: dict

    fields: list[A_field]
    questions: list[SAP_question]

    report_template: str

    def __init__(self, config_path: str):
        self.__something(self.__validate(self.__load(config_path)))

    def start(self):
        for index, field in enumerate(self.fields):
            yield index, field

        for index, quest in enumerate(self.questions):
            yield index, quest

    def answer(self, index, _quest: A_field | SAP_question, answer):
        if isinstance(_quest, A_field):
            # !допилить валидацию
            self.fields.__getitem__(index).answer = answer
        elif isinstance(_quest, SAP_question):
            if isinstance(answer, list) and any(isinstance(el, int) for el in answer):
                self.questions.__getitem__(index).select(answer)
            else:
                raise ValueError("answer for Question must be List[int]")
        else:
            raise ValueError("_quest must be SAP_question or A_field")

    def report(self):
        # DRAFT !!!
        self.score = sum([1 for quest in self.questions if quest.right]) / len(self.questions)
        tmp = jinja2.Template(self.report_template)
        report = tmp.render(**self.__dict__)
        return report

    def __load(self, path: str) -> dict | Exception:
        """

        :param path: путь до файла
        :type path:
        :return:
        :rtype:
        """
        try:
            with open(path, 'r', encoding='utf8') as config_file:
                config = yaml.safe_load(config_file)
                return config
        except yaml.YAMLError as e:
            print("Error in configuration file:", e)
        except Exception as e:
            print(e)

    def __validate(self, yaml_data: dict) -> dict:
        """
        Метод проверяет правильность
        :param yaml_data:
        :type yaml_data:
        :return:
        :rtype:
        """
        # Нужно добавить валидацию
        return yaml_data

    def __something(self, yaml_data: dict):
        self.name = yaml_data['name']
        self.standard = yaml_data['standard']
        self.definition = yaml_data['definition']

        self.author = yaml_data['author']

        self.fields = [
            A_field(field['name'], field['required'])
            for field in yaml_data['fields']
        ]
        self.questions = [
            SAP_question(quest['question'], quest['options'], quest['true_selected']) for
            quest in yaml_data['questions']
        ]

        self.report_template = yaml_data['report']['template']


if __name__ == '__main__':
    sapa = SAP_audit('../../templates/config-sample.yaml')

    test_ = 1
    for i, quest in sapa.start():
        if isinstance(quest, A_field):
            print('F: ', i, quest.name)
            sapa.answer(i, quest, str(input('F: '+str(i)+" "+quest.name+' : ')))
            test_ += 123
        elif isinstance(quest, SAP_question):
            print('Q: ', i, quest.text, *quest.options)
            sapa.answer(i, quest, [int(select) for select in input('F: '+str(i)+" "+quest.text+' : ').split()])

    report = sapa.report()
    print(report)

    # for i in f:
    #     print("F: ", i.name, "\t|\t", i.answer)
    # for i in q:
    #     print('Q: ', i.text, i.selected, i.right)