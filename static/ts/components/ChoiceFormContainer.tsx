import * as React from "react";
import { useState } from "react";
import * as ReactDom from "react-dom";

import { IChoice } from "./interfaces";
import { ChoiceForm } from "./ChoiceForm";
import { ChoiceList } from "./ChoiceList";



const ChoiceFormContainer = () => {
  const [choices, setChoices] = useState<IChoice[]>([]);

  return (
    <>
      <ChoiceForm choices={choices} setChoices={setChoices} />
      <ChoiceList choices={choices} />
    </>
  )
}

ReactDom.render(
  <ChoiceFormContainer />,
  document.getElementById("choice-form")
);
