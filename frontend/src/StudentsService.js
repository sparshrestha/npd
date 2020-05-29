import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class StudentsService{

    // constructor(){}

    getStudents() {
        const url = `${API_URL}/api/students/`;
        return axios.get(url).then(response => response.data);
    }
    getStudentsByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getStudent(pk) {
        const url = `${API_URL}/api/students/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    deleteStudent(student){
        const url = `${API_URL}/api/students/${student.pk}`;
        return axios.delete(url);
    }
    createStudent(student){
        const url = `${API_URL}/api/students/`;
        return axios.post(url,student);
    }
    updateStudent(student){
        const url = `${API_URL}/api/students/${student.pk}`;
        return axios.put(url,student);
    }
}