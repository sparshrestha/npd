import  React, { Component } from  'react';
import  StudentsService  from  './StudentsService';

const  studentsService  =  new  StudentsService();

class  StudentsList  extends  Component {

constructor(props) {
    super(props);
    this.state  = {
        students: [],
        nextPageURL:  ''
    };
    this.nextPage  =  this.nextPage.bind(this);
    this.handleDelete  =  this.handleDelete.bind(this);
}

componentDidMount() {
    var  self  =  this;
    studentsService.getStudents().then(function (result) {
        console.log(result);
        self.setState({ students:  result.data, nextPageURL:  result.nextlink})
    });
}
handleDelete(e,pk){
    var  self  =  this;
    studentsService.deleteStudent({pk :  pk}).then(()=>{
        var  newArr  =  self.state.students.filter(function(obj) {
            return  obj.pk  !==  pk;
        });

        self.setState({students:  newArr})
    });
}

nextPage(){
    var  self  =  this;
    console.log(this.state.nextPageURL);
    studentsService.getStudentsByURL(this.state.nextPageURL).then((result) => {
        self.setState({ students:  result.data, nextPageURL:  result.nextlink})
    });
}
render() {

    return (
        <div  className="customers--list">
            <table  className="table">
            <thead  key="thead">
            <tr>
                <th>#</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Phone</th>
                <th>Email</th>
                <th>Address</th>
                <th>Description</th>
                <th>Actions</th>
            </tr>
            </thead>
            <tbody>
            {this.state.students.map( c  =>
                <tr  key={c.pk}>
                <td>{c.pk}  </td>
                <td>{c.first_name}</td>
                <td>{c.last_name}</td>
                <td>{c.phone}</td>
                <td>{c.email}</td>
                <td>{c.address}</td>
                <td>{c.description}</td>
                <td>
                <button  onClick={(e)=>  this.handleDelete(e,c.pk) }> Delete</button>
                <a  href={"/student/" + c.pk}> Update</a>
                </td>
            </tr>)}
            </tbody>
            </table>
            <button  className="btn btn-primary"  onClick=  {  this.nextPage  }>Next</button>
        </div>
        );
  }
}
export  default  StudentsList;