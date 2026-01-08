import pytest
from src.services.student_service import StudentService
from src.database.db_manager import DatabaseManager
from src.models.student import Student

# --- التجهيز (Fixture) ---
@pytest.fixture
def service():
    # نستخدم :memory: لإنشاء قاعدة بيانات مؤقتة وسريعة
    temp_db_manager = DatabaseManager(":memory:")
    svc = StudentService()
    svc.db = temp_db_manager 
    return svc

# --- اختبار 6: إضافة طالب صحيح ---
def test_add_valid_student(service):
    # ننشئ كائن الطالب
    student = Student(
        std_id="7643866", name="Ali", email="test@test.com", phone="777777777",
        web_design=90, info_sec=90, comm_tech=90,
        data_struct=90, wireless_net=90, comm_skill=90
    )
    
    # نرسل الكائن بالكامل للدالة
    success, msg = service.add_student(student)
    
    if not success:
        print(f"\nDEBUG ERROR: {msg}")

    assert success is True
    assert msg == "Student added successfully"

# --- اختبار 7: منع التكرار ---
def test_add_duplicate_student(service):
    std1 = Student("9847894", "Ahmed", "a@a.com", "738745673", 50, 50, 50, 50, 50, 50)
    service.add_student(std1)
    
    std2 = Student("9847894", "Salim", "b@b.com", "794673462", 60, 60, 60, 60, 60, 60)
    
    success, msg = service.add_student(std2)
    
    # نتوقع الفشل لأن الرقم مكرر
    assert success is False 
    assert "Student ID already exists" in msg

# --- اختبار 8: استرجاع البيانات ---
def test_get_all_students(service):
    service.add_student(Student("9834563", "Aslam", "a@a.com", "763826646", 50, 50, 50, 50, 50, 50))
    service.add_student(Student("8943987", "Kmal", "b@b.com", "736276662", 50, 50, 50, 50, 50, 50))
    
    students = service.get_all_students()
    assert len(students) == 2

# --- اختبار 9: دقة البيانات ---
def test_data_integrity(service):
    original_std = Student("7836452", "Yaseen", "x@x.com", "788574363", 88, 77, 66, 55, 44, 33)
    service.add_student(original_std)
    
    retrieved_std = service.get_all_students()[0]
    assert retrieved_std.name == "Yaseen"
    assert retrieved_std.web_design == 88

# --- اختبار 10: الدرجات الحدودية ---
def test_add_boundary_grades(service):
    std_zero = Student("8748672", "Osama", "z@z.com", "789743466", 0, 0, 0, 0, 0, 0)
    success1, msg1 = service.add_student(std_zero)
    if not success1: print(f"\nDEBUG ZERO: {msg1}")
    assert success1 is True
    
    std_full = Student("9748797", "yaser", "f@f.com", "786327569", 100, 100, 100, 100, 100, 100)
    success2, msg2 = service.add_student(std_full)
    if not success2: print(f"\nDEBUG FULL: {msg2}")
    assert success2 is True