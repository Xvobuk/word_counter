Для работы файла должен быть установлен Python.

Установите билиотеку pandas: 

*pip install pandas*

Скачайте вашу переписку в Телеграме через экспорт выбрав метод сохранения данных в виде JSON-объекта, убрав все галочки. То есть скачать надо безф отографий, голосовых сообщений и так далее. Просто текст.

Файл result.json поместите в одну папку с файлом программы.

Запустите программу.

Вы получите на вывод два файла: один выдаёт топ-100 не отчищенных от местоимений, междометий и множества союзов результат, а второй уже выдаст статистику поинтереснее.

Адаптировано только для русского языка на данный момент.

____________________________________________

To run the file, Python must be installed.

Install the pandas library:

*pip install pandas*

Download your Telegram chat by exporting the data in the form of a JSON object, ensuring that all checkboxes are unchecked. This means downloading only text without photos, voice messages, and so on.

Place the result.json file in the same folder as the program file.

Run the program.

You will receive two output files: one will provide the top-100 results without filtering out pronouns, interjections, and many conjunctions, while the second will give a more interesting statistic.

At this point works only with Russian language.
