import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import numpy as np


def diagnose_disease(symptoms, factors):
    disease_model = {
        "Альцгеймер": "Потеря памяти, трудности с речью, изменения в поведении, дезориентация, проблемы с выполнением привычных задач".lower().split(', '),
        "Паркинсон": "Тремор, ригидность, замедленность движений, нарушения равновесия, изменения в почерке".lower().split(', '),
        "Рассеянный склероз": "Усталость, нарушения координации, онемение или покалывание, проблемы со зрением, мышечная слабость".lower().split(', '),
        "Инсульт": "Внезапная слабость или онемение одной стороны тела, затруднения в речи, потеря равновесия, головная боль".lower().split(', '),
        "Эпилепсия": "Судороги, потеря сознания, ауры, изменения в восприятии, временная потеря памяти".lower().split(', '),
        "Мигрень": "Сильная головная боль, тошнота, чувствительность к свету и звуку, зрительные нарушения".lower().split(', '),
        "Невралгия тройничного нерва": "Резкая боль в области лица, спонтанные приступы боли, триггерные точки".lower().split(', '),
        "Нейропатия": "Онемение, покалывание, жжение, мышечная слабость, боли".lower().split(', '),
        "Хорея Гентингтона": "Неконтролируемые движения, изменения в настроении, когнитивные нарушения, трудности с речью".lower().split(', '),
        "Болезнь Лу Герига": "Мышечная слабость, трудности с речью и глотанием, судороги, потеря мышечной массы".lower().split(', '),
        "Деменция с тельцами Леви": "Колебания внимания и сознания, визуальные галлюцинации, нарушения движения, проблемы с памятью".lower().split(', '),
        "Неврит": "Боль, онемение, слабость в области иннервации нерва, нарушения чувствительности".lower().split(', '),
        "Синдром Туретта": "Тики (моторные и вокальные), импульсивное поведение, трудности с концентрацией".lower().split(', '),
        "Фибромиалгия": "Хроническая боль в мышцах и суставах, усталость, нарушения сна, чувствительность к боли".lower().split(', '),
        "Спинальная мышечная атрофия": "Мышечная слабость, трудности с движением, атрофия мышц, проблемы с дыханием".lower().split(', '),
        "Миастения гравис": "Мышечная слабость, утомляемость при физической активности, затруднения с глотанием и речью".lower().split(', '),
        "Нейробластома": "Опухолевые образования, боли в животе или спине, усталость, потеря веса".lower().split(', '),
        "Синдром беспокойных ног": "Непреодолимое желание двигать ногами, дискомфорт в ногах, ухудшение симптомов ночью".lower().split(', '),
        "Травматическая энцефалопатия": "Изменения в настроении и поведении, проблемы с памятью и вниманием, головные боли".lower().split(', '),
        "Краниоцеребральная травма": "Головные боли, потеря сознания, спутанность сознания, тошнота".lower().split(', '),
        "Нейросифилис": "Головные боли, изменения в поведении и настроении, проблемы с памятью и координацией".lower().split(', '),
        "Менингит": "Высокая температура, головная боль, ригидность шеи, чувствительность к свету".lower().split(', '),
        "Энцефалит": "Головная боль, лихорадка, спутанность сознания, судороги".lower().split(', '),
        "Нейропатия, вызванная диабетом": "Онемение и покалывание в конечностях, боли, снижение чувствительности".lower().split(', '),
        "Церебральный паралич": "Нарушения движения и координации, мышечная спастичность или слабость".lower().split(', '),
        "Гидроцефалия": "Увеличение головы (у детей), головные боли, проблемы с координацией и равновесием".lower().split(', '),
        "Атаксия": "Нарушения координации движений, неустойчивость при ходьбе и стоянии".lower().split(', '),
        "Синдром Кушинга": "Изменения настроения и поведения, усталость, мышечная слабость".lower().split(', '),
        "Синдром Фридрейха": "Прогрессирующая атаксическая ходьба, сердечно-сосудистые проблемы, диабет".lower().split(', '),
        "Периферическая нейропатия": "Онемение и покалывание в конечностях, мышечная слабость".lower().split(', '),
        "Нейросклероз": "Прогрессирующая потеря функций нервной системы, изменения в поведении и настроении".lower().split(', '),
        "Болезнь Кройцфельдта-Якоба": "Быстрое ухудшение когнитивных функций, нарушения движений, поведенческие изменения".lower().split(', '),
        "Псевдопаркинсонизм": "Тремор, ригидность мышц, замедленность движений без истинного паркинсонизма".lower().split(', '),
        "Синдром Дауна": "Задержка развития речи и двигательных навыков, когнитивные нарушения".lower().split(', '),
        "Синдром Вильямса": "Проблемы с обучением и памятью, социальная открытость и дружелюбие".lower().split(', '),
        "Болезнь Альцгеймера в молодом возрасте": "Ранняя потеря памяти и когнитивных функций, изменения в поведении".lower().split(', '),
        "Болезнь Вильсона": "Неврологические расстройства (тремор), изменения поведения и настроения".lower().split(', '),
        "Синдром Кернига": "Ригидность шеи и боли при сгибании головы вперед".lower().split(', '),
        "Боковой амиотрофический склероз (БАС)": "Мышечная слабость и атрофия, трудности с речью и глотанием".lower().split(', '),
        "Аутизм (неврологические аспекты)": "Трудности в общении и взаимодействии с окружающими, ограниченные интересы и повторяющиеся действия".lower().split(', ')
    }
    secondary_factors_model ={
        "Альцгеймер": "1;1;1;1;1".split(';'),
        "Паркинсон": "1;1;1;1;1".split(';'),
        "Рассеянный склероз": "1;1;1;1;1".split(';'),
        "Инсульт": "1;1;0;1;1".split(';'),
        "Эпилепсия": "1;1;1;1;0".split(';'),
        "Мигрень": "1;0;1;1;1".split(';'),
        "Невралгия тройничного нерва": "1;1;1;1;0".split(';'),
        "Нейропатия": "0;1;1;1;0".split(';'),
        "Хорея Гентингтона": "1;1;0;0;0".split(';'),
        "Болезнь Лу Герига": "1;1;1;0;1".split(';'),
        "Деменция с тельцами Леви": "1;1;1;0;0".split(';'),
        "Неврит": "0;0;0;1;0".split(';'),
        "Синдром Туретта": "1;1;1;0;0".split(';'),
        "Фибромиалгия": "1;0;1;1;0".split(';'),
        "Спинальная мышечная атрофия": "1;1;0;0;0".split(';'),
        "Миастения гравис": "0;1;1;1;0".split(';'),
        "Нейробластома": "1;1;0;0;1".split(';'),
        "Синдром беспокойных ног": "0;1;1;0;0".split(';'),
        "Травматическая энцефалопатия": "0;0;1;0;0".split(';'),
        "Краниоцеребральная травма": "0;0;1;0;0".split(';'),
        "Нейросифилис": "0;0;0;1;0".split(';'),
        "Менингит": "0;0;0;1;0".split(';'),
        "Энцефалит": "0;0;0;1;0".split(';'),
        "Нейропатия, вызванная диабетом": "0;1;1;0;0".split(';'),
        "Церебральный паралич": "0;1;0;0;0".split(';'),
        "Гидроцефалия": "0;1;0;0;0".split(';'),
        "Атаксия": "1;1;0;0;0".split(';'),
        "Синдром Кушинга": "0;0;0;1;0".split(';'),
        "Синдром Фридрейха": "1;1;0;0;0".split(';'),
        "Периферическая нейропатия": "0;1;0;1;0".split(';'),
        "Нейросклероз": "1;1;0;0;0".split(';'),
        "Болезнь Кройцфельдта-Якоба": "1;0;0;0;1".split(';'),
        "Псевдопаркинсонизм": "0;1;0;1;0".split(';'),
        "Синдром Дауна": "0;1;1;0;0".split(';'),
        "Синдром Вильямса": "1;0;0;0;0".split(';'),
        "Болезнь Альцгеймера в молодом возрасте": "1;1;0;0;1".split(';'),
        "Болезнь Вильсона": "1;1;0;1;0".split(';'),
        "Синдром Кернига": "0;1;0;1;1".split(';'),
        "Боковой амиотрофический склероз (БАС)": "1;1;1;0;1".split(';'),
        "Аутизм (неврологические аспекты)": "1;1;1;1;0".split(';'),
    }
    scores = {disease: 0 for disease in disease_model}

    for disease, model_symptoms in disease_model.items():
        scores[disease] = sum(symptom in symptoms for symptom in model_symptoms)

    for disease, model_factors in secondary_factors_model.items():
        scores[disease] += sum(factor in factors for factor in model_factors) * 0.4
    a = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    filtered_diseases = {disease: score for disease, score in scores.items() if score >= 1.8}
    sorted_diseases = sorted(filtered_diseases.items(), key=lambda x: x[1], reverse=True)
    return ", ".join([disease for disease, _ in sorted_diseases]) if sorted_diseases else "Неизвестное заболевание"


class DiagnosisApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Диагностика неврологических заболеваний')

        self.symptom_label = QLabel('Введите симптомы через запятую:')
        self.symptom_input = QLineEdit()

        self.factor_label = QLabel('Введите второстепенные факторы через ";" (если важно = 1, если не важно = 0) (Семейная история (наследственность), Возраст, Пол, Психическое здоровье, Экологические или профессиональные факторы:')
        self.factor_input = QLineEdit()

        self.diagnose_button = QPushButton('Диагностировать')
        self.diagnose_button.clicked.connect(self.handle_diagnosis)

        layout = QVBoxLayout()
        layout.addWidget(self.symptom_label)
        layout.addWidget(self.symptom_input)
        layout.addWidget(self.factor_label)
        layout.addWidget(self.factor_input)
        layout.addWidget(self.diagnose_button)

        self.setLayout(layout)

    def handle_diagnosis(self):
        try:
            # Считывание симптомов
            symptoms = [s.strip().lower() for s in self.symptom_input.text().split(',')]

            # Считывание факторов
            factors_input = [f.strip() for f in self.factor_input.text().split(';')]
            factors = {f.split('=')[0].strip(): f.split('=')[1].strip() for f in factors_input if '=' in f}

            # Диагностика
            diagnosis = diagnose_disease(symptoms, factors)
            QMessageBox.information(self, 'Результат диагностики', f'Вероятные заболевания: {diagnosis}')

        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'Произошла ошибка: {str(e)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DiagnosisApp()
    ex.show()
    sys.exit(app.exec())