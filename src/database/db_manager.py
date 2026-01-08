import sqlite3
from contextlib import contextmanager

DB_NAME = "students_v2.db"

class DatabaseManager:
    def __init__(self, db_name=DB_NAME):
        #متغيرلتخزين الاختبار الداذم في حالة الاختبار
        self.db_name = db_name
        self._memory_conn= None
        self.init_tables()

    @contextmanager
    def get_connection(self):
       """Context Manager لإدارة الاتصال"""
       
       # --- حالة خاصة للاختبارات (قاعدة بيانات الذاكرة) ---
       if self.db_name == ":memory:":
           if self._memory_conn is None:
               self._memory_conn = sqlite3.connect(":memory:")
           yield self._memory_conn
           
       # --- الحالة الطبيعية (قاعدة بيانات ملف) ---
       else:
           conn = sqlite3.connect(self.db_name)
           try:
               yield conn
           finally:
               conn.close() 

    def init_tables(self):
        """إنشاء الجداول مع القيود (Constraints)"""
        schema = """
        CREATE TABLE IF NOT EXISTS students (
            std_id TEXT PRIMARY KEY CHECK(length(std_id)=7),  -- منع تكرار الرقم الجامعي
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT CHECK(length(phone) = 9),
            web_design INTEGER CHECK(web_design BETWEEN 0 AND 100), -- قيد: الدرجة 0-100
            info_sec INTEGER CHECK(info_sec BETWEEN 0 AND 100),
            comm_tech INTEGER CHECK(comm_tech BETWEEN 0 AND 100),
            data_struct INTEGER CHECK(data_struct BETWEEN 0 AND 100),
            wireless_net INTEGER CHECK(wireless_net BETWEEN 0 AND 100),
            comm_skill INTEGER CHECK(comm_skill BETWEEN 0 AND 100)
        );
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(schema)
                conn.commit()
        except Exception as e:
            print(f"Error creating tables: {e}")