import { useState, useEffect } from 'react';
import { collection, addDoc, query, where, onSnapshot } from 'firebase/firestore';
import { db, auth } from '../firebase';

const Students = () => {
  const [students, setStudents] = useState([]);
  const [newStudent, setNewStudent] = useState({
    name: '',
    rollNumber: '',
    className: ''
  });

  useEffect(() => {
    const q = query(collection(db, 'students'), 
      where('userId', '==', auth.currentUser.uid));
    const unsubscribe = onSnapshot(q, (snapshot) => {
      setStudents(snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() })));
    });
    return unsubscribe;
  }, []);

  const addStudent = async (e) => {
    e.preventDefault();
    await addDoc(collection(db, 'students'), {
      ...newStudent,
      userId: auth.currentUser.uid
    });
    setNewStudent({ name: '', rollNumber: '', className: '' });
  };

  return (
    <div className="students-container">
      <h2>Manage Students</h2>
      
      <form onSubmit={addStudent} className="student-form">
        <input
          type="text"
          placeholder="Student Name"
          value={newStudent.name}
          onChange={e => setNewStudent({...newStudent, name: e.target.value})}
          required
        />
        <input
          type="text"
          placeholder="Roll Number"
          value={newStudent.rollNumber}
          onChange={e => setNewStudent({...newStudent, rollNumber: e.target.value})}
          required
        />
        <input
          type="text"
          placeholder="Class"
          value={newStudent.className}
          onChange={e => setNewStudent({...newStudent, className: e.target.value})}
          required
        />
        <button type="submit">Add Student</button>
      </form>

      <div className="student-list">
        {students.map(student => (
          <div key={student.id} className="student-item">
            <span>{student.name}</span>
            <span>Roll: {student.rollNumber}</span>
            <span>Class: {student.className}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Students;