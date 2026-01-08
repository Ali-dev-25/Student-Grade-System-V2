import flet as ft
from src.services.student_service import StudentService
from src.models.student import Student

def main_view(page: ft.Page):
    # 1. تهيئة طبقة الخدمة (للتعامل مع البيانات)
    service = StudentService()

    page.title = "Student Grade System V2"
    page.scroll = "auto"
    page.window.maximized = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.rtl = True  

    # --- حقول الإدخال ---
    tname = ft.TextField(label="اسم الطالب", icon=ft.Icons.PERSON, height=40 )
    tid = ft.TextField(label="الرقم الجامعي", icon=ft.Icons.BADGE, height= 40)
    tmail = ft.TextField(label="البريد الإلكتروني", icon=ft.Icons.EMAIL, height=40)
    tphone = ft.TextField(label="رقم الهاتف", icon=ft.Icons.PHONE, keyboard_type=ft.KeyboardType.PHONE, height=40)

#وضعت حقول الدرجات في قائمه لسهولة الوصول
    grade_fields = {
        "web": ft.TextField(label="Web Design",  col={"md":6}, keyboard_type=ft.KeyboardType.NUMBER),
        "info": ft.TextField(label="Info Security",  col={"md":6}, keyboard_type=ft.KeyboardType.NUMBER),
        "comm_tech": ft.TextField(label="Comm Tech",  col={"md":6}, keyboard_type=ft.KeyboardType.NUMBER),
        "data": ft.TextField(label="Data Struct",  col={"md":6}, keyboard_type=ft.KeyboardType.NUMBER),
        "wireless": ft.TextField(label="Wireless",  col={"md":6}, keyboard_type=ft.KeyboardType.NUMBER),
        "skills": ft.TextField(label="Comm Skills", col={"md":6}, keyboard_type=ft.KeyboardType.NUMBER),
    }

   # جدول عرض البيانات
    students_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nmae")),
            ft.DataColumn(ft.Text("Email")),
            ft.DataColumn(ft.Text("Web Design"), numeric=True),
            ft.DataColumn(ft.Text("Info Security"), numeric=True),
            ft.DataColumn(ft.Text("Communication Tech"), numeric=True),
            ft.DataColumn(ft.Text("Data Struct"), numeric=True),
            ft.DataColumn(ft.Text("Wireless-Network"), numeric=True),
            ft.DataColumn(ft.Text("Communication-Skills"), numeric=True),
            ft.DataColumn(ft.Text("المعدل"), numeric=True),
            ft.DataColumn(ft.Text("التقدير")),
        ],
        rows=[],
        border=ft.border.all(1, "grey"),
        vertical_lines=ft.border.BorderSide(1, "grey"),
        horizontal_lines=ft.border.BorderSide(1, "grey"),
    )

# --- العمليات (Logic) رسائل---
    
    def show_message(message, color):
        """استخدام Overlay لعرض Dialog"""
        
        # إنشاء Dialog
        dialog = ft.AlertDialog(
            title=ft.Text("تنبيه"),
            content=ft.Text(message),
            actions=[
                ft.TextButton("موافق", on_click=lambda e: close_dialog())
            ],
        )
        
        def close_dialog():
            """إغلاق الـ Dialog"""
            page.overlay.remove(dialog)  
            page.update()
        
        # إضافة Dialog إلى overlay الصفحة
        page.overlay.append(dialog)
        dialog.open = True
        page.update()
        
#-----------------------------
    def load_students():
        """جلب الطلاب من السيرفس وتحديث الجدول"""
        students = service.get_all_students()
        students_table.rows.clear()
        
        for std in students:
            avg = std.calculate_average()
            
            # تحديد التقدير ولونه
            if avg >= 90: grade_text, color = "ممتاز", "green"
            elif avg >= 80: grade_text, color = "جيد جداً", "blue"
            elif avg >= 65: grade_text, color = "جيد", "cyan"
            elif avg >= 50: grade_text, color = "مقبول", "orange"
            else: grade_text, color = "ضعيف", "red"

            students_table.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(std.std_id)),
                    ft.DataCell(ft.Text(std.name)),
                    ft.DataCell(ft.Text(std.email)),
                    # --- إضافة قيم المواد ---
                    ft.DataCell(ft.Text(str(std.web_design))),
                    ft.DataCell(ft.Text(str(std.info_sec))),
                    ft.DataCell(ft.Text(str(std.comm_tech))),
                    ft.DataCell(ft.Text(str(std.data_struct))),
                    ft.DataCell(ft.Text(str(std.wireless_net))),
                    ft.DataCell(ft.Text(str(std.comm_skill))),
                    # ------------------------
                    ft.DataCell(ft.Text(f"{avg:.2f}")),
                    ft.DataCell(ft.Container(
                        content=ft.Text(grade_text, color="white", weight="bold"),
                        bgcolor=color,
                        padding=5,
                        border_radius=5
                    )),
                ])
            )
        page.update()
    
