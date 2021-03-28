import React from 'react';
import { useEffect } from "react-table";
import {useState } from "react"
import { useTable,useFilters } from 'react-table'
import '../style.css';
import { render } from 'react-dom';



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
		getTableProps,
		getTableBodyProps,
		headerGroups,
		rows,
		prepareRow,
		setFilter // The useFilter Hook provides a way to set the filter
	  } = useTable(
		{
		  columns,
		  data
		},
		useFilters // Adding the useFilters Hook to the table
		// You can add as many Hooks as you want. Check the documentation for details. You can even add custom Hooks for react-table here
	  );

	// Create a state
	const [filterInput, setFilterInput] = useState(0);

	// Update the state when input changes
	const handleFilterChange = e => {
		const value = e.target.value || undefined;
		setFilter("name", value); // Update the show.name filter. Now our table will filter and show only the rows which have a matching value
		setFilterInput(value);
	  };
	  const handleFilterChange1 = e => {
		const value = e.target.value || undefined;
		setFilter("formatted_address", value); // Update the show.name filter. Now our table will filter and show only the rows which have a matching value
		setFilterInput(value);
	  };


	
	/* 
	  Render the UI for your table
	  - react-table doesn't have UI, it's headless. We just need to put the react-table props from the Hooks, and it will do its magic automatically
	*/

	return (
	
		<div>
		 <h2 className = "heading"> Friends of Green</h2>
		 <span>
		<label>
			Search by name:
			<input
	  	value={filterInput}
	  	onChange={handleFilterChange}
	  	placeholder="Search by name"
		/> 
		</label>
		 
		 </span>
		 <span>
		<label>
			Search by Address:
			<input
	  	value={filterInput}
	  	onChange={handleFilterChange1}
	  	placeholder="Search by name"
		/> 
		<i className="fa fa-search search-icon" aria-hidden="true"/>
		</label>
		 
		 </span>
		
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
	  </div>
	);
  }