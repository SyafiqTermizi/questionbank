import * as React from "react";
import * as ReactDom from "react-dom";


const Elem = () => <h1>Hello React</h1>;

ReactDom.render(<Elem />, document.getElementById("choice-form"))