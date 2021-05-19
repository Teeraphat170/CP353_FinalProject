# CP353_FinalProject<br/>
สมาชิกภายในกลุ่ม<br>
1.นายพฤธา พึ่งชื่น			รหัสนิสิต 62102010162<br>
2.นายธีรภัทร เชยชม			รหัสนิสิต 62102010170<br>
3.นายวิชญนนท์ พูนเพิ่มความดี	รหัสนิสิต 62102010186<br>

ขั้นตอนการรันโปรเจค<br>
1.โหลดไฟล์จาก https://drive.google.com/file/d/1OG9wpjhLEgPLLd3-xGFD6OEss8DPVtaY/view?usp=sharing<br>
&nbsp;&nbsp;&nbsp;แล้วเอาไปวางไว้ที่ CP353_FinalProject\flask-project\ml-model\variables  
&nbsp;&nbsp;&nbsp;จากการที่ไฟล์มีขนาดใหญ่เกินไปจึงทำให้ไม่สามารถอัพโหลดลง github ได้<br>
2.เปิดโฟลเดอร์ flask-project ด้วย Visual Studio Code<br>
3.รันโปรเจคผ่าน app.py<br>
4.การเพิ่ม,อัพเดต,ลบ ข้อมูลจะต้องทำใน Swagger UI, Postman เท่านั้น<br>
5.ตัวอย่างการใช้ Postman <br>
&nbsp;&nbsp;&nbsp;Get : http://localhost:5000/Fruit?name=Banana<br>
&nbsp;&nbsp;&nbsp;Post : {"color" : "yellow","name" : "lemon","types" : "Citrus","pic" : "static/pic/lemon.jpg"}<br>
&nbsp;&nbsp;&nbsp;Put : {"key" : "lemon","color" : "red","name" : "lemon","types" : "Citrus","pic" : "static/pic/lemon.jpg"}<br>
&nbsp;&nbsp;&nbsp;Delete : http://localhost:5000/Fruit/delete/lemon<br>

Google drive : https://drive.google.com/file/d/1jNImroXJdWp6XySp9StYXzSLnZCxQemD/view?usp=sharing
