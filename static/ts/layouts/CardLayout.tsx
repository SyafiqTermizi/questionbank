import * as React from "react";

interface Props {
  cardClass?: string;
  cardHeaderTitle: string;
}

export const CardLayout: React.FC<Props> = ({
  cardClass,
  cardHeaderTitle,
  children
}) => (
  <div className="row">
    <div className="col-12">
      <div className={cardClass? cardClass: "card"}>
        <div className="card-header">
          <b>{cardHeaderTitle}</b>
        </div>
        <div className="card-body">
          {children}
        </div>
      </div>
    </div>
  </div>  
)
