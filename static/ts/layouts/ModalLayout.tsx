import React from "react";

import { RowLayout } from "./Layouts";

export const ModalLayout: React.FC<{ headerText: string }> = (props) => (
  <RowLayout>
    <div
      className="modal fade"
      id="modalForm"
      tabIndex={-1}
      aria-labelledby="modalFormLabel"
      aria-hidden="true"
    >
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title" id="modalFormLabel">
              {props.headerText}
            </h5>
            <button
              type="button"
              className="close"
              data-dismiss="modal"
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          {props.children}
        </div>
      </div>
    </div>
  </RowLayout>
);
