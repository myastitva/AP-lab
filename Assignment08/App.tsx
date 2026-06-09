import { useState } from "react";
import "./dashboard.css";

export default function CourseEnrollmentDashboard() {

  const [studentsMap, setStudentsMap] = useState(new Map());
  const [filterCourse, setFilterCourse] = useState("");

  const addStudent = () => {

    const id = Date.now();

    const newStudent = {
      id,
      name: `Student ${id}`,
      enrolledCourses: new Set(["React", "Data Structures"]),
      gpa: Number((Math.random() * 4).toFixed(2))
    };

    const updated = new Map(studentsMap);
    updated.set(id, newStudent);

    setStudentsMap(updated);
  };

  const removeStudent = (id) => {

    const updated = new Map(studentsMap);
    updated.delete(id);

    setStudentsMap(updated);
  };

  const studentsArray = [...studentsMap.values()];

  const sortedStudents = [...studentsArray].sort(
    (a, b) => b.gpa - a.gpa
  );

  const filteredStudents = filterCourse
    ? sortedStudents.filter(student =>
        student.enrolledCourses.has(filterCourse)
      )
    : sortedStudents;

  const uniqueCourses = studentsArray.reduce((courseSet, student) => {

    student.enrolledCourses.forEach(course =>
      courseSet.add(course)
    );

    return courseSet;

  }, new Set());

  return (
    <div className="dashboard">

      <h1>Course Enrollment Dashboard</h1>

      <div className="controls">

        <button className="addBtn" onClick={addStudent}>
          Add Student
        </button>

        <input
          className="filterInput"
          placeholder="Filter by course"
          value={filterCourse}
          onChange={(e) => setFilterCourse(e.target.value)}
        />

      </div>

      <div className="coursesBox">

        <h3>All Unique Courses</h3>

        <div className="courseList">
          {[...uniqueCourses].map((course, index) => (
            <span key={index} className="courseTag">
              {course}
            </span>
          ))}
        </div>

      </div>

      <h2>Students (Sorted by GPA)</h2>

      <div className="studentGrid">

        {filteredStudents.map(student => (

          <div className="studentCard" key={student.id}>

            <h3>{student.name}</h3>

            <p className="gpa">GPA: {student.gpa}</p>

            <div className="courseList">

              {[...student.enrolledCourses].map((course, i) => (
                <span key={i} className="courseTag">
                  {course}
                </span>
              ))}

            </div>

            <button
              className="removeBtn"
              onClick={() => removeStudent(student.id)}
            >
              Remove
            </button>

          </div>

        ))}

      </div>

    </div>
  );
}