

import { useState } from 'react'
import axios from "axios";
import logo from './logo.svg';
import './App.css';

function App() {
    document.body.style = "background-color: #3F3F4F;"

    // new line start
    const [profileData, setProfileData] = useState(null)

    /*function getData() {
        axios({
                  method: "GET",
                  url:"/profile",
        })
                .then((response) => {
                    const res =response.data
                    setProfileData(({
                        profile_name: res.name,
                        about_me: res.about}))
                }).catch((error) => {
                if (error.response) {
                    console.log(error.response)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                }})}*/
  //end of new line

    function selectBondrewd()
    {
        axios({
            method: "GET",
            url:"/bondrewd",
        }).then((response) => {
            console.log(response)
        })
    }

    function selectAinz()
    {
        axios({
            method: "GET",
            url:"/ainz",
        }).then((response) => {
            console.log(response)
        })
    }

    return (
        <div className="App">
            <form action="/post" method="post" target="output">
                <label>
                    Enter your prompt here.
                    <input type="text" name="prompt"/>
                </label>
                <input type="submit"/>
            </form>

            <button onClick={selectBondrewd}>Select Bondrewd</button>
            <button onClick={selectAinz}>Select Ainz</button>

              <iframe name="output" />
        </div>
    );
}

export default App;



