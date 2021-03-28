import React from 'react';
import { useTable } from "react-table";
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

// class Table extends React.Component {
// 	constructor(props) {
// 	   super(props) //since we are extending class Table so we have to use super in order to override Component class constructor
// 	   this.state = { //state is by default an object
// 		  students: [
// 			 { id: 1, Company: 'Wasif', Address: 21, website: 'wasif@email.com', Type:'Agri Tourism',Contact:'Abishek', email:'wasif@email.com', Phone:'9941898989', Desc:'Business Description' },
// 			 { id: 2, Company: 'Ali', Address: 19, website: 'ali@email.com',Type:'Agri Tourism',Contact:'Abishek', email:'wasif@email.com', Phone:'9941898989', Desc:'Business Description' },
// 			 { id: 3, Company: 'Saad', Address: 16, website: 'saad@email.com',Type:'Agri Tourism',Contact:'Abishek', email:'wasif@email.com', Phone:'9941898989', Desc:'Business Description' },
// 			 { id: 4, Company: 'Asad', Address: 25, website: 'asad@email.com',Type:'Agri Tourism',Contact:'Abishek', email:'wasif@email.com', Phone:'9941898989', Desc:'Business Description' }
// 		  ]
// 	   }
// 	}

// 	renderTableData() {
// 		return this.state.students.map((student, index) => {
// 		   const { id, Company, Address, website,Type,Contact,email,Phone, Desc } = student //destructuring
// 		   return (
// 			  <tr key={id}>
// 				 <td>{id}</td>
// 				 <td>{Company}</td>
// 				 <td>{Address}</td>
// 				 <td>{website}</td>
// 				 <td>{Type}</td>
// 				 <td>{Contact}</td>
// 				 <td>{email}</td>
// 				 <td>{Phone}</td>
// 				 <td>{Desc}</td>
// 			  </tr>
// 		   )
// 		})
// 	 }

// 	 renderTableHeader() {
// 		let header = Object.keys(this.state.students[0])
// 		return header.map((key, index) => {
// 		   return <th key={index}>{key.toUpperCase()}</th>
// 		})
// 	 }
 
// 	render() { //Whenever our class runs, render method will be called automatically, it may have already defined in the constructor behind the scene.
// 		return (
// 			<div>
// 			   <h1 id='title'>Agri DashBoard</h1>
// 			   <table id='students'>
// 				  <tbody>
// 					 <tr>{this.renderTableHeader()}</tr>
// 					 {this.renderTableData()}
// 				  </tbody>
// 			   </table>
// 			</div>
// 		 )
// 	}
//  }


export default function Table({ columns, data }) {


	
	// Use the useTable Hook to send the columns and data to build the table
	const {
	  getTableProps, // table props from react-table
	  getTableBodyProps, // table body props from react-table
	  headerGroups, // headerGroups, if your table has groupings
	  rows, // rows for the table based on the data passed
	  prepareRow // Prepare the row (this function needs to be called for each row before getting the row props)
	} = useTable({
	  columns,
	  data
	});
  
	/* 
	  Render the UI for your table
	  - react-table doesn't have UI, it's headless. We just need to put the react-table props from the Hooks, and it will do its magic automatically
	*/
	return (
	  <table className="tablecss" {...getTableProps()}>
		<thead className="thead">
		  {headerGroups.map(headerGroup => (
			<tr className="thtrcss" {...headerGroup.getHeaderGroupProps()}>
			  {headerGroup.headers.map(column => (
				<th style={column.style} {...column.getHeaderProps()}>{column.render("Header")}</th>
			  ))}
			</tr>
		  ))}
		</thead>
		<tbody {...getTableBodyProps()}>
		  {rows.map((row, i) => {
			prepareRow(row);
			return (
			  <tr className="trcss"{...row.getRowProps()}>
				{row.cells.map(cell => {
				  return <td className="tdcss" {...cell.getCellProps()}>{cell.render("Cell")}</td>;
				})}
			  </tr>
			);
		  })}
		</tbody>
	  </table>
	);
  }