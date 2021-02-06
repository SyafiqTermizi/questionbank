import * as React from "react";

import { RowLayout } from "./Layouts";

interface Props {
  cardClass?: string;
  cardHeaderClass?: string;
  cardTitle: string;
  cardAction?: (args: any) => void;
  cardActionClass?: string;
  cardActionText?: string;
  cardActionSecondary?: (args: any) => void;
  cardActionSecondaryClass?: string;
  cardActionSecondaryText?: string;
}

export const CardLayout: React.FC<Props> = ({
  cardClass,
  cardHeaderClass,
  cardTitle,
  cardAction,
  cardActionClass,
  cardActionText,
  children,
  cardActionSecondary,
  cardActionSecondaryClass,
  cardActionSecondaryText,
}) => (
  <RowLayout>
    <div className={cardClass ? cardClass : "card"}>
      <div className={`card-header ${cardHeaderClass}`}>
        <div className="row">
          <div className="col-6">
            <b>{cardTitle}</b>
          </div>
          <div className="col-6 text-right">
            {cardActionSecondary &&
              cardActionSecondaryClass &&
              cardActionSecondaryText && (
                <button
                  type="button"
                  data-toggle="modal"
                  data-target="#modalForm"
                  className={`mr-2 btn btn-${cardActionSecondaryClass}`}
                  onClick={cardActionSecondary}
                >
                  {cardActionSecondaryText}
                </button>
              )}
            {cardAction && cardActionClass && cardActionText && (
              <button
                className={`btn btn-${cardActionClass}`}
                onClick={cardAction}
              >
                {cardActionText}
              </button>
            )}
          </div>
        </div>
      </div>
      <div className="card-body">{children}</div>
    </div>
  </RowLayout>
);
