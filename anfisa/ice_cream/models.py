from django.db import models

# Объявляем класс IceCream, наследник класса Model из пакета models
class IceCream(models.Model):
    # Тип: CharField (строка с ограничением длины)
    name = models.CharField(max_length=200)
    # Тип: TextField (текстовое поле)
    # используется для больших текстовых блоков
    description = models.TextField()
    # Тип: булева переменная, «да/нет»;
    # значение по умолчанию: True
    on_main = models.BooleanField(default=True)
