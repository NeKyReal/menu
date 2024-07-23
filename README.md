
---

Этот проект представляет собой Django-приложение для создания и управления древовидным меню. Меню создается и редактируется через стандартную админку Django и отображается на страницах с помощью template tag. Поддерживается несколько меню на одной странице, определяемых по названию.

---

### Использование

1. Создайте меню и пункты меню в админке Django.
2. Вставьте ```template tag``` для отображения меню в нужное место вашего шаблона:
``` jinja
{% load custom_menu %}
{% draw_menu 'main_menu' %}
```

---
