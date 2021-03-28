import React, { useMemo,useState, useEffect }  from 'react';
import regeneratorRuntime from "regenerator-runtime";
import Table from "./components/Table";
import axios from 'axios';
import './style.css';

// class App extends React.Component {
// 	render() {
// 		return (
// 			<div>
// 				App Content
// 			</div>
// 		);
// 	}
// }


// export default App;

function App() {

	const [loadingData, setLoadingData] = useState(true);

	const Types = ({ values }) => {
		// Loop through the array and create a badge-like component instead of a comma-separated string
		return (
		  <>
			{values.map((type, idx) => {
			  return (
				<span key={idx} className="badge">
				  {type}
				</span>
			  );
			})}
		  </>
		);
	  };
	  

	const columns = useMemo(
		() => [
		  {
			// first group - TV Show
			Header: "Agri Dashboard",
			// First group columns
			columns: [
			  {
				Header: "Name",
				accessor: "name"

			  },
			  {
				Header: "Address",
				accessor: "formatted_address"
			  },
			  {
				Header: "Contact Information",
				accessor: "placeJson.result.international_phone_number"

			  },
			  {
				Header: "Location",
				accessor: "placeJson.result.url"

			  },

			  {
				Header: "Type",
				accessor: "types",
				Cell: ({ cell: { value } }) => <Types values={value} />
			  },
			  {
				Header: "Website",
				accessor: "placeJson.result.website"

			  }
			]
		  }
		],
		[]
	  );

	// data state to store the TV Maze API data. Its initial value is an empty array
	const [data, setData] = useState([]);
  
	// Using useEffect to call the API once mounted and set the data
	useEffect(() => {
		async function getData() {
		  await axios
			.get("http://13.88.227.190/fog/Get_Business/")
			.then((response) => {
			  // check if the data is populated
			  console.log(response.data);
			  setData(response.data);
			  // you tell it that you had the result
			  setLoadingData(false);
			});
		}
  
		if (loadingData) {
			// if the result is not ready so you make the axios call
			getData();
		  }
		}, []);

		return (
			<div className="App">
			  {/* here you check if the state is loading otherwise if you wioll not call that you will get a blank page because the data is an empty array at the moment of mounting */}
			  {loadingData ? (
				<p>Loading Please wait...</p>
			  ) : (
				<Table columns={columns} data={data} />
			  )}
			</div>
		  );
		}
  
  export default App;