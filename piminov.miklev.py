import flet as ft

def main(page: ft.Page):
    click = 0

    def button_click(e):# счет нажатий
        nonlocal click
        click += 1
        label.value = f"Количество нажатий: {click}"
        page.update()

    def reset_count(e):# счетчик
        nonlocal click
        click = 0
        label.value = "Количество нажатий: 0"
        page.update()

    def save_file(e):# сохранение
        with open("click_count.txt", "w") as file:
            file.write(str(click))
        label.value = "Счетчик сохранён в файл click_count!"
        page.update()

    label = ft.Text("Количество кликов: 0")
    #кнопки
    click_button = ft.ElevatedButton("Нажми на меня!", on_click=button_click)
    reset_button = ft.ElevatedButton("Обнулить счет", on_click=reset_count)
    save_button = ft.ElevatedButton("Сохранить счетчик", on_click=save_file)

    page.add(label, click_button, reset_button, save_button)

ft.app(target=main)