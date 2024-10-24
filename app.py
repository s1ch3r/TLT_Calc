import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton, QComboBox, QTableWidget, QTableWidgetItem
#from logic import Logic


class MyApp(QWidget):
    def __init__(self):
        super().__init__()


        # Переменные на значения (не LineEdit или типо того) возможно они юзлесс

        # Инициализация переменных
        self.wide = ""
        self.reservoir_temperature_val = ""
        self.max_product_temperature = ""
        self.min_environment_temperature = ""
        self.max_environment_temperature = ""
        self.truba = ""

        # Новые поля
        """
        self.additional_var1 =
        ...
        self.additionnal_var12 =
        """
        

        # Настройка пользовательского интерфейса
        self.initUI()

    def initUI(self):
        # Создание основного вертикального макета
        layout = QVBoxLayout()

        # layout колонок для ввода
        h_layout_columns = QHBoxLayout()

        # Создаем левый, правый и третий столбцы
        left_column_layout = self.create_left_column()
        right_column_layout = self.create_right_column()
        third_column_layout = self.create_third_column()

        # Добавляем левый, правый и третий столбцы в основной горизонтальный макет
        h_layout_columns.addLayout(left_column_layout)
        h_layout_columns.addLayout(right_column_layout)
        h_layout_columns.addLayout(third_column_layout)

        # Добавляем горизонтальный макет столбцов в основной вертикальный макет
        layout.addLayout(h_layout_columns)

        # Кнопка для подтверждения выбора
        self.submit_button = QPushButton("Подтвердить выбор", self)
        self.submit_button.clicked.connect(self.update_truba)
        layout.addWidget(self.submit_button)

        # Кнопки "Исходные данные" и "Результаты расчета"
        buttons_layout = QHBoxLayout()
        self.source_data_button = QPushButton("Исходные данные", self)
        self.source_data_button.clicked.connect(self.show_source_data_table)
        self.result_button = QPushButton("Результаты расчета", self)
        self.result_button.clicked.connect(self.show_result_table)
        buttons_layout.addWidget(self.source_data_button)
        buttons_layout.addWidget(self.result_button)
        layout.addLayout(buttons_layout)

        # Метка для финального значения
        self.output_value_label = QLabel("Финальное значение: ", self)
        layout.addWidget(self.output_value_label)

        # Таблица для исходных данных
        self.source_data_table = QTableWidget(1, 18, self)
        self.source_data_table.setHorizontalHeaderLabels([
            "Толщина трубы", 
            "Треб. темп. резервуара", 
            "Макс. темп. продукта", 
            "Мин. темп. окр. среды", 
            "Макс. темп. окр. среды", 
            "Материал труб", 
            "Доп. поле 1", 
            "Доп. поле 2", 
            "Доп. поле 3", 
            "Доп. поле 4", 
            "Доп. поле 5", 
            "Доп. поле 6", 
            "Доп. поле 7", 
            "Доп. поле 8", 
            "Доп. поле 9", 
            "Доп. поле 10", 
            "Доп. поле 11", 
            "Доп. поле 12"
        ])
        layout.addWidget(self.source_data_table)

        # Таблица для результатов расчета (изначально скрыта)
        self.result_table = QTableWidget(1, 18, self)
        self.result_table.setHorizontalHeaderLabels([
            "Расчет для толщины трубы", 
            "Расчет для треб. темп. резервуара", 
            "Расчет для макс. темп. продукта", 
            "Расчет для мин. темп. окр. среды", 
            "Расчет для макс. темп. окр. среды", 
            "Результат для материала труб",
            "Расчет для доп. поля 1",
            "Расчет для доп. поля 2",
            "Расчет для доп. поля 3",
            "Расчет для доп. поля 4",
            "Расчет для доп. поля 5",
            "Расчет для доп. поля 6",
            "Расчет для доп. поля 7",
            "Расчет для доп. поля 8",
            "Расчет для доп. поля 9",
            "Расчет для доп. поля 10",
            "Расчет для доп. поля 11",
            "Расчет для доп. поля 12"
        ])
        self.result_table.setVisible(False)
        layout.addWidget(self.result_table)

        # Установка макета для основного окна
        self.setLayout(layout)

        # Настройка окна
        self.setWindowTitle('v0.3')
        self.setGeometry(0, 0, 1920, 1080)

    def create_left_column(self):
        """Создаёт макет для левого столбца"""
        left_column_layout = QVBoxLayout()


        self.wide_line_edit = QLineEdit()
        self.wide_line_edit.setPlaceholderText("0.00 мм")

        self.reservoir_temperature_line_edit = QLineEdit()
        self.reservoir_temperature_line_edit.setPlaceholderText("0 °C")

        self.max_product_temperature_line_edit = QLineEdit()
        self.max_product_temperature_line_edit.setPlaceholderText("0 °C")


        # additional fields 1 col
        self.additional_field1 = QLineEdit()
        self.additional_field1.setPlaceholderText("1")
        self.additional_field2 = QLineEdit()
        self.additional_field2.setPlaceholderText("2")
        self.additional_field3 = QLineEdit()
        self.additional_field3.setPlaceholderText("3")


        # Дополнительные поля
        left_column_layout.addLayout(self.create_line_edit_field("Толщина трубы: ", self.wide_line_edit))
        left_column_layout.addLayout(self.create_line_edit_field("Требуемая температура резервуара: ", self.reservoir_temperature_line_edit))
        left_column_layout.addLayout(self.create_line_edit_field("Макс. температура продукта: ", self.max_product_temperature_line_edit))
        left_column_layout.addLayout(self.create_line_edit_field("Доп. поле 1", self.additional_field1))
        left_column_layout.addLayout(self.create_line_edit_field("Доп. поле 2", self.additional_field2))
        left_column_layout.addLayout(self.create_line_edit_field("Доп. поле 3", self.additional_field3))

        return left_column_layout

    def create_right_column(self):
        """Создаёт макет для правого столбца"""
        right_column_layout = QVBoxLayout()

        # Материал труб
        h_layout_material = QHBoxLayout()
        label_material = QLabel("Материал труб: ")
        self.material_combobox = QComboBox()
        self.material_combobox.addItems(["", "Сталь углеродистая", "Сталь нержавеющая", "Чугун", "Медь", "Латунь", "Алюминий"])
        h_layout_material.addWidget(label_material)
        h_layout_material.addWidget(self.material_combobox)
        right_column_layout.addLayout(h_layout_material)


        self.min_environment_temperature_line_edit = QLineEdit()
        self.min_environment_temperature_line_edit.setPlaceholderText("0 °C")

        self.max_environment_temperature_line_edit = QLineEdit()
        self.max_environment_temperature_line_edit.setPlaceholderText("0 °C")


        # add fields 2 col
        self.additional_field4 = QLineEdit()
        self.additional_field4.setPlaceholderText("4")
        self.additional_field5 = QLineEdit()
        self.additional_field5.setPlaceholderText("5")
        self.additional_field6 = QLineEdit()
        self.additional_field6.setPlaceholderText("6")

        # Дополнительные поля
        right_column_layout.addLayout(self.create_line_edit_field("Мин. температура окружающей среды: ", self.min_environment_temperature_line_edit))
        right_column_layout.addLayout(self.create_line_edit_field("Макс. температура окружающей среды: ", self.max_environment_temperature_line_edit))
        right_column_layout.addLayout(self.create_line_edit_field("Доп. поле 4", self.additional_field4))
        right_column_layout.addLayout(self.create_line_edit_field("Доп. поле 5", self.additional_field5))
        right_column_layout.addLayout(self.create_line_edit_field("Доп. поле 6", self.additional_field6))

        return right_column_layout

    def create_third_column(self):
        """Создаёт макет для третьего столбца"""
        third_column_layout = QVBoxLayout()

        self.additional_field7 = QLineEdit()
        self.additional_field7.setPlaceholderText("7")
        self.additional_field8 = QLineEdit()
        self.additional_field8.setPlaceholderText("8")
        self.additional_field9 = QLineEdit()
        self.additional_field9.setPlaceholderText("9")
        self.additional_field10 = QLineEdit()
        self.additional_field10.setPlaceholderText("10")
        self.additional_field11 = QLineEdit()
        self.additional_field11.setPlaceholderText("11")
        self.additional_field12 = QLineEdit()
        self.additional_field12.setPlaceholderText("12")

        third_column_layout.addLayout(self.create_line_edit_field("Доп. поле 7", self.additional_field7))
        third_column_layout.addLayout(self.create_line_edit_field("Доп. поле 8", self.additional_field8))
        third_column_layout.addLayout(self.create_line_edit_field("Доп. поле 9", self.additional_field9))
        third_column_layout.addLayout(self.create_line_edit_field("Доп. поле 10", self.additional_field10))
        third_column_layout.addLayout(self.create_line_edit_field("Доп. поле 11", self.additional_field11))
        third_column_layout.addLayout(self.create_line_edit_field("Доп. поле 12", self.additional_field12))

        return third_column_layout

    def create_line_edit_field(self, label_text, line_edit):
        """Создает строку с Label и LineEdit"""
        h_layout_additional = QHBoxLayout()
        label_additional = QLabel(f"{label_text}: ")
        h_layout_additional.addWidget(label_additional)
        h_layout_additional.addWidget(line_edit)
        return h_layout_additional

    def update_truba(self):
        """Обновляет значения в таблице и расчеты"""
        # Обновление исходных данных
        self.source_data_table.setItem(0, 0, QTableWidgetItem(self.wide_line_edit.text()))
        self.source_data_table.setItem(0, 1, QTableWidgetItem(self.reservoir_temperature_line_edit.text()))
        self.source_data_table.setItem(0, 2, QTableWidgetItem(self.max_product_temperature_line_edit.text()))
        self.source_data_table.setItem(0, 3, QTableWidgetItem(self.min_environment_temperature_line_edit.text()))
        self.source_data_table.setItem(0, 4, QTableWidgetItem(self.max_environment_temperature_line_edit.text()))
        self.source_data_table.setItem(0, 5, QTableWidgetItem(self.material_combobox.currentText()))

        # Дополнительные поля
        self.source_data_table.setItem(0, 6, QTableWidgetItem(self.additional_field1.text()))
        self.source_data_table.setItem(0, 7, QTableWidgetItem(self.additional_field2.text()))
        self.source_data_table.setItem(0, 8, QTableWidgetItem(self.additional_field3.text()))
        self.source_data_table.setItem(0, 9, QTableWidgetItem(self.additional_field4.text()))
        self.source_data_table.setItem(0, 10, QTableWidgetItem(self.additional_field5.text()))
        self.source_data_table.setItem(0, 11, QTableWidgetItem(self.additional_field6.text()))
        self.source_data_table.setItem(0, 12, QTableWidgetItem(self.additional_field7.text()))
        self.source_data_table.setItem(0, 13, QTableWidgetItem(self.additional_field8.text()))
        self.source_data_table.setItem(0, 14, QTableWidgetItem(self.additional_field9.text()))
        self.source_data_table.setItem(0, 15, QTableWidgetItem(self.additional_field10.text()))
        self.source_data_table.setItem(0, 16, QTableWidgetItem(self.additional_field11.text()))
        self.source_data_table.setItem(0, 17, QTableWidgetItem(self.additional_field12.text()))

        self.update_result_table()

    def update_result_table(self):
        """Обновляет значения таблицы результатов расчета на основе данных из исходной таблицы"""
        for col in range(18):
            source_value = self.source_data_table.item(0, col).text()
            if source_value.isdigit():
                #result_value = str(Logic.calc(int(self.wide_line_edit.text()))) 
                result_value = str(int(source_value) + 777)
            else:
                result_value = source_value + " + 777"
            self.result_table.setItem(0, col, QTableWidgetItem(result_value))

    def show_result_table(self):
        """Отображает таблицу результатов расчета"""
        self.source_data_table.setVisible(False)
        self.result_table.setVisible(True)

    def show_source_data_table(self):
        """Отображает таблицу исходных данных"""
        self.result_table.setVisible(False)
        self.source_data_table.setVisible(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())
