from dataclasses import dataclass
import yaml

from src.standarts_auditing_platform.sap_question import SAP_question


@dataclass
class A_field:
    name: str
    required: bool
    __answer = None
    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, value):
        self.__answer = value


class SAP_audit:
    _name: str
    _standard: str
    _definition: str
    _author: dict
    _fields: list[A_field]
    _questions: list[SAP_question]

    def __init__(self, config_path: str):
        self.__something(self.__validate(self.__load(config_path)))

    def start(self):
        for index, field in enumerate(self._fields):
            yield index, field

        for index, quest in enumerate(self._questions):
            yield index, quest

    def answer(self, index, _quest: A_field | SAP_question, answer):
        if isinstance(_quest, A_field):
            # !допилить валидацию
            self._fields.__getitem__(index).answer = answer
        elif isinstance(_quest, SAP_question):
            if isinstance(answer, list) and any(isinstance(el, int) for el in answer):
                self._questions.__getitem__(index).select(answer)
            else:
                raise ValueError("answer for Question must be List[int]")
        else:
            raise ValueError("_quest must be SAP_question or A_field")

    def report(self):
        # DRAFT !!!
        return self._fields, self._questions

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
        self._name = yaml_data['name']
        self._standard = yaml_data['standard']
        self._definition = yaml_data['definition']
        self._fields = [
            A_field(field['name'], field['required'])
            for field in yaml_data['fields']
        ]
        self._questions = [
            SAP_question(quest['question'], quest['options'], quest['true_selected']) for
            quest in yaml_data['questions']
        ]
        print(self.__dict__, sep='\n')


if __name__ == '__main__':
    sapa = SAP_audit('../../templates/config-sample.yaml')

    test_ = 1
    for i, quest in sapa.start():
        if isinstance(quest, A_field):
            print('Field: ', i, quest.name)
            sapa.answer(i, quest, str(test_))
            test_ += 123
        elif isinstance(quest, SAP_question):
            print('Q: ', i, quest.text, *quest.options)
            sapa.answer(i, quest, [1, 2])

    f, q = sapa.report()

    for i in f:
        print("F: ", i.name, "\t|\t", i.answer)
    for i in q:
        print('Q: ', i.text, i.selected, i.right)