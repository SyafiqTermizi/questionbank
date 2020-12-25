import * as React from "react";
import * as ReactDom from "react-dom";

import { Sidebar } from "./Sidebar";

export const ExamForm = () => (
  <div className="row mt-3">
    <div className="col-2">
      <Sidebar />
    </div>
    <div className="col-10">
    </div>
  </div>
);

ReactDom.render(
  <ExamForm />,
  document.getElementById("exam-form")
)
