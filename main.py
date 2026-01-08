import flet as ft
from src.ui.main_window import main_view

# نقطة الدخول الرئيسية للبرنامج
def main(page: ft.Page):
    # استدعاء دالة بناء الواجهة
    main_view(page)

if __name__ == "__main__":
    ft.app(target=main)