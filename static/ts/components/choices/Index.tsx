import * as React from "react";
import { useState } from "react";
import * as ReactDom from "react-dom";

import { IChoice } from "../interfaces";
import { ChoiceForm } from "./ChoiceForm";
import { ChoiceList } from "./ChoiceList";

const ChoiceFormContainer = () => {
  const initialChoice = window.choices;
  const [choices, setChoices] = useState<IChoice[]>(initialChoice);

  const deleteChoice = (id: number): void => {
    const tempChoices = [...choices];
    const filteredChoice = tempChoices.filter(choice => choice.id !== id)
    setChoices(filteredChoice);
    window.choices = filteredChoice;
  }

  const proxySetChoices = (choices: IChoice[]) => {
    setChoices(choices);
    window.choices = choices;
  }

  return (
    <>
      <ChoiceForm choices={choices} setChoices={proxySetChoices} />
      <ChoiceList choices={choices} deleteChoice={deleteChoice} />
    </>
  )
}

ReactDom.render(
  <ChoiceFormContainer />,
  document.getElementById("choice-form")
);
