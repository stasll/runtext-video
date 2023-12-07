import cv2
import numpy as np

def running_text(text):
    # Создаем пустое изображение
    image = np.zeros((100, 100, 3), dtype=np.uint8)

    # Устанавливаем начальные координаты для текста
    x = 100
    y = 50

    # Устанавливаем параметры шрифта
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_color = (255, 255, 255)
    line_type = 2

    # Создаем видео
    video = cv2.VideoWriter('/content/testproject/polls/running_text.mp4', cv2.VideoWriter_fourcc(*'XVID'), 30, (100, 100))

    # Добавляем текст на каждом кадре
    for i in range(90):
        image = np.zeros((100, 100, 3), dtype=np.uint8)  # Очищаем изображение
        cv2.putText(image, text, (x, y), font, font_scale, font_color, line_type)  # Добавляем текст
        video.write(image)  # Записываем кадр в видео

        # Изменяем скорость движения в зависимости от длины текста
        if len(text) <= 5:
            x -= 1
        elif 5 < len(text) <= 7:
            x-=2
        elif 7 < len(text) <= 10:
            x-=3
        elif 10 < len(text) <= 13:
            x -= 4
        else:
            x-=5

    video.release()
    return video
