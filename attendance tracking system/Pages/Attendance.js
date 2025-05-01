
import { useState, useEffect } from 'react';
import { collection, query, where, getDocs, addDoc, serverTimestamp } from 'firebase/firestore';
import { db, auth } from '../firebase';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';

const Attendance = () => {
  const [date, setDate] = useState(new Date());
  const [students, setStudents] = useState([]);
  const [attendance, setAttendance] = useState({});

  useEffect(() => {
    const fetchStudents = async () => {
      const q = query(collection(db, 'students'), 
        where('userId', '==', auth.currentUser.uid));
      const snapshot = await getDocs(q);
      setStudents(snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() })));
    };
    fetchStudents();
  }, []);

  const handleStatusChange = (studentId, status) => {
    setAttendance(prev => ({
      ...prev,
      [studentId]: status
    }));
  };

  const submitAttendance = async () => {
    const attendanceData = {
      date: date,
      records: Object.keys(attendance).map(studentId => ({
        studentId,
        status: attendance[studentId],
        timestamp: serverTimestamp()
      })),
      userId: auth.currentUser.uid
    };

    await addDoc(collection(db, 'attendance'), attendanceData);
    alert('Attendance saved successfully!');
  };

  return (
    <div className="attendance-container">
      <h2>Mark Attendance</h2>
      <DatePicker selected={date} onChange={date => setDate(date)} />
      
      <div className="attendance-list">
        {students.map(student => (
          <div key={student.id} className="student-card">
            <span>{student.name}</span>
            <div className="status-buttons">
              <button 
                className={attendance[student.id] === 'present' ? 'active' : ''}
                onClick={() => handleStatusChange(student.id, 'present')}
              >
                Present
              </button>
              <button 
                className={attendance[student.id] === 'absent' ? 'active' : ''}
                onClick={() => handleStatusChange(student.id, 'absent')}
              >
                Absent
              </button>
            </div>
          </div>
        ))}
      </div>
      
      <button onClick={submitAttendance} className="submit-btn">
        Save Attendance
      </button>
    </div>
  );
};

export default Attendance;