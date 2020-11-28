import * as React from "react";

import { IChoice } from "../interfaces";
import { CardLayout } from "../../layouts/CardLayout";

interface Props {
  choices: IChoice[],
  deleteChoice: (id: number) => void;
}

export const ChoiceList: React.FC<Props> = ({ choices, deleteChoice }) => {

  const choiceList = choices.map((choice) => {
    const cardClass = choice.isCorrect ? "card card-accent-success border-success" : "card";
    return (
      <CardLayout
        cardTitle=""
        cardClass={cardClass}
        cardHeaderClass={choice.isCorrect? "bg-success":""}
        key={choice.id}
        cardAction={() => deleteChoice(choice.id)}
        cardActionClass="danger"
        cardActionText="delete"
      >
        <div dangerouslySetInnerHTML={ { __html: choice.text } }></div>
      </CardLayout>
    )
  })

  return (
    <>
      {choiceList}
    </>
  )
}

