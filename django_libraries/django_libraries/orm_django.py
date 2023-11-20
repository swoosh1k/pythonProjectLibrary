"""
Django ORM предоставляет множество методов для работы с данными. Рассмотрим некоторые из них:

all(): возвращает все записи из модели.

filter(**kwargs): возвращает записи, которые соответствуют указанным параметрам фильтрации.

exclude(**kwargs): возвращает записи, которые не соответствуют указанным параметрам фильтрации.

get(**kwargs): возвращает одну запись, которая соответствует указанным параметрам фильтрации.
 Если не найдено ни одной записи или найдено более одной записи, то возникает исключение.
create(**kwargs): создает и сохраняет новую запись в базе данных.

update(**kwargs): обновляет записи, которые соответствуют указанным параметрам фильтрации.

delete(): удаляет записи, которые соответствуют указанным параметрам фильтрации.

Это только некоторые из методов, которые можно использовать в Django ORM.
 Кроме того, существуют методы для выполнения агрегирующих запросов, связанных запросов, обратных связей и т.д.



Конструкция filter() в Django ORM используется для выборки объектов из базы данных,
 которые соответствуют заданным условиям.

Пример:

Предположим, что у нас есть модель Product с полями name, price и in_stock.
 Чтобы выбрать все продукты, которые в наличии и стоят менее 1000 рублей,
  можно использовать следующий код:

from myapp.models import Product
products = Product.objects.filter(in_stock=True, price__lt=1000)

Здесь filter() применяется к менеджеру объектов модели Product,
и в качестве аргументов передаются условия выборки.
Аргументы соединяются операцией "И" (AND). В примере мы передаем два условия: in_stock=True и price__lt=1000.
Второе условие использует оператор __lt (less than),
 который указывает на выборку объектов с ценой меньше указанного значения.

Результат выполнения этого кода будет представлять собой QuerySet (множество объектов),
содержащее все продукты, удовлетворяющие заданным условиям.


Метод exclude используется в Django ORM для получения queryset, исключающего объекты, удовлетворяющие определенным условиям.

from myapp.models import MyModel
# Получаем queryset, исключающий объекты, у которых поле field1 равно 'value1'
queryset = MyModel.objects.exclude(field1='value1')

В этом примере мы получаем queryset из модели MyModel,
и исключаем все объекты, у которых поле field1 равно 'value1'.
Этот метод можно использовать в сочетании с другими методами,
такими как filter, order_by, annotate и т.д., для получения более сложных запросов к базе данных.


Метод get используется для получения единственного объекта из базы данных,
удовлетворяющего определенным критериям.
Если несколько объектов соответствуют запросу, то будет вызвано исключение
MultipleObjectsReturned. Если ни один объект не соответствует запросу, то будет вызвано исключение DoesNotExist.

Пример использования метода get:
from myapp.models import MyModel
# Получить единственный объект MyModel, у которого поле 'my_field' равно 'my_value'
my_object = MyModel.objects.get(my_field='my_value')

В данном примере мы получаем объект модели MyModel, у которого значение поля my_field равно 'my_value'.
Если такой объект существует, то он будет присвоен переменной my_object.
Если же объекта с таким значением поля не существует, то будет вызвано исключение MyModel.DoesNotExist.
Если объектов с таким значением поля несколько, то будет вызвано исключение MyModel.MultipleObjectsReturned.




Метод create используется для создания нового объекта в базе данных и сохранения его в одной операции. Пример:

from myapp.models import Person

# Создаем новый объект Person и сохраняем его в базе данных
new_person = Person.objects.create(
    first_name='John',
    last_name='Doe',
    age=30,
)
В этом примере мы создаем новый объект Person и сохраняем его в базе данных в одной операции с помощью метода create.
Мы передаем значения для полей first_name, last_name и age в качестве аргументов метода.
Если объект был успешно создан и сохранен, метод create вернет этот объект.




В Django агрегирующие запросы используются для анализа данных и получения сводной информации из базы данных.
Они позволяют производить различные вычисления (например, подсчет суммы, количества, среднего значения)
по заданным критериям и фильтрам. В отличие от обычных запросов, которые возвращают объекты модели,
агрегирующие запросы возвращают единственное значение.

Примеры агрегирующих запросов в Django:

count() - возвращает количество объектов, удовлетворяющих заданным критериям;
sum() - возвращает сумму значений заданного поля;
avg() - возвращает среднее значение заданного поля;
min() - возвращает минимальное значение заданного поля;
max() - возвращает максимальное значение заданного поля.

Например, следующий код возвращает сумму всех полей price у объектов модели Product, у которых category равна electronics:

from django.db.models import Sum
from myapp.models import Product

total_price = Product.objects.filter(category='electronics').aggregate(Sum('price'))['price__sum']
В данном примере мы использовали метод aggregate(),
который позволяет производить агрегирующие запросы и получать единственное значение.


"""