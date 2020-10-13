import * as React from "react";

interface Props {
  cardClass?: string;
  cardTitle: string;
  cardAction?: (args: any) => void;
  cardActionClass?: string;
  cardActionText?: string;
}

export const CardLayout: React.FC<Props> = ({
  cardClass,
  cardTitle,
  cardAction,
  cardActionClass,
  cardActionText,
  children
}) => (
  <div className="row">
    <div className="col-12">
      <div className={cardClass? cardClass: "card"}>
        <div className="card-header">
          <div className="row">
            <div className="col-6">
              <b>{cardTitle}</b>
            </div>
            <div className="col-6 text-right">
              {
                cardAction && cardActionClass && cardActionText && 
                  <button
                    className={`btn btn-outline-${cardActionClass}`}
                    onClick={cardAction}
                  >
                    {cardActionText}
                  </button>
              }
            </div>
          </div>
        </div>
        <div className="card-body">
          {children}
        </div>
      </div>
    </div>
  </div>  
)
