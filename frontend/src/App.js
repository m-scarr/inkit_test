import React, { Component } from 'react'
import axios from "axios"

export default class App extends Component {
  state = { docInfo: "" }

  componentDidMount() {
    axios.defaults.baseURL = "http://localhost:8000"
    axios.get("/docInfo").then((res) => {
      this.setState({ docInfo: JSON.stringify(res.data).split("{").join("{\n\t").split(",").join(",\n\t").split("}").join("\n}") })
    })
  }

  render() {
    return (
      <pre>
        <code>
          {this.state.docInfo}
        </code>
      </pre>
    )
  }
}

