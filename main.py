#Импорт
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

#Результаты формы
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # получаем выбранное изображение
        selected_image = request.form.get('image-selector')
        # Задание №2.Получаем текст
        text1 = request.form.get('textTop')
        text2 = request.form.get('textBottom')

        # Задание №3. Получаем расположение текста
        x1 = request.form.get('textTop_y')
        x2 = request.form.get('textBottom_y')

        # Задание №3. Получаем цвет текста
        color = request.form.get('color-selector')

        return render_template('index.html', 
                               # отображаем выбранное изображение
                               selected_image=selected_image, 
                               # Задание №2. Отображаем текст
                               text1 = text1,
                               text2 = text2,
                               # Задание №3. Отображаем цвет 
                               x1 = x1,
                               x2 = x2,
                               #Задание №3. Отоброжаем расположение текста
                               color = color,
                               )
    else:
        # отображаем первое изображение по умолчанию
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
