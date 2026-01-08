import pytest
from src.models.student import Student

# اختبار لحساب المعدل
def test_calculate_average():
    student =Student(
        std_id="8574673", 
        name="Ali",
        email="a@a.com",
        phone="733223678",
        web_design=100,
        info_sec=100,
        comm_tech=100,
        data_struct=100,
        wireless_net=100,
        comm_skill=100
    )
    assert student.calculate_average() == 100.0
    
    
#اختبار حساب المعدل بالكسور
def test_calculate_avrage_float():
    student = Student(
        std_id="2875647",
        name="Sara",
        email="s@a.com",
        phone="773223679",
        web_design=85,
        info_sec=90,
        comm_tech=80,
        data_struct=75,
        wireless_net=95,
        comm_skill=70
)
    assert student.calculate_average() == 82.5

#رفض الدرجات السالبه
def test_validate_negative_grade():
    student = Student(
        std_id="8574690",
        name="Omar",
        email="o@a.com",
        phone="773223680",
        web_design=-10,
        info_sec=90,
        comm_tech=80,
        data_struct=75,
        wireless_net=95,
        comm_skill=70
    )
    with pytest.raises(ValueError, match="Mark -10 is out of valid range"):
        student.validate()
        
#رفض الدرجات التي تزيد عن 100
def test_validate_exceeding_grade():
    student = Student(
        std_id="8754357",
        name="Lina",
        email="l@a.com",
        phone="773223681",
        web_design=110,
        info_sec=90,
        comm_tech=80,
        data_struct=75,
        wireless_net=95,
        comm_skill=70
    )
    with pytest.raises(ValueError, match="Mark 110 is out of valid range"):
        student.validate()
        
#رفض البيانات الفارغه للرقم الجامعي والاسم
def test_validate_empty_fields():
    student = Student(
        std_id=None,
        name="",
        email="s@a.com",
        phone=773223682,
        web_design=85,
        info_sec=90,
        comm_tech=80,
        data_struct=75,
        wireless_net=95,
        comm_skill=70
    )
    with pytest.raises(ValueError):
        student.validate()
        
def test_validate_id_length():
    # طالب برقم جامعي قصير (3 خانات)
    student = Student(
        std_id="123", name="Short ID", email="e@e.com", phone="123456789",
        web_design=50, info_sec=50, comm_tech=50,
        data_struct=50, wireless_net=50, comm_skill=50
    )
    # نتوقع خطأ بسبب الطول
    with pytest.raises(ValueError):
        student.validate()
