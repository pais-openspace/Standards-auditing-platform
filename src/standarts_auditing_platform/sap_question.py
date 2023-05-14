
class SAP_question:
    """
    Представление вопроса
    """
    text: str
    options: tuple[int, str]
    true_selected: list[int]

    def __init__(self, text: str, options: tuple[int, str], true_selected: list[int]):
        self.text = text
        self.options = options
        self.true_selected = true_selected
        self.selected = None

    @property
    def right(self) -> bool:
        """

        :return: Правильность ответа
        """
        return self.true_selected == self.selected

    def select(self, option_id: list[int]) -> None:
        """

        :param option_id: id ответа
        :return:
        """
        self.selected = option_id
