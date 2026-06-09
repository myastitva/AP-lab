import java.util.*;
import java.util.stream.Collectors;
class Student {
private int id;
private String name;
private List<String> courses;
private Map<String, Integer> scores;
public Student(int id, String name, List<String> courses, Map<String, Integer> scores) {
this.id = id;
this.name = name;
this.courses = new ArrayList<>(courses); // Defensive copy
this.scores = new HashMap<>(scores); // Defensive copy
}
public int getId() { return id; }
public String getName() { return name; }
public List<String> getCourses() { return courses; }
public Map<String, Integer> getScores() { return scores; }
// Helper to calculate average score for this student
public double getAverageScore() {
if (courses.isEmpty()) return 0.0;
// Using Stream to sum scores, handling missing scores with getOrDefault
int sum = courses.stream()
.mapToInt(course -> scores.getOrDefault(course, 0))
.sum();
return (double) sum / courses.size();
}
@Override
public String toString() {
return String.format("ID: %d | Name: %-10s | Avg: %.2f", id, name, getAverageScore());
}
}
public class StudentPerformanceAnalyzer {
// 1. Get Top N Students sorted by average score (descending)


public static List<Student> getTopNStudents(List<Student> students, int n) {
return students.stream()
// using Comparator to sort by average score descending
.sorted(Comparator.comparingDouble(Student::getAverageScore).reversed())
.limit(n)
.collect(Collectors.toList());
}
// 2. Get Average Score Per Course
public static Map<String, Double> getAverageScorePerCourse(List<Student> students) {
// FlatMap to create a stream of Map.Entry<Course, Score>
// We ensure we only consider courses the student is actually enrolled in (from their list)
// and safely get the score using getOrDefault
return students.stream()
.flatMap(student -> student.getCourses().stream()
.map(course -> new AbstractMap.SimpleEntry<>(
course,
student.getScores().getOrDefault(course, 0)
)))
// Group by Course Name (Key) and average the Scores (Value)
.collect(Collectors.groupingBy(
Map.Entry::getKey,
Collectors.averagingInt(Map.Entry::getValue)
));
}


// 3. Get All Unique Courses
public static Set<String> getAllUniqueCourses(List<Student> students) {
return students.stream()
.flatMap(student -> student.getCourses().stream())
.collect(Collectors.toCollection(HashSet::new));
}
public static void main(String[] args) {
// Creating Dummy Data
List<Student> batch = new ArrayList<>();
// Student 1: Alice (Full scores)
Map<String, Integer> scores1 = new HashMap<>();
scores1.put("Math", 90);
scores1.put("Physics", 85);
batch.add(new Student(101, "Alice", Arrays.asList("Math", "Physics"), scores1));