#---------------------------------------
    def add_student_click(e):
        try:
            #  تجميع البيانات
            marks = {}
            for key, field in grade_fields.items():
                val = field.value.strip() if field.value else "0"
                
                #التحققمن الالقيم قبل التحويل
                if not val.isdigit():
                    show_message(f"Wrong! please, enter numbers in {field.label}")
                    print("[DEBUG] المدخلات ليست ارقاما")
                    return
                marks[key] = int(val)
            print("[DEBUG] 2. تم تجميع الدرجات بنجاح")

            # 2. إنشاء كائن الطالب (Model)
            new_student = Student(
                std_id=tid.value.strip(),
                name=tname.value.strip(),
                email=tmail.value.strip(),
                phone=tphone.value.strip(),
                web_design=marks["web"],
                info_sec=marks["info"],
                comm_tech=marks["comm_tech"],
                data_struct=marks["data"],
                wireless_net=marks["wireless"],
                comm_skill=marks["skills"]
            )

            #  إرسال الكائن لطبقة الخدمة (Service)
            success, message = service.add_student(new_student)

            if  success:
                show_message(message, "green")
                # تفريغ الحقول
                tid.value = ""
                tname.value = ""
                tmail.value = ""
                tphone.value = ""
                for field in grade_fields.values():
                    field.value = ""
                page.update()
                load_students() # تحديث الجدول
            else:
                show_message(message, "red")
                
        except ValueError as err:
            # هذا الخطأ يأتي من دالة validate في المودل أو من تحويل الأرقام
            show_message(f"Error in data: {str(err)}", "red")
        except Exception as ex:
            show_message(f" Wrong happened: {str(ex)}", "red")
            
#------------------------------------
    def export_excel_click(e):
        """Button export Excel"""
        success, msg= service.export_to_excel()
        color = "green" if success else "red"
        show_message(msg, color)
    
    #دوال التنقل
    def go_home(e=None):
        """عرض الصفحة الرئيسية (فورم الإضافة)"""
        page.clean()
        page.add(
            ft.Column([
                ft.Text("نظام إدارة درجات الطلاب ", size=30, weight="bold", color="blue"),
                ft.Divider(),
                
                ft.Text("البيانات الشخصية", size=20, weight="bold"),
                ft.ResponsiveRow([tname, tid, tmail, tphone]),
                
                ft.Divider(),
                ft.Text("الدرجات ", size=20, weight="bold"),
                ft.ResponsiveRow(list(grade_fields.values())),
                
                ft.Divider(),
                # أزرار التحكم
                ft.Row([
                    ft.ElevatedButton("حفظ الطالب", on_click=add_student_click, icon=ft.Icons.SAVE, bgcolor="blue", color="white", height=50),
                    ft.ElevatedButton("عرض القائمة", on_click=show_students_view, icon=ft.Icons.VIEW_LIST, bgcolor="green", color="white", height=50),
                    ft.ElevatedButton("Export to Excel", on_click=lambda e: export_excel_click(e), icon= ft.Icons.DOWNLOAD, bgcolor="orange", color="white", height=50)
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
                
            ], spacing=10)
        )
        page.update()

    def show_students_view(e):
        """عرض صفحة الجدول"""
        page.clean()
        load_students() # تحديث البيانات قبل العرض
        
        page.add(
            ft.Column([
                ft.Row([
                    ft.ElevatedButton("رجوع", icon=ft.Icons.ARROW_BACK, on_click=go_home, bgcolor="red", color="white"),
                    ft.Text("قائمة الطلاب المسجلين", size=25, weight="bold"),
                ], alignment=ft.MainAxisAlignment.START),
                
                ft.Divider(),
                
                # وضع الجدول داخل حاوية مع تفعيل Scroll
                ft.Card(
                ft.Container(
                    content=ft.Row([students_table], scroll=ft.ScrollMode.ALWAYS),
                    border=ft.border.all(1, "grey"),
                    border_radius=10,
                    padding=10,
                    expand=True # للتوسع
                ),
                color = "whits",
                elevation=5,
                margin=10
                )
            ])
        )
        page.update()

    # --- بداية التشغيل ---
    load_students()  # تحميل البيانات في الخلفية
    go_home()    

