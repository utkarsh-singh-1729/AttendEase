
import { useState, useEffect } from 'react';
import { collection, query, where, getDocs } from 'firebase/firestore';
import { db, auth } from '../firebase';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js/auto';

const Reports = () => {
  const [startDate, setStartDate] = useState(new Date());
  const [endDate, setEndDate] = useState(new Date());
  const [reportData, setReportData] = useState(null);

  const generateReport = async () => {
    const q = query(collection(db, 'attendance'),
      where('userId', '==', auth.currentUser.uid),
      where('date', '>=', startDate),
      where('date', '<=', endDate)
    );

    const snapshot = await getDocs(q);
    const data = snapshot.docs.map(doc => doc.data());
    
    // Process data for chart
    const chartData = {
      labels: ['Present', 'Absent'],
      datasets: [{
        label: 'Attendance Summary',
        data: [
          data.flatMap(d => d.records).filter(r => r.status === 'present').length,
          data.flatMap(d => d.records).filter(r => r.status === 'absent').length
        ],
        backgroundColor: ['#4CAF50', '#F44336']
      }]
    };

    setReportData(chartData);
  };

  return (
    <div className="reports-container">
      <h2>Attendance Reports</h2>
      
      <div className="date-range">
        <DatePicker
          selected={startDate}
          onChange={date => setStartDate(date)}
          selectsStart
          startDate={startDate}
          endDate={endDate}
        />
        <DatePicker
          selected={endDate}
          onChange={date => setEndDate(date)}
          selectsEnd
          startDate={startDate}
          endDate={endDate}
          minDate={startDate}
        />
        <button onClick={generateReport}>Generate Report</button>
      </div>

      {reportData && (
        <div className="chart-container">
          <Bar data={reportData} />
        </div>
      )}
    </div>
  );
};

export default Reports;