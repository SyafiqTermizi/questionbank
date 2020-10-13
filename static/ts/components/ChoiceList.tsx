import * as React from "react";

import { IChoice } from "./interfaces";

import { CardLayout } from "../layouts/CardLayout";

interface Props {
  choices: IChoice[],
}

export const ChoiceList: React.FC<Props> = ({ choices }) => {

  const choiceList = choices.map((choice, index) => {
    const cardClass = choice.isCorrect ? "card card-accent-success" : "card" ;
    return (
      <CardLayout cardHeaderTitle="" cardClass={cardClass}>
        {choice.text}
      </CardLayout>
    )
  })

  return (
    <>
      {choiceList}
    </>
  )
}
