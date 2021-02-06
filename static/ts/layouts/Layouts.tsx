import * as React from "react";

export const RowLayout: React.FC = (props) => (
  <div className="row">
    <div className="col-12">{props.children}</div>
  </div>
);
