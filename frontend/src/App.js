import React, { Component } from 'react'
import axios from "axios"

export default class App extends Component {
  state = { response: "" }

  componentDidMount() {
    axios.get("http://localhost:8000/").then((response) => {
      this.setState({ response: JSON.stringify(response.data).split("{").join("{\n\t").split(",").join(",\n\t").split("}").join("\n}") })
    }).catch((err) => {
      console.log(err)
    })
  }
  
  render() {
    return (
      <pre>
        <code>
          {this.state.response}
        </code>
      </pre>
    )
  }
}

