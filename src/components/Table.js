import React from 'react';
import '../style.css';


// class Table extends React.Component {

    

// 	render() {

// 		return (
// 			<div >
//                 Table Page
//             </div>
// 		)
// 	}
// }

// export default Table

// Table.js

class Table extends React.Component {
	constructor(props) {
	   super(props) //since we are extending class Table so we have to use super in order to override Component class constructor
	   this.state = { //state is by default an object
		  students: [
			 { id: 1, Company: 'Wasif', Address: 21, website: 'wasif@email.com', Type:'Agri Tourism',Contact:'Abishek', email:'wasif@email.com', Phone:'9941898989', Desc:'Business Description' },
			 { id: 2, Company: 'Ali', Address: 19, website: 'ali@email.com',Type:'Agri Tourism',Contact:'Abishek', email:'wasif@email.com', Phone:'9941898989', Desc:'Business Description' },
			 { id: 3, Company: 'Saad', Address: 16, website: 'saad@email.com',Type:'Agri Tourism',Contact:'Abishek', email:'wasif@email.com', Phone:'9941898989', Desc:'Business Description' },
			 { id: 4, Company: 'Asad', Address: 25, website: 'asad@email.com',Type:'Agri Tourism',Contact:'Abishek', email:'wasif@email.com', Phone:'9941898989', Desc:'Business Description' }
		  ]
	   }
	}

	renderTableData() {
		return this.state.students.map((student, index) => {
		   const { id, Company, Address, website,Type,Contact,email,Phone, Desc } = student //destructuring
		   return (
			  <tr key={id}>
				 <td>{id}</td>
				 <td>{Company}</td>
				 <td>{Address}</td>
				 <td>{website}</td>
				 <td>{Type}</td>
				 <td>{Contact}</td>
				 <td>{email}</td>
				 <td>{Phone}</td>
				 <td>{Desc}</td>
			  </tr>
		   )
		})
	 }

	 renderTableHeader() {
		let header = Object.keys(this.state.students[0])
		return header.map((key, index) => {
		   return <th key={index}>{key.toUpperCase()}</th>
		})
	 }
 
	render() { //Whenever our class runs, render method will be called automatically, it may have already defined in the constructor behind the scene.
		return (
			<div>
			   <h1 id='title'>Agri DashBoard</h1>
			   <table id='students'>
				  <tbody>
					 <tr>{this.renderTableHeader()}</tr>
					 {this.renderTableData()}
				  </tbody>
			   </table>
			</div>
		 )
	}
 }


export default Table