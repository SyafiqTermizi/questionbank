import * as React from "react";

import { IChoice } from "./interfaces";

interface Props {
  choices: IChoice[],
}

export const ChoiceList: React.FC<Props> = ({ choices }) => {

  const choiceList = choices.map((choice, index) => {
    const cardClass = choice.isCorrect ? "card card-accent-success" : "card" ;
    return (
      <div className="row" key={index}>
        <div className="col-12">
          <div className={cardClass}>
            <div className="card-header">
              <b>Choice {index}</b>
            </div>
            <div className="card-body">
              {choice.text}
            </div>
          </div>
        </div>
      </div>
    )
  })

  return (
    <>
      {choiceList}
    </>
  )
}
